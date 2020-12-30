'''
Airflow DAGs


In Airflow, a pipeline is represented as a Directed Acyclic Graph or DAG. The nodes of the graph represent tasks that are executed. The directed connections between nodes represent dependencies between the tasks.

Representing a data pipeline as a DAG makes much sense, as some tasks need to finish before others can start. You could compare this to an assembly line in a car factory. The tasks build up, and each task can depend on previous tasks being finished. A fictional DAG could look something like this:

Example DAG

Assembling the frame happens first, then the body and tires and finally you paint. Let's reproduce the example above in code.

Instructions 1/2
50 XP

- First, the DAG needs to run on every hour at minute 0. Fill in the schedule_interval keyword argument using the crontab notation. For example, every hour at minute N would be N * * * *. Remember, you need to run

'''
# 1/2
# Create the DAG object
dag = DAG(dag_id="car_factory_simulation",
          default_args={"owner": "airflow",
                        "start_date": airflow.utils.dates.days_ago(2)},
          schedule_interval="0 * * * *")


'''
Instructions 2/2
50 XP

- The downstream flow should match what you can see in the image above. The first step has already been filled in for you.

'''
# Create the DAG object
dag = DAG(dag_id="car_factory_simulation",
          default_args={"owner": "airflow",
                        "start_date": airflow.utils.dates.days_ago(2)},
          schedule_interval="0 * * * *")

# Task definitions
assemble_frame = BashOperator(
    task_id="assemble_frame", bash_command='echo "Assembling frame"', dag=dag)
place_tires = BashOperator(task_id="place_tires",
                           bash_command='echo "Placing tires"', dag=dag)
assemble_body = BashOperator(
    task_id="assemble_body", bash_command='echo "Assembling body"', dag=dag)
apply_paint = BashOperator(task_id="apply_paint",
                           bash_command='echo "Applying paint"', dag=dag)

# Complete the downstream flow
assemble_frame.set_downstream(place_tires)
assemble_frame.set_downstream(assemble_body)
assemble_body.set_downstream(apply_paint)
