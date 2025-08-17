from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QListWidget, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush, QFont
from cfg import config
from docx import Document
import os

class MergeWindow(QMainWindow):  # Изменили наследование
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Merge module")
        self.setGeometry(200, 200, 1000, 700)
        self.setWindowIcon(QIcon(":/icons/merge"))
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
    
    def initUI(self):
        layout = QVBoxLayout()
        
        # Список документов
        self.list_docs = QListWidget()
        layout.addWidget(self.list_docs)
        
        # Кнопки управления
        btn_layout = QHBoxLayout()
        
        self.btn_add = QPushButton("Add Documents")
        self.btn_remove = QPushButton("Remove Selected")
        self.btn_merge = QPushButton("Merge Documents")
        
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_remove)
        btn_layout.addWidget(self.btn_merge)
        
        layout.addLayout(btn_layout)
        
        # Подключение кнопок
        self.btn_add.clicked.connect(self.add_documents)
        self.btn_remove.clicked.connect(self.remove_selected)
        self.btn_merge.clicked.connect(self.merge_documents)
        
        self.setLayout(layout)
    
    def add_documents(self):
        default_dir = config.get('default_data_dir')
        file_paths, _ = QFileDialog.getOpenFileNames(
            self, 
            "Select Documents", 
            default_dir, 
            "Word Documents (*.docx)"
        )
        
        if file_paths:
            self.documents.extend(file_paths)
            self.list_docs.addItems(file_paths)
    
    def remove_selected(self):
        for item in self.list_docs.selectedItems():
            self.documents.remove(item.text())
            self.list_docs.takeItem(self.list_docs.row(item))
    
    def merge_documents(self):
        if len(self.documents) < 2:
            QMessageBox.warning(self, "Warning", "Please select at least 2 documents to merge")
            return
        
        try:
            # Создаем новый документ
            merged_doc = Document()
            
            # Проходим по каждому файлу и добавляем его содержимое
            for doc_path in self.documents:
                doc = Document(doc_path)
                for element in doc.element.body:
                    merged_doc.element.body.append(element)
            
            # Сохраняем
            default_dir = config.get('default_merge_dir')
            file_path, _ = QFileDialog.getSaveFileName(
                self, 
                "Save Merged Document", 
                os.path.join(default_dir, "merged_document.docx"), 
                "Word Documents (*.docx)"
            )
            
            if file_path:
                merged_doc.save(file_path)
                QMessageBox.information(self, "Success", f"Documents merged successfully:\n{file_path}")
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to merge documents:\n{str(e)}")