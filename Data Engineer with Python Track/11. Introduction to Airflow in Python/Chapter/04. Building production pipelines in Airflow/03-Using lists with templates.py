'''
Using lists with templates


Once again, you decide to make some modifications to the design of your cleandata workflow. This time, you realize that you need to run the command cleandata.sh with the date argument and the file argument as before, except now you have a list of 30 files. You do not want to create 30 tasks, so your job is to modify the code to support running the argument for 30 or more files.

The Python list of files is already created for you, simply called filelist.

Instructions
100XP

- Modify the templated command to iterate over a list of filenames.
- Pass the filelist to the templated command in the operator.

'''
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

filelist = [f'file{x}.txt' for x in range(30)]

default_args = {
    'start_date': datetime(2020, 4, 15),
}

cleandata_dag = DAG('cleandata',
                    default_args=default_args,
                    schedule_interval='@daily')

# Modify the template to handle multiple files in a
# single run.
templated_command = """
  <% for filename in params.filenames %>
  bash cleandata.sh {{ ds_nodash }} {{ filename }};
  <% endfor %>
"""

# Modify clean_task to use the templated command
clean_task = BashOperator(task_id='cleandata_task',
                          bash_command=templated_command,
                          params={'filenames': filelist},
                          dag=cleandata_dag)
