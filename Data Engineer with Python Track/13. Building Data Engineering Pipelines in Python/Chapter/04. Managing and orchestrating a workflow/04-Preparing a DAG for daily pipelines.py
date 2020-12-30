'''
Preparing a DAG for daily pipelines


Now you know why Airflow is so powerful and how it can help you schedule and monitor workflows. An Airflow workflow is designed as a Directed Acyclic Graph (DAG). When thinking about a workflow, you should think of individual tasks that can be executed independently. This is also a very resilient design, as each task could be retried multiple times if an error occurs.

You’ve seen when jobs should be triggered, how to define operators and how to set up dependencies between them. You now know all you need to create your first Airflow workflow (the DAG). The only thing left is bringing everything together into your full data pipeline. The BashOperator, PythonOperator and SparkSubmitOperators have already been imported for you, as well as the DAG class and the datetime class.

Instructions
100 XP

- Create a DAG(),
- Use a boolean value to indicate that emails should not be sent when tasks fail.
- Specify that tasks in this DAG should start on June 25th, 2019.
- Instruct Airflow to run this DAG daily, using an @daily preset, which is another way of specifying schedules like cron, that is more easily readable, at the cost of being less well-known or clear about the exact time.

'''
# Create a DAG object
dag = DAG(
    dag_id='optimize_diaper_purchases',
    default_args={
        # Don't email on failure
        'email_on_failure': False,
        # Specify when tasks should have started earliest
        'start_date': datetime(2019, 6, 25)
    },
    # Run the DAG daily
    schedule_interval='@daily')
