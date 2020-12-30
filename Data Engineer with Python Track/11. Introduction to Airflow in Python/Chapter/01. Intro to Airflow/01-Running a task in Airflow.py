'''
Running a task in Airflow


You've just started looking at using Airflow within your company and would like to try to run a task within the Airflow platform. You remember that you can use the airflow run command to execute a specific task within a workflow. Note that an error while using airflow run will return airflow.exceptions.AirflowException: on the last line of output.

An Airflow DAG is set up for you with a dag_id of etl_pipeline. The task_id is download_file and the start_date is 2020-01-08. All other components needed are defined for you.

Which command would you enter in the console to run the desired task?

Instructions
50XP

Possible Answers :

    - airflow run dag task 2020-01-08

    - airflow run etl_pipeline task 2020-01-08

    - airflow run etl_pipeline download_file 2020-01-08

Answer : airflow run etl_pipeline download_file 2020-01-08

'''
