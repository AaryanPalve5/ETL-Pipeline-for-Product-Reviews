import pandas as pd
import requests


def extract_csv(file_path):
    return pd.read_csv(file_path)


def extract_json(file_path):
    with open(file_path, 'r') as f:
        return pd.read_json(f)
 
def extract_txt(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
     
    data = [line.strip().split('|') for line in lines]
    return pd.DataFrame(data, columns=['review_id', 'product_id', 'customer_id', 'rating', 'review_date', 'review_text'])
