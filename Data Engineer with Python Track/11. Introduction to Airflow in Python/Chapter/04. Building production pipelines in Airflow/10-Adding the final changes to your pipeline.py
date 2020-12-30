'''
Adding the final changes to your pipeline


To finish up your workflow, your manager asks that you add a conditional logic check to send a sales report via email, only if the day is a weekday. Otherwise, no email should be sent. In addition, the email task should be templated to include the date and a project name in the content.

The branch callable is already defined for you.

Instructions
100XP

- Import the necessary operators.
- Configure the EmailOperator to provide the specific data to the callable.
- Complete the branch callable as necessary to point to the email_report_task or no_email_task.
- Configure the branch operator to properly check for the condition.

'''
from airflow.models import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.email_operator import EmailOperator
from dags.process import process_data
from datetime import datetime, timedelta

# Update the default arguments and apply them to the DAG.

default_args = {
    'start_date': datetime(2019, 1, 1),
    'sla': timedelta(minutes=90)
}

dag = DAG(dag_id='etl_update', default_args=default_args)

sensor = FileSensor(task_id='sense_file',
                    filepath='/home/repl/workspace/startprocess.txt',
                    poke_interval=45,
                    dag=dag)

bash_task = BashOperator(task_id='cleanup_tempfiles',
                         bash_command='rm -f /home/repl/*.tmp',
                         dag=dag)

python_task = PythonOperator(task_id='run_processing',
                             python_callable=process_data,
                             provide_context=True,
                             dag=dag)

email_subject = """
  Email report for {{ params.department }} on {{ ds_nodash }}
"""

email_report_task = EmailOperator(task_id='email_report_task',
                                  to='sales@mycompany.com',
                                  subject=email_subject,
                                  html_content='',
                                  params={
                                      'department': 'Data subscription services'},
                                  dag=dag)

no_email_task = DummyOperator(task_id='no_email_task', dag=dag)


def check_weekend(**kwargs):
    dt = datetime.strptime(kwargs['execution_date'], "%Y-%m-%d")
    # If dt.weekday() is 0-4, it's Monday - Friday. If 5 or 6, it's Sat / Sun.
    if (dt.weekday() < 5):
        return 'email_report_task'
    else:
        return 'no_email_task'


branch_task = BranchPythonOperator(task_id='check_if_weekend',
                                   python_callable=check_weekend,
                                   provide_context=True,
                                   dag=dag)


sensor >> bash_task >> python_task

python_task >> branch_task >> [email_report_task, no_email_task]
