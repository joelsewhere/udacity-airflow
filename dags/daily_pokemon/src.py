# 2) Import the PostgresHook
# YOUR CODE HERE

# 1) Alter the function below so the `ds` and `ti`
#    context variables are received as parameters
def task_1():

    query = f"""

    SELECT * 
    FROM pokemon.daily_type
    WHERE date = '{ds}';

    """

    
    # 3) Initialize a PostgresHook using the "postgres_pokemon" connection id
    # YOUR CODE HERE
    # 4) Use the `get_pandas_df` method to run the sql query defined above
    # YOUR CODE HERE

    # 5) Push the value stored in the `type` column to the xcom
    # YOUR CODE HERE


# 6) Alter the function below so the `ti` 
#    context variable is received a parameter
def task_2():
    # 7) Pull the daily_type value from the xcom
    # YOUR CODE HERE

    # 8) Pass the daily_type into the `get_random_pokemon` function
    #    defined at the bottom of this file
    # YOUR CODE HERE

    # 9) Push the random pokemon's "name" and "url" to the xcom
    # YOUR CODE HERE
    pass
    

def get_random_pokemon(daily_type):
    from requests import get
    from random import choice
    if not daily_type:
        daily_type = 'fire'
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
    
        


