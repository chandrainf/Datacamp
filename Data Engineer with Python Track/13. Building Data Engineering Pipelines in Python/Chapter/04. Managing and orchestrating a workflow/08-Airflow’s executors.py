'''
Airflow’s executors


Apache Airflow’s “SequentialExecutor” is low maintenance, but its biggest drawback is a lack of parallelization (hence the name). All other executors provide some way to parallelize tasks if their dependencies are met.

In a production environment, you’re not likely to encounter the “SequentialExecutor”. Which executor is configured in the /home/repl/workspace/airflow/airflow.cfg configuration file?

Instructions
50XP

Possible Answers

    - SequentialExecutor

    - LocalExecutor

    - CeleryExecutor

    - DaskExecutor

    - KubernetesExecutor

Answer : CeleryExecutor

'''
