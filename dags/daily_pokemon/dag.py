# 1) Import the DAG object
# YOUR CODE HERE

# 4) Import the PythonOperator
# YOUR CODE HERE

# 8) Import the PostgresOperator
# YOUR CODE HERE

# 2) Import datetime
# YOUR CODE HERE

# 5) Import the `task_1` and `task_2` functions from src.py
# YOUR CODE HERE

# 3) Define a dag with the following configurations:
    # The dag should be named "daily_pokemon"
    # The dag should run once per day
    # The dag should have a start date set to 07/05/2023
# YOUR CODE HERE

# 6) Initialize a PythonOperator task with the following configurations
    # The task should be named "daily_type"
    # The task should activate the `task_1` function
# YOUR CODE HERE

# 7) Initialize a PythonOperator task with the following configurations
    # The task should be named "daily_pokemon"
    # The task should activate the `task_2` function
# YOUR CODE HERE

# 9) Initialize a PostgresOperator task with the following configurations
    # The task should be named "create_table"
    # The task should run the "create_pokemon.sql" file
    # The task should use the connection id "postgres_pokemon"
    # The table's schema is "pokemon"
    # The table's name is "daily_pokemon"
# YOUR CODE HERE

# 10) Initialize a PostgresOperator task with the following configurations
    # Thnse task should be named "insert_sql"
    # The task should run the "insert_pokemon.sql" file
    # The task should use the connection id "postgres_pokemon" 
# YOUR CODE HERE

# 11) Set the task dependencies so the following is true
    # The "daily_pokemon" task depends on the "daily_type" task
    # The "insert_sql" task depends on the "create_table" task
    # The "insert_sql" task depends on the "daily_pokemon" task
# YOUR CODE HERE
