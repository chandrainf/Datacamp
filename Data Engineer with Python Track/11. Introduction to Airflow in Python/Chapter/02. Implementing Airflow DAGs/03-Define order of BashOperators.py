'''
Define order of BashOperators


Now that you've learned about the bitshift operators, it's time to modify your workflow to include a pull step and to include the task ordering. You have three currently defined components, cleanup, consolidate, and push_data.

The DAG analytics_dag is available as before and the BashOperator is already imported.

Instructions
100 XP

- Define a BashOperator called pull_sales with a bash command of wget https://salestracking/latestinfo?json.
- Set the pull_sales operator to run before the cleanup task.
- Configure consolidate to run next, using the downstream operator.
- Set push_data to run last using either bitshift operator.

'''
pull_sales = BashOperator(
    task_id='pullsales_task',
    bash_command='wget https://salestracking/latestinfo?json',
    dag=analytics_dag
)

# Set pull_sales to run prior to cleanup
pull_sales >> cleanup

# Configure consolidate to run after cleanup
cleanup >> consolidate

# Set push_data to run last
consolidate >> push_data
