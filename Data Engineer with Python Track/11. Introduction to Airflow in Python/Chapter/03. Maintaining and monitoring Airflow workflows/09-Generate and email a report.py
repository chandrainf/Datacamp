'''
Generate and email a report


Airflow provides the ability to automate almost any style of workflow. You would like to receive a report from Airflow when tasks complete without requiring constant monitoring of the UI or log files. You decide to use the email functionality within Airflow to provide this message.

All the typical Airflow components have been imported for you, and a DAG is already defined as dag.

Instructions
100 XP

- Define the proper operator for the email_report task.
- Fill the missing details for the Operator. Use the file named monthly_report.pdf.
- Set the email_report task to occur after the generate_report task.

'''
# Define the email task
email_report = EmailOperator(
    task_id='email_report',
    to='airflow@datacamp.com',
    subject='Airflow Monthly Report',
    html_content="""Attached is your monthly workflow report - please refer to it for more detail""",
    files=['monthly_report.pdf'],
    dag=report_dag
)

# Set the email task to run after the report is generated
email_report << generate_report
