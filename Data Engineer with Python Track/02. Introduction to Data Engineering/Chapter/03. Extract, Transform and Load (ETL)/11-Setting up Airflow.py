'''
Setting up Airflow


In this exercise, you'll learn how to add a DAG to Airflow. To the right, you have a terminal at your disposal. The workspace comes with Airflow pre-configured, but it's easy to install on your own.

You'll need to move the dag.py file containing the DAG you defined in the previous exercise to, the DAGs folder. Here are the steps to find it:

The airflow home directory is defined in the AIRFLOW_HOME environment variable. Type echo $AIRFLOW_HOME to find out.
In this directory, find the airflow.cfg file. Use head to read the file, and find the value of the dags_folder.
Now you can find the folder and move the dag.py file there: mv ./dag.py <dags_folder>.

Which files does the DAGs folder have after you moved the file?

Instructions
50XP

Possible Answers

    - It has one DAG file: dag.py.
    - It has two DAG files: dag.py and dag_recommendations.py.
    - It has three DAG files: dag.py, you_wont_guess_this_dag.py, and super_secret_dag.py.

Answer : It has two DAG files: dag.py and dag_recommendations.py.

'''
