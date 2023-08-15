from requests import get

def task_1(params, ti):
    latitude, longitude = params['latitude'], params['longitude']
    endpoint = f'https://api.weather.gov/points/{latitude},{longitude}'
    json = get(endpoint).json()
    hourly_forecast_endpoint = json['properties']['forecastHourly']

    ti.xcom_push(key="hourly_forecast_endpoint", value=hourly_forecast_endpoint)

def task_2(ti):
    
    hourly_endpoint = ti.xcom_pull(task_ids=['get_endpoint'], key="hourly_forecast_endpoint")[0]

    json = get(hourly_endpoint).json()
    temperature = json['properties']['periods'][0]['temperature']

    ti.xcom_push(key="temperature", value=temperature)
