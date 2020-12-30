'''
Creating a production pipeline #2


Continuing on your last workflow, you'd like to add some additional functionality, specifically adding some SLAs to the code and modifying the sensor components.

Refer to the source code of the DAG to determine if anything extra needs to be added. The default_args dictionary has been defined for you, though it may require further modification.

Instructions
100XP

- Add an SLA of 90 minutes to the DAG.
- Update the FileSensor object to check for files every 45 seconds.
- Modify the python_task to send Airflow variables to the callable. Note that the callable is configured to accept the variables using the provide_context argument.

'''
from airflow.models import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from dags.process import process_data
from datetime import timedelta, datetime

# Update the default arguments and apply them to the DAG
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

sensor >> bash_task >> python_task
