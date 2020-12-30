'''
Defining a task SLA


After completing the SLA on the entire workflow, you realize you really only need the SLA timing on a specific task instead of the full workflow.

The appropriate Airflow libraries are imported for you.

Instructions
100 XP

- Import the timedelta object.
- Add a 3 hour SLA to the task object

'''
# Import the timedelta object
from datetime import timedelta

test_dag = DAG('test_workflow', start_date=datetime(
    2020, 2, 20), schedule_interval='@None')

# Create the task with the SLA
task1 = BashOperator(task_id='first_task',
                     sla=timedelta(hours=3),
                     bash_command='initialize_data.sh',
                     dag=test_dag)
