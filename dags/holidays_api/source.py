from requests import get
from airflow.providers.sqlite.hooks.sqlite import SqliteHook
import airflow.providers.sqlite.hooks.sqlite as module
from airflow.models.connection import Connection

def get_country_code(ds, ti, **kwargs):

    query = f"""
    
    SELECT * 
    FROM countries
    WHERE date = '{ds}';
    
    """


    query = """
    
    SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;

    """
    from urllib.parse import unquote
    print('module', module.__file__)
    hook = SqliteHook(sqlite_conn_id='sqlite_file')
    hook.default_conn_name='sqlite_file'
    print('1', hook.sqlite_conn_id)
    conn = hook.get_connection('sqlite_file')
    print('CONN', conn.get_uri())
    airflow_uri = unquote(conn.get_uri())
    print('UNQUOTE', airflow_uri)
    airflow_sqlite_uri = airflow_uri.replace("/?", "?")
    print('!!!', airflow_sqlite_uri)
    sqlalchemy_uri = airflow_sqlite_uri.replace("sqlite://", "sqlite:///")
    print('????', sqlalchemy_uri)
    print('hook uri', hook.get_uri())
    df = hook.get_pandas_df(query)
    print(df)
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