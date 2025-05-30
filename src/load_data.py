import pandas as pd
from src.utils import get_data_path

def load_nobel_data(filename="nobel.csv"):
    data_path = get_data_path(filename)
    return pd.read_csv(data_path)
