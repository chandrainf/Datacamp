'''
Scheduling the full data pipeline with Airflow


In the previous exercises, you’ve learned about several Airflow operators that can be used to trigger small data pipelines that work with files in the data lake. These were the data pipelines that you learned about in chapters 1 and 2! You’ve also seen how to specify the order of certain steps, using the .set_upstream() and .set_downstream() methods (or using the bitshift operators).

Now it’s time for the frosting on the cake: bring the operators from the previous exercises together and schedule them in the right order!

The operators you could need (SparkSubmitOperator, PythonOperator and BashOperator) have been imported already.

Instructions
100 XP

- Use the correct operators for the ìngest (a bash task), clean (a Spark job) and insight (another Spark job) tasks.
- Define the order in which the tasks should be run.

'''
spark_args = {"py_files": dependency_path,
              "conn_id": "spark_default"}
# Define ingest, clean and transform job.
with dag:
    ingest = BashOperator(
        task_id='Ingest_data', bash_command='tap-marketing-api | target-csv --config %s' % config)
    clean = SparkSubmitOperator(
        application=clean_path, task_id='clean_data', **spark_args)
    insight = SparkSubmitOperator(
        application=transform_path, task_id='show_report', **spark_args)

    # set triggering sequence
    ingest >> clean >> insight
