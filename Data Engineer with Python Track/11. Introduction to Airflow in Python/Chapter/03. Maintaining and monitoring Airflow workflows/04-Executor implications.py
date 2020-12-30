'''
Executor implications


You're learning quite a bit about running Airflow DAGs and are gaining some confidence at developing new workflows. That said, your manager has mentioned that on some days, the workflows are taking a lot longer to finish and asks you to investigate. She also mentions that the salesdata_ready.csv file is taking longer to generate these days and the time of day it is completed is variable.

This exercise requires information from the previous two lessons - remember the implications of the available arguments and modify the workflow accordingly. Note that for this exercise, you're expected to modify one line of code, not add any extra code.

Instructions
100XP

    - Determine the level of parallelism available on this system. You can do this by listing dags (airflow list_dags).
    - Look at the source for the DAG file and fix which entry is causing the problem.

Answer :
1. Open execute_report_dag.py
2. Modification line 15 to mode='reschedule'
3. Run in terminal command airflow list_dags

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
    dag=report_dag
)

generate_report_task = BashOperator(
    task_id='generate_report',
    bash_command='generate_report.sh',
    start_date=datetime(2020, 2, 20),
    dag=report_dag
)

precheck >> generate_report_task
