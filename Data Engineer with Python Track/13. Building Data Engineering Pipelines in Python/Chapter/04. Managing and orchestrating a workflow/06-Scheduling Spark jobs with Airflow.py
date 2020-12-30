'''
Scheduling Spark jobs with Airflow


Remember chapter 2, where you imported, cleaned and transformed data using Spark? You will now use Airflow to schedule this as well. You already saw at the end of chapter 2 that you could package code and use spark-submit to run a cleaning and transformation pipeline. Back then, you executed something along the lines of spark-submit --py-files some.zip some_app.py. To do this with Airflow, you will use the SparkSubmitOperator, which is a wrapper around spark-submit, having similarly named arguments.

There are many other spark-submit parameters that you could specify, however we will not dive into those details here.

Note also that you can use a context manager to create a DAG. This reduces the need to write dag=dag as an argument in each of the operators, which also reduces the likelihood of forgetting to specify this in each of them.

Instructions
100 XP

- Import the SparkSubmitOperator.
- Set the path for entry_point by joining the AIRFLOW_HOME environment variable and scripts/clean_ratings.py.
- Set the path for dependency_path by joining the AIRFLOW_HOME environment variable and dependencies/pydiaper.zip.
- Complete the clean_data task by passing a reference to the file that starts the Spark job and the additional files the job will use.

'''
# Import the operator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

# Set the path for our files.
entry_point = os.path.join(
    os.environ["AIRFLOW_HOME"], "scripts", "clean_ratings.py")
dependency_path = os.path.join(
    os.environ["AIRFLOW_HOME"], "dependencies", "pydiaper.zip")

with DAG('data_pipeline', start_date=datetime(2019, 6, 25),
         schedule_interval='@daily') as dag:
        # Define task clean, running a cleaning job.
    clean_data = SparkSubmitOperator(
        application=entry_point,
        py_files=dependency_path,
        task_id='clean_data',
        conn_id='spark_default')
