'''
Determining the order of tasks


While looking through a colleague's workflow definition, you're trying to decipher exactly in which order the defined tasks run. The code in question shows the following:

    pull_data << initialize_process
    pull_data >> clean >> run_ml_pipeline
    generate_reports << run_ml_pipeline

Instructions
100XP

- Order the tasks in the sequence defined by the bitshift code, with the first task to run on top and the last task to run on the bottom.

'''
