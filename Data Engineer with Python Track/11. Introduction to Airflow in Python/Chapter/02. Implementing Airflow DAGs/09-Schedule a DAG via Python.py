'''
Schedule a DAG via Python


You've learned quite a bit about creating DAGs, but now you would like to schedule a specific DAG on a specific day of the week at a certain time. You'd like the code include this information in case a colleague needs to reinstall the DAG to a different server.

The Airflow DAG object and the appropriate datetime methods have been imported for you.

Instructions
100 XP

- Set the start date of the DAG to November 1, 2019.
- Configure the retry_delay to 20 minutes. You will learn more about the timedelta object in Chapter 3. For now, you just need to know it expects an integer value.
- Use the cron syntax to configure a schedule of every Wednesday at 12:30pm.

'''
# Update the scheduling arguments as defined
default_args = {
    'owner': 'Engineering',
    'start_date': datetime(2019, 11, 1),
    'email': ['airflowresults@datacamp.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=20)
}

dag = DAG('update_dataflows', default_args=default_args,
          schedule_interval='30 12 * * 3')
