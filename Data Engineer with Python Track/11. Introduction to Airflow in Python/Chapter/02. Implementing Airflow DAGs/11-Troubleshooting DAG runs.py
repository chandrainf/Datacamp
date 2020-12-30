'''
Troubleshooting DAG runs


You've scheduled a DAG called process_sales which is set to run on the first day of the month and email your manager a copy of the report generated in the workflow. The start_date for the DAG is set to February 15, 2020. Unfortunately it's now March 2nd and your manager did not receive the report and would like to know what happened.

Use the information you've learned about Airflow scheduling to determine what the issue is.

Instructions
50XP

Possible Answers

    - The schedule_interval has not yet passed since the start_date.

    - The email_manager_task is not downstream of the other tasks.

    - The DAG run has an error.

    - The op_kwargs are incorrect for the EmailOperator.

Answer : The schedule_interval has not yet passed since the start_date.

'''
