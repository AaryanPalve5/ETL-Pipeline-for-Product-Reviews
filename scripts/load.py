import sqlite3
import pandas as pd
from typing import Any

def load_to_db(df: pd.DataFrame, db_path: str) -> None:
    try:
        with sqlite3.connect(db_path) as conn:
            df.to_sql('product_reviews', conn, if_exists='replace', index=False)
            conn.commit()
    except sqlite3.Error as e:
        raise RuntimeError(f"Database error: {str(e)}")

def execute_query(query: str, db_path: str) -> pd.DataFrame:
    try:
        with sqlite3.connect(db_path) as conn:
            return pd.read_sql_query(query, conn)
    except (sqlite3.Error, pd.io.sql.DatabaseError) as e:
        raise RuntimeError(f"Query execution failed: {str(e)}")
