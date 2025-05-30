# app.py
from flask import Flask, render_template, request, jsonify
import os
import uuid
import rag_processor as rag

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp_pdfs'

# Инициализация модели
embedder = rag.EmbeddingProcessor()
vector_db = rag.VectorDatabase(embedder.embedding_dim)
rag = rag.RAGProcessor(embedder, vector_db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Сохраняем файл временно
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    filename = str(uuid.uuid4()) + ".pdf"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    # Обработка PDF
    text, metadata = rag.extract_text_from_pdf(filepath)
    preprocessor = rag.TextPreprocessor()
    chunks = preprocessor.chunk_text(text)
    
    # Обновляем векторную БД
    chunk_texts = [chunk['text'] for chunk in chunks]
    embeddings = embedder.generate_embeddings(chunk_texts)
    
    chunk_metadata = []
    for chunk in chunks:
        page_match = rag.re.search(r'\[Страница (\d+)\]', chunk['context'])
        page = int(page_match.group(1)) if page_match else 0
        chunk_metadata.append({
            'text': chunk['text'],
            'context': chunk['context'],
            'page': page
        })
    
    vector_db.add_embeddings(embeddings, chunk_metadata)
    
    return jsonify({
        'message': 'File processed successfully',
        'pages': metadata['total_pages']
    })

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    query = data.get('query', '')
    
    if not query:
        return jsonify({'error': 'Empty query'}), 400
    
    result = rag.generate_answer(query)
    return jsonify({
        'answer': result['answer'],
        'sources': result['sources'],
        'contexts': result['used_context']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)