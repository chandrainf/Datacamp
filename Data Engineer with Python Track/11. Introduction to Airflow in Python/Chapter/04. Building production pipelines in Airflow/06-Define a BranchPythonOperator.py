'''
Define a BranchPythonOperator


After learning about the power of conditional logic within Airflow, you wish to test out the BranchPythonOperator. You'd like to run a different code path if the current execution date represents a new year (ie, 2020 vs 2019).

The DAG is defined for you, along with the tasks in question. Your current task is to implement the BranchPythonOperator.

Instructions
100 XP

- In the function year_check, configure the code to determine if the year of the current execution date is different than the previous execution date (ie, is the year different between the appropriate Airflow template variables.)
- Finish the BranchPythonOperator by adding the appropriate arguments.
- Set the dependencies on current_year_task and new_year_task.

'''
# Create a function to determine if years are different


def year_check(**kwargs):
    current_year = int(kwargs['ds_nodash'][0:4])
    previous_year = int(kwargs['prev_ds_nodash'][0:4])
    if current_year == previous_year:
        return 'current_year_task'
    else:
        return 'new_year_task'


# Define the BranchPythonOperator
branch_task = BranchPythonOperator(task_id='branch_task', dag=branch_dag,
                                   python_callable=year_check, provide_context=True)
# Define the dependencies
branch_dag >> current_year_task
branch_dag >> new_year_task
