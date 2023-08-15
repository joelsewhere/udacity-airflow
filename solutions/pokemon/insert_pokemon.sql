INSERT INTO {{ params["schema"] }}.{{ params["table"] }} VALUES (
    '{{ ds }}'
   , '{{ ti.xcom_pull(task_ids=["daily_pokemon"], key="name")[0] }}'
   , '{{ ti.xcom_pull(task_ids=["daily_pokemon"], key="url")[0] }}'
);