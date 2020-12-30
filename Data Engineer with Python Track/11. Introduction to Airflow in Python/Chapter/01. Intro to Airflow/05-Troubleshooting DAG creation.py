'''
Troubleshooting DAG creation


Now that you've successfully worked with a couple workflows, you notice that sometimes there are issues making a workflow appear within Airflow. You'd like to be able to better troubleshoot the behavior of Airflow when there may be something wrong with the code.

Two DAGs are defined for you and Airflow is setup. Note that any changes you make within the editor are automatically saved.

Instructions
100XP

- Use the airflow shell command to determine which DAG is not being recognized correctly.
- After you determine the broken DAG, open the file and fix any Python errors.
- Once modified, verify that the DAG now appears within Airflow's output.

'''
from airflow.models import DAG
default_args = {
    'owner': 'jdoe',
    'email': 'jdoe@datacamp.com'
}
dag = DAG('refresh_data', default_args=default_args)
