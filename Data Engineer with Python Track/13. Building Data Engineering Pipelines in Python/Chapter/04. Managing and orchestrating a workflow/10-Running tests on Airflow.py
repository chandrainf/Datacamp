'''
Running tests on Airflow


Not all errors are displayed in Airflow’s web interface with clear messages. An example of this is given in this exercise. Some smart people in your organization decided that all teams that want to use the Airflow server, must specify which DAGs are theirs, by specifying the owner attribute of a DAG’s default arguments. Those same smart people even wrote a test to ensure this. They keep a white-list of all teams that have permission to use the Airflow server too.

In this example, the DAG is technically correct. However, your CI/CD pipeline stops at the testing stage. Your goal is to get past this stage.

Instructions
100XP

- cd into the airflow directory.
- Run the script script/test, by simply executing that command. It is the same script the CI/CD tool is triggering. Doing so will give you a big hint about what’s wrong.
- Fix the error by modifying dags/greeting.py.
- Rerun the script script/test, to validate you are now compliant with company policy.

'''

# Modifying dags/greeting.py
"""
An Apache Airflow DAG used in course material.

"""


from datetime import datetime, timedelta
from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
default_args = {
    "owner": "squad-a",
    "depends_on_past": False,
    "start_date": datetime(2019, 7, 5),
    "email": ["foo@bar.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "cleaning",
    default_args=default_args,
    user_defined_macros={"env": Variable.get("environment")},
    schedule_interval="0 5 */2 * *"
)


def say(what):
    print(what)


with dag:
    say_hello = BashOperator(task_id="say-hello", bash_command="echo Hello,")
    say_world = BashOperator(task_id="say-world", bash_command="echo World")
    shout = PythonOperator(task_id="shout",
                           python_callable=say,
                           op_kwargs={'what': '!'})

    say_hello >> say_world >> shout
