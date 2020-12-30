'''
More PythonOperators


To continue implementing your workflow, you need to add another step to parse and save the changes of the downloaded file. The DAG process_sales_dag is defined and has the pull_file task already added. In this case, the Python function is already defined for you, parse_file(inputfile, outputfile).

Note that often when implementing Airflow tasks, you won't necessarily understand the individual steps given to you. As long as you understand how to wrap the steps within Airflow's structure, you'll be able to implement a desired workflow.

Instructions
100 XP

- Define the Python task to the variable parse_file_task with the id parse_file.
- Add the parse_file(inputfile, outputfile) to the Operator.
- Define the arguments to pass to the callable.
- Add the task to the DAG.

'''
# Add another Python task
parse_file_task = PythonOperator(
    task_id='parse_file',
    # Set the function to call
    python_callable=parse_file,
    # Add the arguments
    op_kwargs={'inputfile': 'latestsales.json',
               'outputfile': 'parsedfile.json'},
    # Add the DAG
    dag=process_sales_dag
)
