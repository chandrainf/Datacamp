'''
Defining a BashOperator task


The BashOperator allows you to specify any given Shell command or script and add it to an Airflow workflow. This can be a great start to implementing Airflow in your environment.

As such, you've been running some scripts manually to clean data (using a script called cleanup.sh) prior to delivery to your colleagues in the Data Analytics group. As you get more of these tasks assigned, you've realized it's becoming difficult to keep up with running everything manually, much less dealing with errors or retries. You'd like to implement a simple script as an Airflow operator.

The Airflow DAG analytics_dag is already defined for you and has the appropriate configurations in place.

Instructions
100 XP

- Import the BashOperator object.
- Define a BashOperator called cleanup with the task_id of cleanup_task.
- Use the command cleanup.sh.
- Add the operator to the DAG.

'''

from airflow.operators.bash_operator import BashOperator

# Define the BashOperator
cleanup = BashOperator(
    task_id='cleanup_task',
    # Define the bash_command
    bash_command='cleanup.sh',
    # Add the task to the dag
    dag=analytics_dag
)
