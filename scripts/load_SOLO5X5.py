import pandas as pd
import datetime
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()
db_name=os.environ.get("DB_NAME")
db_user=os.environ.get("DB_USER")
db_password=os.environ.get("DB_PASSWORD")
db_port=os.environ.get("DB_PORT")
conn_string = f'postgresql://{db_user}:{db_password}@0.0.0.0/{db_name}'
df = pd.read_csv("../processed/processed.csv")
df.to_sql('db_GM', con=conn_string, if_exists='replace', index=False)