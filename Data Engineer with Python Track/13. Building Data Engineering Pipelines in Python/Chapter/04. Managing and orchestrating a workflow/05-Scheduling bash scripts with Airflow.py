'''
Scheduling bash scripts with Airflow


Remember the first chapter, where the singer tap was packaged as tap-marketing-api and you piped it into a target CSV file? Back then you did this manually in Bash. Now that you know how, you can configure Airflow to run this automatically.

As you’ve seen already, in Airflow there are pre-defined operators, such as the BashOperator and the PythonOperator.

In this exercise, you need to instruct Airflow to run the ingestion pipeline, so you will use the BashOperator for this purpose. Define this Bash task in Airflow and assign it a clear name to easily distinguish and understand it in the user interface.

Instructions
100 XP

- Assign the task an id of ingest_data.
- Pipe the output from tap-marketing-api to target-csv, using the bash_command argument of the BashOperator. Pass the reference to the data_lake.conf as the value to target-csv’s --config flag. The command you construct in this way should be equivalent to what you’ve executed in the last exercise of chapter 1.

'''
config = os.path.join(os.environ["AIRFLOW_HOME"],
                      "scripts",
                      "configs",
                      "data_lake.conf")

ingest = BashOperator(
    # Assign a descriptive id
    task_id="ingest_data",
    # Complete the ingestion pipeline
    bash_command='tap-marketing-api | target-csv --config %s' % config,
    dag=dag)
