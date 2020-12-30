'''
Understanding parameter options


You've used a few different methods to add templates to your workflows. Considering the differences between options, why would you want to create individual tasks (ie, BashOperators) with specific parameters vs a list of files?

For example, why would you choose

    t1 = BashOperator(task_id='task1', bash_command=templated_command, params={'filename': 'file1.txt'}, dag=dag)
    t2 = BashOperator(task_id='task2', bash_command=templated_command, params={'filename': 'file2.txt'}, dag=dag)
    t3 = BashOperator(task_id='task3', bash_command=templated_command, params={'filename': 'file3.txt'}, dag=dag)
    over using a loop form such as

    t1 = BashOperator(task_id='task1', 
                    bash_command=templated_command, 
                    params={'filenames': ['file1.txt', 'file2.txt', 'file3.txt']},
                    dag=dag)
                    
Answer the question
50XP

Possible Answers

    -Using a loop form is slower.

    -Using specific tasks allows better monitoring of task state and possible parallel execution.

    -The params object can only handle lists of a few items.

Answer : Using specific tasks allows better monitoring of task state and possible parallel execution.

'''
