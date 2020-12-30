'''
Creating a production pipeline #1


You've learned a lot about how Airflow works - now it's time to implement your workflow into a production pipeline consisting of many objects including sensors and operators. Your boss is interested in seeing this workflow become automated and able to provide SLA reporting as it provides some extra leverage for closing a deal the sales staff is working on. The sales prospect has indicated that once they see updates in an automated fashion, they're willing to sign-up for the indicated data service.

From what you've learned about the process, you know that there is sales data that will be uploaded to the system. Once the data is uploaded, a new file should be created to kick off the full processing, but something isn't working correctly.

Refer to the source code of the DAG to determine if anything extra needs to be added.

Instructions
100XP

- Update the DAG in pipeline.py to import the needed operators.
- Run the sense_file task from the command line and look for any errors. Use the command airflow test and the appropriate arguments to run the command. For the last argument, use a -1 instead of a specific date.
- Determine why the sense_file task does not complete and remedy this using the editor.
- Re-test the sense_file task and verify the problem is fixed.

Answer :
-run command in terminal type airflow test etl_update sense_file -1

'''
from airflow.models import DAG
from airflow.contrib.sensors.file_sensor import FileSensor

# Import the needed operators
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import date, datetime


def process_data(**context):
    file = open('/home/repl/workspace/processed_data.tmp', 'w')
    file.write(f'Data processed on {date.today()}')
    file.close()


dag = DAG(dag_id='etl_update', default_args={
          'start_date': datetime(2020, 4, 1)})

sensor = FileSensor(task_id='sense_file',
                    filepath='/home/repl/workspace/startprocess.txt',
                    poke_interval=5,
                    timeout=15,
                    dag=dag)

bash_task = BashOperator(task_id='cleanup_tempfiles',
                         bash_command='rm -f /home/repl/*.tmp',
                         dag=dag)

python_task = PythonOperator(task_id='run_processing',
                             python_callable=process_data,
                             dag=dag)

sensor >> bash_task >> python_task
