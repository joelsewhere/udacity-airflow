from requests import get
from airflow.providers.sqlite.hooks.sqlite import SqliteHook

def get_country_code(ds, ti, **kwargs):

    query = f"""
    
    SELECT * 
    FROM countries
    WHERE date = '{ds}';
    
    """

    hook = SqliteHook()
    df = hook.get_pandas_df(query)
    country = df.iloc[0]
    ti.xcom_push(key="country", value=country)



def collect_public_holidays(ti, ds, **kwargs):
    root = 'https://date.nager.at'
    endpoint = f'/api/v3/PublicHolidays/{country.date.year}/{country.country_code}'
    country = ti.xcom_pull(key='country', task_ids=['country'])[0]
    print('CODE       ', country.country_code)

    response = get(root + endpoint)
    data = response.json()
    ti.xcom_push(key='country_data', value=data)