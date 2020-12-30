'''
Sending templated emails


While reading through the Airflow documentation, you realize that various operations can use templated fields to provide added flexibility. You come across the docs for the EmailOperator and see that the content can be set to a template. You want to make use of this functionality to provide more detailed information regarding the output of a DAG run.

Instructions
100XP

- Create a Python string that represents the email content you wish to send. Use the substitutions for the current date string (with dashes) and a variable called username.
- Create the EmailOperator task using the template string for the html_content.
- Set the subject field to a macro call using macros.uuid.uuid4(). This simply provides a string of a universally unique identifier as the subject field.
- Assign the params dictionary as appropriate with the username of testemailuser.

'''
from airflow.models import DAG
from airflow.operators.email_operator import EmailOperator
from datetime import datetime

# Create the string representing the html email content
html_email_str = """
Date: {{ ds }}
Username: {{ params.username }}
"""

email_dag = DAG('template_email_test',
                default_args={'start_date': datetime(2020, 4, 15)},
                schedule_interval='@weekly')

email_task = EmailOperator(task_id='email_task',
                           to='testuser@datacamp.com',
                           subject="{{ macros.uuid.uuid4() }}",
                           html_content=html_email_str,
                           params={'username': 'testemailuser'},
                           dag=email_dag)
