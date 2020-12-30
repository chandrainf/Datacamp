'''
Recovering from deployed but broken DAGs


Sometimes your DAGs will not have been properly tested, before they are deployed, even though some checks can be easily added to a CI pipeline. In this example, someone copied a newer version of a DAG over to the Airflow server. The DAG contains a mistake though, one that could have easily been spotted had that person merely tried to execute python dags/greeting.py, as any Airflow DAG is still simply a valid Python module.

At least the Airflow user interface gives us a hint of what’s wrong:

Airflow notification of a broken DAG

It is fairly late in the process of deploying your DAGs, and it requires manual effort, but it’s better than nothing. It stresses the importance of automating checks though.

Instructions
100XP

-Resolve the error by opening greeting.py, examining the DAG configured in it, and adding the missing import statement.

'''

# Modified dags/greeting.py

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
