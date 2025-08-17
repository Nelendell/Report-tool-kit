import os
import sys
from pathlib import Path

class PathManager:
    def __init__(self):
        self.APP_DIR = Path(__file__).resolve().parent.parent
        self.SRC_DIR = self.APP_DIR / 'src'
        self.CACHE_DIR = self.APP_DIR / 'cache'
        self.OUT_DIR = self.APP_DIR / 'out'
        
        # Создание директорий при инициализации
        self.CACHE_DIR.mkdir(exist_ok=True)
        self.OUT_DIR.mkdir(exist_ok=True)
        
        # Добавление в пути импорта
        sys.path.append(str(self.SRC_DIR))

        print(" ___ roots loading -> ")
        print(f"src   directory: {self.SRC_DIR}  ")
        print(f"out   directory: {self.OUT_DIR}  ")
        print(f"cache directory: {self.CACHE_DIR}")
        print("___  roots loaded  ___")

    def get(self, name):
        return getattr(self, f"{name}_DIR", None)

# Синглтон для доступа из любых модулей
path_manager = PathManager()