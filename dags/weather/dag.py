"""
INSTRUCTIONS

The comments provided in this file will guide you through the steps for creating 
a dag that collects the temperature for a given United States latitude and longitude.

PROJECT VARIABLES:
- The postgres connection id for all Postgres tasks is: "postgres_weather"
- The schema for all postgres tasks is "weather"
- The table for all postgres tasks is "temperature"

"""

# 1) Import the DAG object
# YOUR CODE HERE
# 2) Import the PostgresOperator
# YOUR CODE HERE
# 3) Import the PythonOperator
# YOUR CODE HERE
# 4) Import datetime
# YOUR CODE HERE
# 5) Import the `task_1` and `task_2` functions from src.py
# YOUR CODE HERE


LATITUDE = 41.881832
LONGITUDE = -87.623177

# 6) Initialize a dag object with the following configurations
    # The dag should be named "weather"
    # The start date should be set to 05/07/2023
    # The dag should run every hour
# YOUR CODE HERE
    
    
# 7) Initialize a PythonOperator task with the following configurations
    # The task should be named "get_endpoint"
    # The task should activate the `task_1` function
    # The latitude and longitude values defined at the top of this file
    #     should be passed to the task_1 function
    #     either via op_kwargs or via params
# YOUR CODE HERE

# 8) Initialize a PythonOperator task with the following configurations
    # The task should be named "get_temperature"
    # The task should activate the `task_2` function
# YOUR CODE HERE

# 9) Initialize a PostgresOperator with the following configurations
    # The task should be named "create_table"
    # The task should run the "create_temperature.sql" file
# YOUR CODE HERE

# 10) A PostgresOperator has been initialized below.
#     Please complete the following:
#         a. Set the connection id
#         b. Using params, replace <SCHEMA> with the schema 
#            described in the instructions at the top of this file
#         c. Using params, replace <TABLE> with the the table
#            described in the instructions at the top of this file
#         d. Using context variables, replace <END> with the end
#            value of the dag's data interval
#         e. Using params, replace <LAT> with the latitude
#            set at the top of this file
#         f. Using params, replace <LON> with the longitude
#            set at the top of this file
#         g. Using context variables, replace <TEMP> with the daily temperature
insert_temperature = PostgresOperator(
    task_id="insert_temperature",
    postgres_conn_id="postgres_weather",
    sql="""INSERT INTO {{ <SCHEMA> }}.{{ <TABLE> }} VALUES (
        '{{ <END> }}'
        , {{ <LAT> }}
        , {{ <LON> }}
        , {{ <TEMP> }}
        );""",
    )

# 11) Set the task dependencies so the following is true:
#       a. get_temperature depends on get_endpoint
#       b. insert temperature depends on get_temperature and create_table
# YOUR CODE HERE

