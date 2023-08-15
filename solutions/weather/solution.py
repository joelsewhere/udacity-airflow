from airflow import DAG 
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from weather.src import task_1, task_2


LATITUDE = 41.881832
LONGITUDE = -87.623177

dag = DAG(
    dag_id="weather",
    start_date=datetime(2023, 7, 5),
    schedule="@hourly",
    params={
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "schema": "weather",
        "table": "temperature"
        }
    )
    
    
get_endpoint = PythonOperator(
    dag=dag,
    task_id="get_endpoint",
    python_callable=task_1,
    )

get_temperature = PythonOperator(
    dag=dag,
    task_id="get_temperature",
    python_callable=task_2,
    )

create_table = PostgresOperator(
    dag=dag,
    postgres_conn_id="postgres_weather",
    task_id="create_table",
    sql="create_temperatures.sql",
    )

insert_temperature = PostgresOperator(
    dag=dag,
    task_id="insert_temperature",
    postgres_conn_id="postgres_weather",
    sql="""INSERT INTO {{ params["schema"] }}.{{ params["table"] }} VALUES (
        '{{ data_interval_end }}'
        , {{ params["latitude"] }}
        , {{ params["longitude"] }}
        , {{ ti.xcom_pull(task_ids=['get_temperature'], key='temperature')[0] }}
        );""",
    )

get_endpoint >> get_temperature >> insert_temperature
create_table >> insert_temperature
