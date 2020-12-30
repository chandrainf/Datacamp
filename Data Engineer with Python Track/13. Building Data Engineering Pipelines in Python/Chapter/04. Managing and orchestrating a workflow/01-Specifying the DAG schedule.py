'''
Specifying the DAG schedule


While cron is old, its succinct syntax is used in many programs, even in Airflow! It shows its head when we instantiate a DAG and tell the Airflow scheduler when a certain time-based task needs to be run. In an Airflow DAG, you can do this by passing a cron expression to the schedule_interval parameter.

In this example exercise, you will create a DAG that should be triggered every Monday, at 7 o’clock in the morning.

Instructions
100 XP

-Complete the cron expression by using the schedule_interval to represent every Monday, at 7 o’clock in the morning.

'''
from datetime import datetime
from airflow import DAG

reporting_dag = DAG(
    dag_id="publish_EMEA_sales_report",
    # Insert the cron expression
    schedule_interval="0 7 * * 1",
    start_date=datetime(2019, 11, 24),
    default_args={"owner": "sales"}
)
