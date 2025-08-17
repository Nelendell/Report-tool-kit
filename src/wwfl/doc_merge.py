from docx import Document
import os

def merge_documents(file_paths, output_path):
    """
    Объединяет несколько DOCX-файлов в один
    
    :param file_paths: Список путей к файлам для объединения
    :param output_path: Путь для сохранения результата
    """
    if not file_paths:
        raise ValueError("No documents to merge")
    
    # Создаем новый документ
    merged_doc = Document()
    
    # Проходим по каждому файлу и добавляем его содержимое
    for doc_path in file_paths:
        if not os.path.exists(doc_path):
            raise FileNotFoundError(f"Document not found: {doc_path}")
            
        doc = Document(doc_path)
        
        # Копируем все элементы документа
        for element in doc.element.body:
            merged_doc.element.body.append(element)
    
    # Сохраняем результат
    merged_doc.save(output_path)
    return output_path