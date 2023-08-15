from requests import get

# 1) Alter the `task_1` function so the function
#    receives the task_instance context variable
#    as well as the latitude and longitude values
#    as inputs
def task_1():

    # 2) If you are passing the latitude and longitude
    #    to this function via `op_args` or `op_kwargs`
    #    ensure that the variables names are `latitude` and
    #    `longitude`
    #
    #    If you've decided to access the latitude and longitude
    #    values with the `params` context variable
    #    assign the latitude and longitude to the variable names
    #    `latitude` and `longitude`
    # YOUR CODE HERE (PARAMS ONLY)

    endpoint = f'https://api.weather.gov/points/{latitude},{longitude}'
    json = get(endpoint).json()
    hourly_forecast_endpoint = json['properties']['forecastHourly']

    # 3) Push the `hourly_forecast_endpoint` to the XCOM
    # YOUR CODE HERE

# 4) Alter the `task_2` function so the function
#    receives the task_instance context variable
#    as an input
def task_2():

    # 5) Pull the hourly_forecast_endpoint value from the XCOM
    #    Assign the value to the variable `hourly_endpoint`
    # YOUR CODE HERE

    json = get(hourly_endpoint).json()
    temperature = json['properties']['periods'][0]['temperature']

    # 6) Push the temperature value to the XCOM
    # YOUR CODE HERE
