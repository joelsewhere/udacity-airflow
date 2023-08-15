INSERT INTO holidays.{{ params["table"] }} VALUES
{% for row in ti.xcom_pull(key="country_data", task_ids=["public_holidays"])[0] %}
    (
    {% for key in row %}
    {% set val=row.get(key) %}
      {% if val %}
         '{{ val }}'
      {% else %}
         null
      {% endif %}
         {% if not loop.last %},{% endif %} 
    {% endfor %}
    ){% if not loop.last %},{% endif %} 
{% endfor %}
  ;