from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QFormLayout, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush, QFont
from cfg import config

class SettingsWindow(QMainWindow):  # Изменили наследование
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings module")
        self.setGeometry(200, 200, 1000, 700)
        self.setWindowIcon(QIcon(":/icons/settings"))
        
        # Центральный виджет

        self.initUI()
    
    def initUI(self):

        print("---")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        print("---")
        layout = QFormLayout(central_widget)
        print("---")
        # Поля для путей
        self.edit_data_dir = QLineEdit()
        self.edit_save_dir = QLineEdit()
        self.edit_cache_dir = QLineEdit()
        self.edit_fig_dir = QLineEdit()
        self.edit_rpt_dir = QLineEdit()
        self.edit_merge_dir = QLineEdit()
        
        # Кнопки обзора
        self.btn_browse_data = QPushButton("Browse...")
        self.btn_browse_save = QPushButton("Browse...")
        self.btn_browse_cache = QPushButton("Browse...")
        self.btn_browse_fig = QPushButton("Browse...")
        self.btn_browse_rpt = QPushButton("Browse...")
        self.btn_browse_merge = QPushButton("Browse...")
        
        # Подключаем кнопки
        self.btn_browse_data.clicked.connect(lambda: self.browse_directory(self.edit_data_dir))
        self.btn_browse_save.clicked.connect(lambda: self.browse_directory(self.edit_save_dir))
        self.btn_browse_cache.clicked.connect(lambda: self.browse_directory(self.edit_cache_dir))
        self.btn_browse_fig.clicked.connect(lambda: self.browse_directory(self.edit_fig_dir))
        self.btn_browse_rpt.clicked.connect(lambda: self.browse_directory(self.edit_rpt_dir))
        self.btn_browse_merge.clicked.connect(lambda: self.browse_directory(self.edit_merge_dir))
        
        # Добавляем поля и кнопки в форму
        layout.addRow("Default Data Directory:", self.create_browse_row(self.edit_data_dir, self.btn_browse_data))
        layout.addRow("Default Save Directory:", self.create_browse_row(self.edit_save_dir, self.btn_browse_save))
        layout.addRow("Cache Directory:", self.create_browse_row(self.edit_cache_dir, self.btn_browse_cache))
        layout.addRow("Figures Directory:", self.create_browse_row(self.edit_fig_dir, self.btn_browse_fig))
        layout.addRow("Reports Directory:", self.create_browse_row(self.edit_rpt_dir, self.btn_browse_rpt))
        layout.addRow("Merged Documents Directory:", self.create_browse_row(self.edit_merge_dir, self.btn_browse_merge))
        
        # Кнопка сохранения
        self.btn_save = QPushButton("Save Settings")
        self.btn_save.clicked.connect(self.save_settings)
        layout.addRow(self.btn_save)
        
        # Загружаем текущие настройки
        self.load_settings()
        
        self.setLayout(layout)
    
    def create_browse_row(self, line_edit, button):
        widget = QWidget()
        hlayout = QHBoxLayout(widget)
        hlayout.addWidget(line_edit)
        hlayout.addWidget(button)
        hlayout.setContentsMargins(0, 0, 0, 0)
        return widget
    
    def browse_directory(self, line_edit):
        dir_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if dir_path:
            line_edit.setText(dir_path)
    
    def load_settings(self):
        self.edit_data_dir.setText(config.get('default_data_dir'))
        self.edit_save_dir.setText(config.get('default_save_dir'))
        self.edit_cache_dir.setText(config.get('default_cache_dir'))
        self.edit_fig_dir.setText(config.get('default_fig_dir'))
        self.edit_rpt_dir.setText(config.get('default_rpt_dir'))
        self.edit_merge_dir.setText(config.get('default_merge_dir'))
    
    def save_settings(self):
        config.set('default_data_dir', self.edit_data_dir.text())
        config.set('default_save_dir', self.edit_save_dir.text())
        config.set('default_cache_dir', self.edit_cache_dir.text())
        config.set('default_fig_dir', self.edit_fig_dir.text())
        config.set('default_rpt_dir', self.edit_rpt_dir.text())
        config.set('default_merge_dir', self.edit_merge_dir.text())
        
        QMessageBox.information(self, "Settings Saved", "All settings have been saved successfully!")