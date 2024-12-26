import os
import pandas as pd
import sqlite3
from extract import extract_csv, extract_json, extract_txt
from transform import normalize_data, clean_data, add_sentiment_column
from load import load_to_db, execute_query

def calculate_summaries(df: pd.DataFrame) -> tuple:
    avg_ratings = df.groupby('product_id')['rating'].mean().reset_index()
    avg_ratings.columns = ['product_id', 'average_rating']
    
    sentiment_by_product = df.groupby('product_id')['sentiment'].mean().reset_index()
    positive_products = sentiment_by_product.nlargest(3, 'sentiment')
    negative_products = sentiment_by_product.nsmallest(3, 'sentiment')
    
    return avg_ratings, positive_products, negative_products

def run_etl():
    source_a_file = os.path.join('data', 'source_a.csv')
    source_b_file = os.path.join('data', 'source_b.json')
    source_c_file = os.path.join('data', 'source_c.txt')
    db_path = 'product_reviews.db'
    
    print("Extracting data from sources...")
    df_a = extract_csv(source_a_file)
    df_b = extract_json(source_b_file)
    df_c = extract_txt(source_c_file)
    
    df = pd.concat([df_a, df_b, df_c], ignore_index=True)
    df = normalize_data(df)
    df = clean_data(df)
    df = add_sentiment_column(df)
    
    avg_ratings, positive_products, negative_products = calculate_summaries(df)
    
    with sqlite3.connect(db_path) as conn:
        avg_ratings.to_sql('average_ratings', conn, if_exists='replace', index=False)
        positive_products.to_sql('positive_reviews', conn, if_exists='replace', index=False)
        negative_products.to_sql('negative_reviews', conn, if_exists='replace', index=False)

if __name__ == '__main__':
    run_etl()
