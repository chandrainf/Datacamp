'''
Troubleshooting DAG dependencies


You've created a DAG with intended dependencies based on your workflow but for some reason Airflow won't load / execute the DAG. Try using the terminal to:

- List the DAGs.
- Decipher the error message.
- Use cat workspace/dags/codependent.py to view the Python code.
- Determine which of the following lines should be removed from the Python code. You may want to consider the last line of the file.

Instructions
50XP

Possible Answers

    - task1 >> task2

    - task2 >> task3

    - task3 >> task1

Answer : task3 >> task1

'''
