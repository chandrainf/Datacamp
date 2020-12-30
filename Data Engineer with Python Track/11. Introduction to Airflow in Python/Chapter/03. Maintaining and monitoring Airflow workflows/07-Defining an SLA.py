'''
Defining an SLA


You've successfully implemented several Airflow workflows into production, but you don't currently have any method of determining if a workflow takes too long to run. After consulting with your manager and your team, you decide to implement an SLA at the DAG level on a test workflow.

All appropriate Airflow libraries have been imported for you.

Instructions
100 XP

- Import the timedelta object.
- Define an SLA of 30 minutes.
- Add the SLA to the DAG.

'''
from datetime import timedelta

# Create the dictionary entry
default_args = {
    'start_date': datetime(2020, 2, 20),
    'sla': timedelta(minutes=30)
}

# Add to the DAG
test_dag = DAG('test_workflow', default_args=default_args,
               schedule_interval='@None')
