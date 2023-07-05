# Airflow Imports
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

# Job imports
from holidays_api.source import get_country_code, collect_public_holidays

# Other dependencies
from datetime import datetime


with DAG(
    dag_id="holidays_api",
    schedule="@daily",
    start_date=datetime(2023, 5, 21)
    ) as dag:
    
    country_code = PythonOperator(
        task_id='country_code',
        python_callable=get_country_code,
        )

    public_holidays = PythonOperator(
        task_id='public_holidays',
        python_callable=collect_public_holidays,
        )

    create_table = PostgresOperator(
        task_id="create_table",
        postgres_conn_id='postgres_holidays',
        sql="create_holidays.sql",
        params={
            "table": "public_holidays"
            },
        )

    insert_data = PostgresOperator(
        task_id='insert_data',
        postgres_conn_id='postgres_holidays',
        sql='insert_holidays.sql',
        params={
            "table": 'public_holidays',
            "columns": [
                "date",
                "localName",
                "name",
                "countryCode",
                "fixed",
                "global",
                "countries",
                "launchYear",
                "types",  
                ]
            },
        )

country_code >> public_holidays >> insert_data
create_table >> insert_data
