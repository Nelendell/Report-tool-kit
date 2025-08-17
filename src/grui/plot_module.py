from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush, QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from wwfl.data_load import load_dataset
from grplt.plotter import create_plot
from cfg import config
import os

class PlotWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Plot module")
        self.setGeometry(200, 200, 1000, 700)
        self.setWindowIcon(QIcon(":/icons/chart"))

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
    
    def initUI(self):
        layout = QVBoxLayout()
        
        # Панель управления
        control_layout = QHBoxLayout()
        
        self.btn_load = QPushButton("Load Data")
        self.btn_plot = QPushButton("Plot Data")
        self.btn_save = QPushButton("Save Figure")
        
        control_layout.addWidget(self.btn_load)
        control_layout.addWidget(self.btn_plot)
        control_layout.addWidget(self.btn_save)
        
        # Подключение кнопок
        self.btn_load.clicked.connect(self.load_data)
        self.btn_plot.clicked.connect(self.generate_plot)
        self.btn_save.clicked.connect(self.save_figure)
        
        # Область для графика
        self.plot_widget = QWidget()
        plot_layout = QVBoxLayout(self.plot_widget)
        self.plot_layout = plot_layout
        
        layout.addLayout(control_layout)
        layout.addWidget(self.plot_widget, 1)
        
        self.setLayout(layout)
    
    def load_data(self):
        default_dir = config.get('default_data_dir')
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Open Data File", 
            default_dir, 
            "CSV Files (*.csv);;Excel Files (*.xlsx);;All Files (*)"
        )
        
        if file_path:
            self.current_data = load_dataset(file_path)
    
    def generate_plot(self):
        if self.current_data is not None:
            # Создаем график
            fig = create_plot(self.current_data)
            
            # Очищаем предыдущий график
            if self.canvas:
                self.plot_layout.removeWidget(self.canvas)
                self.canvas.deleteLater()
            
            # Отображаем новый график
            self.canvas = FigureCanvas(fig)
            self.figure = fig  # сохраняем ссылку
            self.plot_layout.addWidget(self.canvas)
            self.canvas.draw()
    
    def save_figure(self):
        if self.figure:
            default_dir = config.get('default_fig_dir')
            file_path, _ = QFileDialog.getSaveFileName(
                self, 
                "Save Figure", 
                os.path.join(default_dir, "plot.png"), 
                "PNG Files (*.png);;PDF Files (*.pdf);;SVG Files (*.svg)"
            )
            
            if file_path:
                self.figure.savefig(file_path, dpi=300)