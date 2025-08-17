import json
from pathlib import Path
from path_manager import path_manager

APP_NAME = "Report tool kit"
APP_VERSION = "1.0.0"
APP_AUTHOR = "RG"

# Настройки по умолчанию
DEFAULT_CONFIG = {
    'recent_files': [],
    'plot_style': 'ggplot',
    'cache_size': 100,
    'default_data_dir': str(Path.home()),
    'default_save_dir': str(Path.home()),
    'default_cache_dir': str(path_manager.CACHE_DIR),
    'default_fig_dir': str(path_manager.OUT_DIR / "fig"),
    'default_rpt_dir': str(path_manager.OUT_DIR / "rpt"),
    'default_merge_dir': str(path_manager.OUT_DIR / "rpt" / "merge")
}

class Config:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._config_path = path_manager.SRC_DIR / 'config.json'
            cls._instance.settings = DEFAULT_CONFIG.copy()
            cls._instance.load()
        return cls._instance
    
    def load(self):
        """Загрузка конфигурации из файла"""
        try:
            if self._config_path.exists():
                with open(self._config_path, 'r') as f:
                    self.settings = json.load(f)
        except:
            self.settings = DEFAULT_CONFIG.copy()
    
    def save(self):
        """Сохранение конфигурации в файл"""
        with open(self._config_path, 'w') as f:
            json.dump(self.settings, f, indent=4)
    
    def get(self, key):
        return self.settings.get(key)
    
    def set(self, key, value):
        self.settings[key] = value
        self.save()

# Глобальный доступ к конфигурации
config = Config()