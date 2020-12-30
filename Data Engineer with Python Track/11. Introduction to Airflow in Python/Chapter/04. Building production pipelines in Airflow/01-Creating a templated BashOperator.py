'''
Creating a templated BashOperator


You've successfully created a BashOperator that cleans a given data file by executing a script called cleandata.sh. This works, but unfortunately requires the script to be run only for the current day. Some of your data sources are occasionally behind by a couple of days and need to be run manually.

You successfully modify the cleandata.sh script to take one argument - the date in YYYYMMDD format. Your testing works at the command-line, but you now need to implement this into your Airflow DAG. For now, use the term {{ ds_nodash }} in your template - you'll see exactly what this is means later on.

Instructions
100XP

- Create a templated command to execute the cleandata.sh script with the current execution date given by Airflow. Assign this command to a variable called templated_command.
- Modify the BashOperator to use the templated command.

'''
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2020, 4, 15),
}

cleandata_dag = DAG('cleandata',
                    default_args=default_args,
                    schedule_interval='@daily')

# Create a templated command to execute
# 'bash cleandata.sh datestring'
templated_command = """
bash cleandata.sh {{ ds_nodash }}
"""

# Modify clean_task to use the templated command
clean_task = BashOperator(task_id='cleandata_task',
                          bash_command='templated_command',
                          dag=cleandata_dag)
