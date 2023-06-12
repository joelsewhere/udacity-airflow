from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# 1
def print_greeting(**kwargs):
    print("Hello world")

# 2
with DAG(
    dag_id="hello_world",  # 3
    start_date=datetime(2023, 4, 25),  # 4
    schedule="@daily",  # 5
    ) as dag:

    # 6
    PythonOperator( 
           task_id="print_greeting",  # 7
           python_callable=print_greeting,  # 8
           )