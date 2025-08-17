from PyQt5.QtWidgets import (QMainWindow, QPushButton, QVBoxLayout, QWidget, 
                             QLabel, QHBoxLayout, QFrame, QSizePolicy)
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt, QSize
from cfg import config, APP_NAME, APP_VERSION, APP_AUTHOR
import sys

class MainApp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"{APP_NAME} v{APP_VERSION}")
        self.setGeometry(100, 100, 1000, 700)
        self.setMinimumSize(800, 600)
        
        # Установка иконки приложения
        self.setWindowIcon(QIcon(":/icons/app_icon"))
        
        self.initUI()
    
    def initUI(self):
        # Центральный виджет с вертикальным расположением
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(30)
        
        # Заголовок приложения
        title_layout = QVBoxLayout()
        title_layout.setAlignment(Qt.AlignCenter)
        
        app_title = QLabel(APP_NAME)
        app_title.setFont(QFont("Arial", 28, QFont.Bold))
        app_title.setStyleSheet("color: #2c3e50;")
        title_layout.addWidget(app_title)
        
        version_label = QLabel(f"Version {APP_VERSION}")
        version_label.setFont(QFont("Arial", 10))
        version_label.setStyleSheet("color: #7f8c8d;")
        title_layout.addWidget(version_label)
        
        main_layout.addLayout(title_layout)
        
        # Кнопки навигации (центрированные)
        buttons_layout = QHBoxLayout()
        buttons_layout.setAlignment(Qt.AlignCenter)
        
        # Создаем кнопки в стиле карточек
        self.btn_plot = self.create_nav_button("Graphic Plot", ":/icons/chart")
        self.btn_report = self.create_nav_button("Reporter", ":/icons/report")
        self.btn_merge = self.create_nav_button("Doc Merge", ":/icons/merge")
        self.btn_settings = self.create_nav_button("Settings", ":/icons/settings")
        
        buttons_layout.addWidget(self.btn_plot)
        buttons_layout.addWidget(self.btn_report)
        buttons_layout.addWidget(self.btn_merge)
        buttons_layout.addWidget(self.btn_settings)
        
        main_layout.addLayout(buttons_layout)
        
        # Нижний колонтитул
        footer_layout = QHBoxLayout()
        footer_layout.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        
        author_label = QLabel(f"© {APP_AUTHOR}")
        author_label.setFont(QFont("Arial", 9))
        author_label.setStyleSheet("color: #95a5a6;")
        footer_layout.addWidget(author_label)
        
        main_layout.addLayout(footer_layout)
        
        # Подключение кнопок
        self.btn_plot.clicked.connect(self.open_plot)
        self.btn_report.clicked.connect(self.open_report)
        self.btn_merge.clicked.connect(self.open_merge)
        self.btn_settings.clicked.connect(self.open_settings)
        
        # Установка фонового изображения
        self.set_background()
    
    def create_nav_button(self, text, icon_path):
        """Создает стилизованную кнопку навигации"""
        button = QPushButton(text)
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(48, 48))
        button.setMinimumSize(192, 108)
        button.setFont(QFont("Arial", 12, QFont.Bold))
        button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 3px;
                padding: 30px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #708090;
            }
        """)
        return button
    
    def set_background(self):
        """Устанавливает фоновое изображение"""
        # Замените путь на актуальный путь к вашему изображению
        bg_path = ":/backgrounds/main_bg"
        try:
            pixmap = QPixmap(bg_path)
            if not pixmap.isNull():
                palette = self.palette()
                palette.setBrush(QPalette.Window, QBrush(pixmap.scaled(
                    self.size())))#, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
                self.setPalette(palette)
        except:
            # Фоллбэк на обычный фон
            self.setStyleSheet("background-color: #ecf0f1;")
    
    def resizeEvent(self, event):
        """Обработчик изменения размера окна"""
        self.set_background()
        super().resizeEvent(event)
    
    def open_plot(self):
        print(" plot window encountered ")
        from .plot_module import PlotWindow
        self.plot_window = PlotWindow()
        self.plot_window.show()
    
    def open_report(self):
        print(" report window encountered ")
        from .report_module import ReportWindow
        self.report_window = ReportWindow()
        self.report_window.show()
    
    def open_merge(self):
        print(" merge window encountered ")
        from .merge_module import MergeWindow
        self.merge_window = MergeWindow()
        self.merge_window.show()
    
    def open_settings(self):
        print(" settings window encountered ")
        from .settings_module import SettingsWindow
        self.settings_window = SettingsWindow()
        self.settings_window.show()