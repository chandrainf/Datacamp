'''
Setting up daily tasks


An Airflow instance deployed to manage enterprise-wide workflows will typically contain multiple DAGs, which all perform different tasks and are scheduled differently. Some tasks need to be scheduled every hour, some every day, some once a week and some only on specific dates.

Given the following Airflow overview of known DAGs, can you find out which two DAGs run exactly once every day?

Airflow’s main dashboard

Answer the question
50XP

Possible Answers

    - imports.company and imports.country

    - imports.company and imports.users

    - warehouse.active_users and imports_users

    - warehouse.active_users and warehouse.company_metrics

Answer : imports.company and imports.users

'''
