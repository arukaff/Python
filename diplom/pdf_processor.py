# Установите зависимости:
# pip install pdfplumber spacy nltk
# python -m spacy download ru_core_news_sm

import re
import pdfplumber
import spacy
from nltk.corpus import stopwords
from typing import List, Tuple

# 1. Извлечение текста из PDF
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

# 2. Предобработка текста
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

# Пример использования
if __name__ == "__main__":
    # Извлечение текста
    text, metadata = extract_text_from_pdf("example.pdf")
    
    if text:
        print(f"Успешно извлечено {metadata['total_pages']} страниц")
        print(f"Ошибки: {metadata['errors']}\n")
        
        # Предобработка
        preprocessor = TextPreprocessor()
        chunks = preprocessor.chunk_text(text)
        
        print(f"Создано {len(chunks)} чанков:")
        for i, chunk in enumerate(chunks[:3], 1):  # Выводим первые 3 чанка
            print(f"\nЧанк {i}:")
            print(chunk['text'][:200] + "...")  # Показываем начало чанка
    else:
        print("Не удалось извлечь текст. Ошибки:")
        for error in metadata['errors']:
            print(f"- {error}")