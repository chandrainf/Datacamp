'''
Branch troubleshooting


While working with a workflow defined by a colleague, you notice that a branching operator executes, but there's never any change in the DAG results. You realize that regardless of the state defined by the branching operator, all other tasks complete, even as some should be skipped.

Use what you've learned to determine the most likely reason that the branching operator is ineffective.

Instructions
50XP

Possible Answers

    - The branch_test method does not return the correct value.

    - The DAG does not run often enough for the callable to work properly.

    - The dependency is missing between the branch_task and even_day_task and odd_day_task.

Answer : The dependency is missing between the branch_task and even_day_task and odd_day_task.

'''
