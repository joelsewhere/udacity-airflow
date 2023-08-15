from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator

dag = DAG(
    dag_id="practice_depedencies",
    start_date=datetime(2023, 7, 5),
    )

A = EmptyOperator(
    dag=dag,
    task_id="A"
    )

B = EmptyOperator(
    dag=dag,
    task_id='B'
    )

C = EmptyOperator(
    dag=dag,
    task_id='C'
    )


D = EmptyOperator(
    dag=dag,
    task_id='D'
    )

E = EmptyOperator(
    dag=dag,
    task_id='E'
    )

A >> B >> C >> D >> E