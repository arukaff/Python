# Дополнительные зависимости:
# pip install sentence-transformers faiss-cpu openai


import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Dict
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import re
import pdfplumber
import spacy
from nltk.corpus import stopwords
from typing import List, Tuple


#  Извлечение текста из PDF
def extract_text_from_pdf(pdf_path: str) -> Tuple[str, dict]:
    """
    Извлекает текст из PDF-файла и возвращает его с метаданными
    Возвращает: (текст, {метаданные})
    """
    full_text = []
    metadata = {
        'source': pdf_path,
        'total_pages': 0,
        'errors': []
    }

    try:
        with pdfplumber.open(pdf_path) as pdf:
            metadata['total_pages'] = len(pdf.pages)
            
            for page_num, page in enumerate(pdf.pages, 1):
                try:
                    text = page.extract_text()
                    if text:
                        full_text.append(f"{text}\n[Страница {page_num}]\n")
                    else:
                        metadata['errors'].append(f"Пустая страница {page_num}")
                except Exception as e:
                    metadata['errors'].append(f"Ошибка на странице {page_num}: {str(e)}")
                    
            return '\n'.join(full_text), metadata
            
    except Exception as e:
        metadata['errors'].append(f"Фатальная ошибка: {str(e)}")
        return '', metadata

#  Предобработка текста
class TextPreprocessor:
    def __init__(self):
        # Загрузка модели Spacy для русского языка
        self.nlp = spacy.load('ru_core_news_sm')
        
        # Стоп-слова для русского языка
        self.stopwords = set(stopwords.words('russian'))
        self.custom_stopwords = {'это', 'весь', 'который', 'такой'}
        self.stopwords.update(self.custom_stopwords)

    def clean_text(self, text: str) -> str:
        """Очистка текста"""
        # Удаление специальных символов и чисел
        text = re.sub(r'[^\w\s]|\d+|[_]', ' ', text, flags=re.UNICODE)
        # Приведение к нижнему регистру
        text = text.lower()
        # Удаление лишних пробелов
        return re.sub(r'\s+', ' ', text).strip()

    def tokenize(self, text: str) -> List[str]:
        """Токенизация и лемматизация"""
        doc = self.nlp(text)
        return [
            token.lemma_ for token in doc
            if not token.is_punct
            and not token.is_space
            and token.lemma_ not in self.stopwords
        ]

    def chunk_text(self, text: str, chunk_size: int = 512, overlap: int = 64) -> List[dict]:
        """Разбивка текста на чанки с перекрытием"""
        cleaned_text = self.clean_text(text)
        tokens = self.tokenize(cleaned_text)
        
        chunks = []
        pos = 0
        
        while pos < len(tokens):
            end_pos = pos + chunk_size
            chunk = tokens[pos:end_pos]
            
            # Извлечение оригинального контекста (сохраняем страницы)
            context_start = max(0, pos - overlap)
            context_end = min(len(tokens), end_pos + overlap)
            context = tokens[context_start:context_end]
            
            # Сохранение информации о позиции
            chunks.append({
                'text': ' '.join(chunk),
                'context': ' '.join(context),
                'start_pos': pos,
                'end_pos': end_pos
            })
            pos += chunk_size - overlap
            
        return chunks
    
#  Класс для работы с эмбеддингами
class EmbeddingProcessor:
    def __init__(self, model_name: str = 'paraphrase-multilingual-mpnet-base-v2'):
        self.model = SentenceTransformer(model_name)
        self.embedding_dim = 768  # Размерность для выбранной модели

    def generate_embeddings(self, texts: List[str]) -> np.ndarray:
        return self.model.encode(texts, convert_to_tensor=False)

#  Векторная база данных
class VectorDatabase:
    def __init__(self, embedding_dim: int):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.metadata = []
        
    def add_embeddings(self, embeddings: np.ndarray, metadata: List[Dict]):
        self.index.add(embeddings)
        self.metadata.extend(metadata)
        
    def search(self, query_embedding: np.ndarray, k: int = 5) -> List[Dict]:
        distances, indices = self.index.search(query_embedding, k)
        return [{
            'score': float(distances[0][i]),
            'text': self.metadata[idx]['text'],
            'page': self.metadata[idx]['page'],
            'context': self.metadata[idx]['context']
        } for i, idx in enumerate(indices[0])]


