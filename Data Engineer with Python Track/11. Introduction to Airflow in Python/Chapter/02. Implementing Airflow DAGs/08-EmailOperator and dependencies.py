'''
EmailOperator and dependencies


Now that you've successfully defined the PythonOperators for your workflow, your manager would like to receive a copy of the parsed JSON file via email when the workflow completes. The previous tasks are still defined and the DAG process_sales_dag is configured.

Instructions
100 XP

- Import the class to send emails.
- Define the Operator and add the appropriate arguments (to, subject, files).
- Set the task order so the tasks run sequentially (Pull the file, parse the file, then email your manager).

'''
# Import the Operator
from airflow.operators.email_operator import EmailOperator

email_manager_task = EmailOperator(
    task_id='email_manager',
    to='manager@datacamp.com',
    subject='Latest sales JSON',
    html_content='Attached is the latest sales JSON file as requested.',
    files='parsedfile.json',
    dag=process_sales_dag
)

# Set the order of tasks
pull_file_task >> parse_file_task >> email_manager_task
