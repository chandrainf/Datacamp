'''
Multiple BashOperators


Airflow DAGs can contain many operators, each performing their defined tasks.

You've successfully implemented one of your scripts as an Airflow task and have decided to continue migrating your individual scripts to a full Airflow DAG. You now want to add more components to the workflow. In addition to the cleanup.sh used in the previous exercise you have two more scripts, consolidate_data.sh and push_data.sh. These further process your data and copy to its final location.

The DAG analytics_dag is available as before, and your cleanup task is still defined. The BashOperator is already imported.

Instructions
100 XP

- Define a BashOperator called consolidate, to run consolidate_data.sh with a task_id of consolidate_task.
- Add a final BashOperator called push_data, running push_data.sh and a task_id of pushdata_task.

'''

# Define a second operator to run the `consolidate_data.sh` script
consolidate = BashOperator(
    task_id='consolidate_task',
    bash_command='consolidate_data.sh',
    dag=analytics_dag)

# Define a final operator to execute the `push_data.sh` script
push_data = BashOperator(
    task_id='pushdata_task',
    bash_command='push_data.sh',
    dag=analytics_dag)
