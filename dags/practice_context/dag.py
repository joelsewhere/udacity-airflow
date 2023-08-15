from airflow import DAG
from datetime import datetime

# 1) Import the PythonOperator
# YOUR CODE HERE


dag = DAG(
    dag_id="practice_context",
    start_date=datetime(2023, 7, 10),
    )

# 2) Alter the `task` definition
#    so the context is made availble
#    to the code inside the function
def task():

    # 3 print the context
    # YOUR CODE HERE
    
    pass


# 4) Initialize a PythonOperator that activates the `task` function
# YOUR CODE HERE