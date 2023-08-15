from airflow.providers.postgres.hooks.postgres import PostgresHook
from requests import get
from random import choice

def task_1(ds, ti):

    query = f"""

    SELECT * 
    FROM pokemon.daily_type
    WHERE date = '{ds}';

    """

    hook = PostgresHook(postgres_conn_id="postgres_pokemon")
    df = hook.get_pandas_df(query)
    
    ti.xcom_push(key="daily_type", value=df.type.iloc[0])


def task_2(ti):
    
    daily_type = ti.xcom_pull(task_ids=['daily_type'], key='daily_type')[0]
    daily_pokemon = get_random_pokemon(daily_type)
    ti.xcom_push(key="name", value=daily_pokemon["name"])
    ti.xcom_push(key="url", value=daily_pokemon["url"])
    

def get_random_pokemon(daily_type):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    headers = {'types': daily_type}
    request_limit = 3
    request_count = 0
    data = []
    while request_count < request_limit:
        
        response = get(url, headers=headers)
        json = response.json()
        data += json['results']
        if json.get("next"):
            url = json["next"]
        else:
            break

        request_count += 1
    
    return choice(data)
    
        


