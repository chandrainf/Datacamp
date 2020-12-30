'''
Examining DAGs with the Airflow UI


You've become familiar with the basics of an Airflow DAG and the basics of interacting with Airflow on the command-line. Your boss would like you to show others on your team how to examine any available DAGs. In this instance, she would like to know which operator is NOT in use with the DAG called update_state, as your team is trying to verify the components used in production workflows.

Remember that the Airflow UI allows various methods to view the state of DAGs. The Tree View lists the tasks and any ordering between them in a tree structure, with the ability to compress / expand the nodes. The Graph View shows any tasks and their dependencies in a graph structure, along with the ability to access further details about task runs. The Code view provides full access to the Python code that makes up the DAG.

Remember to select the operator NOT used in this DAG.

Instructions
50XP

Possible Answers

    - BashOperator

    - PythonOperator

    - JdbcOperator

    - SimpleHttpOperator

Answer : JdbcOperator

'''
