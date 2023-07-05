from requests import get
import pandas as pd
from datetime import datetime
from random import choice
from airflow.providers.postgres.hooks.postgres import PostgresHook


def get_country_code(ds, ti, **kwargs):

    query = f"""
    
    SELECT * 
    FROM holidays.country_selection
    WHERE date = '{ds}';
    
    """

    hook = PostgresHook(postgres_conn_id='postgres_holidays')
    df = hook.get_pandas_df(query).astype(str)
    print(df.iloc[0])
    country = df.countryCode[0]
    ti.xcom_push(key="country_code", value=country)



def collect_public_holidays(ti, data_interval_start, **kwargs):
    root = 'https://date.nager.at'
    country_code = ti.xcom_pull(key='country_code', task_ids=['country_code'])[0]
    endpoint = f'/api/v3/PublicHolidays/{data_interval_start.year}/{country_code}'
    print('CODE       ', country_code)

    response = get(root + endpoint)
    data = response.json()
    for entry in data:
        for key in entry:
            if isinstance(entry[key], str) or isinstance(entry[key], list):
                entry[key] = str(entry[key]).replace("'", "''")


    ti.xcom_push(key='country_data', value=data)