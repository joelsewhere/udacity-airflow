from requests import get
import pandas as pd
from datetime import datetime
from random import choice
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

def setup_db(**kwargs):
    url = 'https://pokeapi.co/api/v2/type/'
    results = get(url).json()['results']
    types = [x['name'] for x in results]
    start=datetime(2023, 7, 4)
    end=datetime(2080, 7, 4)
    dates = pd.date_range(start=start, end=end, freq="D")
    data = [dict(date=date, type=choice(types)) for date in dates]
    df = pd.DataFrame(data)
    print(df.head())
    hook = PostgresHook(postgres_conn_id="postgres_pokemon")
    engine = hook.get_sqlalchemy_engine()
    conn = engine.connect()
    print(type(conn))
    df.to_sql('daily_type', conn, schema='pokemon', index=False)
    conn.close()


with DAG(
    dag_id='setup_db',
    start_date=datetime(2023, 7, 5),
    catchup=False,
) as dag:
    
    op = PythonOperator(
        task_id="setup",
        python_callable=setup_db,
    )
