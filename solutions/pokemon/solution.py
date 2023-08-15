from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from solutions.pokemon.solution_src import task_1, task_2
from datetime import datetime


dag = DAG(
    dag_id="daily_pokemon",
    schedule='@daily',
    start_date=datetime(2023, 7, 5),
    params={
        "schema": 'pokemon',
        "table": "daily_pokemon",
        }
    )
    
daily_type = PythonOperator(
    dag=dag,
    task_id="daily_type",
    python_callable=task_1,
    )

daily_pokemon = PythonOperator(
    dag=dag,
    task_id="daily_pokemon",
    python_callable=task_2,
    )

create_table = PostgresOperator(
    dag=dag,
    task_id="create_table",
    sql="create_pokemon.sql",
    postgres_conn_id="postgres_pokemon",

    )

insert_sql = PostgresOperator(
    dag=dag,
    task_id="insert_sql",
    sql="insert_pokemon.sql",
    postgres_conn_id="postgres_pokemon",
    )

daily_type >> daily_pokemon >> insert_sql
create_table >> insert_sql
