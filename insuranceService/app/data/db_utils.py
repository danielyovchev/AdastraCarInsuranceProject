"""Database Utils file"""
import os
import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/car_insurance')


def _get_db_engine():
    """Private Function for creating a db engine """
    engine = create_engine(DATABASE_URL)
    return engine


def fetch_table_data(table_name):
    """Function for fetching data from a given table"""
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, _get_db_engine())
    return df
