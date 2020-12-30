'''
Adding status emails


You've worked through most of the Airflow configuration for setting up your workflows, but you realize you're not getting any notifications when DAG runs complete or fail. You'd like to setup email alerting for the success and failure cases, but you want to send it to two addresses.

Instructions
100XP

-Edit the execute_report_dag.py workflow.
-Add the emails airflowalerts@datacamp.com and airflowadmin@datacamp.com to the appropriate key in default_args.
-Set the failure email option to True.
-Configure the success email to send you messages as well.

Answer :
1. Open execute_report_dag.py
2. Modification line 7 to 9
3. Run file

'''
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from datetime import datetime

default_args = {
    'email': ['airflowalerts@datacamp.com', 'airflowadmin@datacamp.com'],
    'email_on_failure': True,
    'email_on_success': True
}
report_dag = DAG(
    dag_id='execute_report',
    schedule_interval="0 0 * * *",
    default_args=default_args
)

precheck = FileSensor(
    task_id='check_for_datafile',
    filepath='salesdata_ready.csv',
    start_date=datetime(2020, 2, 20),
    mode='reschedule',
    dag=report_dag)

generate_report_task = BashOperator(
    task_id='generate_report',
    bash_command='generate_report.sh',
    start_date=datetime(2020, 2, 20),
    dag=report_dag
)

precheck >> generate_report_task
