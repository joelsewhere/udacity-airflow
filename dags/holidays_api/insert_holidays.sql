INSERT INTO {{ params["table"] }} ({{ params['columns']|join(',') }}) VALUES
{% for row in ti.xcom_pull(key="country_data", task_ids=["public_holidays"])[0] %}
    (
    {% for key in row %}
         "{{ row.get(key) }}"{% if not loop.last %},{% endif %} 
    {% endfor %}
    ){% if not loop.last %},{% endif %} 
{% endfor %}
  ;