#  Класс для генерации ответов с локальной моделью
class RAGProcessor:
    def __init__(self, embedding_processor, vector_db, model_name: str = "IlyaGusev/saiga_llama3_8b"):
        self.embedding_processor = embedding_processor
        self.vector_db = vector_db
        
        # Инициализация модели и токенизатора
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            trust_remote_code=True,
            device_map="auto"
        )
        
        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=-1
            # device_map="auto"
        )

    def _format_prompt(self, context: str, question: str) -> str:
        """Форматирование промпта для модели Saiga"""
        return (
            f"<SC6>Пользователь: Используя следующий контекст, ответь на вопрос. "
            f"Если ответа нет в контексте, скажи 'Не могу найти ответ'.\n\n"
            f"Контекст: {context}\n\n"
            f"Вопрос: {question}\n"
            "Помощник:"
        )

    def generate_answer(self, query: str, max_context_length: int = 2000) -> Dict:
        # Поиск релевантных чанков
        query_embedding = self.embedding_processor.generate_embeddings([query])
        results = self.vector_db.search(query_embedding)
        
        # Формирование контекста с учетом ограничений модели
        context_parts = []
        current_length = 0
        for res in results:
            context_part = f"[Страница {res['page']}]: {res['context']}"
            if current_length + len(context_part) > max_context_length:
                break
            context_parts.append(context_part)
            current_length += len(context_part)
        
        full_context = "\n".join(context_parts)
        
        # Генерация промпта
        prompt = self._format_prompt(full_context, query)
        
        # Генерация ответа
        try:
            response = self.generator(
                prompt,
                max_new_tokens=500,
                do_sample=True,
                temperature=0.3,
                top_p=0.9,
                repetition_penalty=1.1,
                eos_token_id=self.tokenizer.eos_token_id,
            )
            
            answer = response[0]['generated_text'].split("Помощник:")[-1].strip()
            answer = answer.split("</s>")[0].strip()
            
            # Очистка ответа от технических артефактов
            answer = re.sub(r"<.*?>|\[.*?\]", "", answer)
            
        except Exception as e:
            answer = f"Ошибка генерации: {str(e)}"
        
        sources = list(set([res['page'] for res in results[:3]]))
        
        return {
            'answer': answer,
            'sources': sources,
            'used_context': context_parts
        }



if __name__ == "__main__":
    # Инициализация компонентов
    embedder = EmbeddingProcessor()
    vector_db = VectorDatabase(embedder.embedding_dim)
    rag = RAGProcessor(embedder, vector_db)

    # 1. Обработка PDF и создание чанков
    text, metadata = extract_text_from_pdf("example.pdf")
    preprocessor = TextPreprocessor()
    chunks = preprocessor.chunk_text(text)
    
    # 2. Генерация эмбеддингов и заполнение БД
    chunk_texts = [chunk['text'] for chunk in chunks]
    embeddings = embedder.generate_embeddings(chunk_texts)
    
    # Извлечение номеров страниц из оригинального текста
    chunk_metadata = []
    for chunk in chunks:
        page_match = re.search(r'\[Страница (\d+)\]', chunk['context'])
        page = int(page_match.group(1)) if page_match else 0
        chunk_metadata.append({
            'text': chunk['text'],
            'context': chunk['context'],
            'page': page
        })
    
    vector_db.add_embeddings(embeddings, chunk_metadata)
    
    # 3. Пример запроса
    query = "Какие основные выводы представлены в документе?"
    result = rag.generate_answer(query)
    
    print("\nРезультат поиска:")
    print(f"Вопрос: {query}")
    print(f"Ответ: {result['answer']}")
    print(f"Источники: Страницы {result['sources']}")
    print("\nИспользованный контекст:")
    for ctx in result['used_context'][:2]:  # Покажем часть контекста
        print(f"- {ctx[:150]}...")