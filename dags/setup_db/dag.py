from requests import get
import pandas as pd
from datetime import datetime
from random import choice
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook


def setup_db(**kwargs):
    root = 'https://date.nager.at'
    endpoint = '/api/v3/AvailableCountries'
    countries = get(root + endpoint)
    json = countries.json()
    start=datetime(2023, 7, 4)
    end=datetime(2080, 7, 4)
    dates = pd.date_range(start=start, end=end)
    data = [dict(date=date, **choice(json)) for date in dates]
    df = pd.DataFrame(data)
    print(df.head())
    hook = PostgresHook(postgres_conn_id="postgres_holidays")
    engine = hook.get_sqlalchemy_engine()
    conn = engine.connect()
    print(type(conn))
    df.to_sql('country_selection', conn, schema='holidays', index=False)
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