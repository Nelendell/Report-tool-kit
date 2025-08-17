import pandas as pd
from path_manager import path_manager

def load_dataset(file_path):
    
    # Реальная загрузка данных
    data = pd.read_csv(file_path)

    return data