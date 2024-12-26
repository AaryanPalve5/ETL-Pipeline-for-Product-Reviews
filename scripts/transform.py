import pandas as pd
from textblob import TextBlob
from typing import Any

def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = ['review_id', 'product_id', 'customer_id', 'rating', 'review_date', 'review_text']
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df = df.dropna(subset=['rating'])
    df['rating'] = df['rating'].astype(int)
    df['review_date'] = pd.to_datetime(df['review_date'], errors='coerce')
    df = df.dropna(subset=['review_date'])
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=['review_text'])
    df = df.drop_duplicates(subset=['review_id'], keep='first')
    return df

def add_sentiment_column(df: pd.DataFrame) -> pd.DataFrame:
    df['sentiment'] = df['review_text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return df
