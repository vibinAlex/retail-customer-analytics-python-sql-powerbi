"""
connectdb.py

Handles the PostgreSQL connection and loads a cleaned pandas DataFrame
into a database table using SQLAlchemy.
"""

from sqlalchemy import create_engine
import pandas as pd


class conncectdbcls:
    """Wraps a SQLAlchemy engine and pushes a DataFrame into PostgreSQL."""

    def __init__(self, username, password, host, port, database, df: pd.DataFrame, table_name):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.df = df
        self.table_name = table_name

    def connect(self, username, password, host, port, database, df: pd.DataFrame, table_name):
        engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")
        # df.dropna()
        self.df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"Data successfully loaded in to table {table_name} in database {database}")
