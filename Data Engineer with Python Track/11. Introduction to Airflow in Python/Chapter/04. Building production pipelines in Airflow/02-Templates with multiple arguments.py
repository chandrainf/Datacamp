'''
Templates with multiple arguments


You wish to build upon your previous DAG and modify the code to support two arguments - the date in YYYYMMDD format, and a file name passed to the cleandata.sh script.

Instructions
100XP

- Modify the templated command to handle a second argument called filename.
- Change the first BashOperator to pass the filename salesdata.txt to the command.
- Add a new BashOperator called clean_task2 to use a second filename supportdata.txt.
- Set clean_task2 downstream of clean_task.

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

# Modify the templated command to handle a
# second argument called filename.
templated_command = """
  bash cleandata.sh {{ ds_nodash }} {{ params.filename }}
"""

# Modify clean_task to pass the new argument
clean_task = BashOperator(task_id='cleandata_task',
                          bash_command=templated_command,
                          params={'filename': 'salesdata.txt'},
                          dag=cleandata_dag)

# Create a new BashOperator clean_task2
clean_task2 = BashOperator(task_id='cleandata_task2',
                           bash_command=templated_command,
                           params={'filename': 'supportdata.txt'},
                           dag=cleandata_dag)

# Set the operator dependencies
clean_task >> clean_task2
