import os
import pandas as pd
from extract import extract_csv, extract_json, extract_txt
from transform import normalize_data, clean_data, add_sentiment_column
from load import load_to_db, execute_query

source_a_file = os.path.join('data', 'source_a.csv')
source_b_file = os.path.join('data', 'source_b.json')
source_c_file = os.path.join('data', 'source_c.txt')
db_path = 'product_reviews.db'

def run_etl():
     
    print("Extracting data from sources...")
    df_a = extract_csv(source_a_file)
    df_b = extract_json(source_b_file)
    df_c = extract_txt(source_c_file)

    
    df = pd.concat([df_a, df_b, df_c], ignore_index=True)
    df = normalize_data(df)

    
    df = clean_data(df)

     
    df = add_sentiment_column(df)
 
    print("Loading data into the database...")
    load_to_db(df, db_path)
    
    
    print("Executing analysis queries...")

    avg_ratings_query = "SELECT product_id, AVG(rating) AS average_rating FROM product_reviews GROUP BY product_id"
    top_pos_query = """
    SELECT product_id, AVG(sentiment) AS avg_sentiment
    FROM product_reviews
    GROUP BY product_id
    ORDER BY avg_sentiment DESC
    LIMIT 3
    """
    top_neg_query = """
    SELECT product_id, AVG(sentiment) AS avg_sentiment
    FROM product_reviews
    GROUP BY product_id
    ORDER BY avg_sentiment ASC
    LIMIT 3
    """
    
    avg_ratings = execute_query(avg_ratings_query, db_path)
    top_pos = execute_query(top_pos_query, db_path)
    top_neg = execute_query(top_neg_query, db_path)
    
   
   
    print("\nAverage Product Ratings:")
    print(avg_ratings)
    print("\nTop 3 Most Positively Reviewed Products:")
    print(top_pos)
    print("\nTop 3 Most Negatively Reviewed Products:")
    print(top_neg)

if __name__ == '__main__':
    run_etl()
