'''
Missing DAG


Your manager calls you before you're about to leave for the evening and wants to know why a new DAG workflow she's created isn't showing up in the system. She needs this DAG called execute_report to appear in the system so she can properly schedule it for some tests before she leaves on a trip.

Airflow is configured using the ~/airflow/airflow.cfg file.

Instructions
100XP

- Examine the DAG for any errors and fix those.
- Determine if the DAG has loaded after fixing the errors.
- If not, determine why the DAG has not loaded and fix the final issue.

Answer :
1. Open execute_report_dag.py
2. Modification line 2 and remove #
3. Run in terminal command airflow list_drags

'''
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from datetime import datetime

report_dag = DAG(
    dag_id='execute_report',
    schedule_interval="0 0 * * *"
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


# sample_dag.py


sample_dag = DAG(
    dag_id='sample_dag',
    schedule_interval="0 0 * * *"
)

sample_task = BashOperator(
    task_id='sample',
    bash_command='generate_sample.sh',
    start_date=datetime(2020, 2, 20),
    dag=sample_dag
)
