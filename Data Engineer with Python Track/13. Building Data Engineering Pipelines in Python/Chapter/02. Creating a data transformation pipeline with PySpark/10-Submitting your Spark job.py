'''
Submitting your Spark job


With the dependencies of a job ready to be distributed across a cluster’s nodes, you can submit a job to a cluster easily. In this exercise, you'll be testing the job locally.

To run a PySpark application locally, you need to call:

    spark-submit --py-files PY_FILES MAIN_PYTHON_FILE
    
with PY_FILES being either a zipped archive, a Python egg or separate Python files that will be placed on the PYTHONPATH environment variable of your cluster's nodes. The MAIN_PYTHON_FILE should be the entry point of your application.

In this particular exercise, the path of the zipped archive is spark_pipelines/pydiaper/pydiaper.zip whereas the path to your application entry point is spark_pipelines/pydiaper/pydiaper/cleaning/clean_ratings.py.

Instructions
100XP

- Submit the Spark job to clean the user ratings.

'''
# You need to run this command in the terminal
spark-submit - -py-files spark_pipelines/pydiaper/pydiaper.zip ./spark_pipelines/pydiaper/pydiaper/cleaning/clean_ratings.py
