from transform import transform_data
from sqlalchemy import create_engine
from config import DB_NAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_USER
import pandas as pd


engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def load():
    df = transform_data()

    if df.empty:
        print("No data!")
        return
    
    # send data to database
    try:
        df.to_sql(name="crypto_data", con=engine, if_exists="append", index=False)
    except Exception as e:
        print(e)
