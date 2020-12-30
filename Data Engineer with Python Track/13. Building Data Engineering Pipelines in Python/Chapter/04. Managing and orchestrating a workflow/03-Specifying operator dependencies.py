'''
Specifying operator dependencies


Now that we have set up the scheduling using a cron expression, we know when the first of our tasks in a DAG should run, but we haven’t mentioned anything about how tasks are related. What we usually run is a number of tasks, and these tasks are modular pieces that fit together in order to complete a full DAG. We need to introduce some logic between our tasks, which we call dependencies, to tell Airflow when each task should start. That is done with the methods .set_upstream() and .set_downstream, which are defined on any Airflow operator.

In this exercise, we have already defined a number of operators for you. Their variable identifiers are the same as the task_ids shown in the figure below. Let’s try to recreate the graph.

Airflow DAG illustrating the sequence of tasks for preparing a pizza

Instructions
100 XP

- Set prepare_crust to precede apply_tomato_sauce using the appropriate method.
- Set apply_tomato_sauceto precede each of tasks in tasks_with_tomato_sauce_parent using the appropriate method.
- Set the tasks_with_tomato_sauce_parent list to precede bake_pizza using either the bitshift operator >> or <<.
- Set bake_pizza to succeed prepare_oven using the appropriate method.

'''
# Specify direction using verbose method
prepare_crust.set_downstream(apply_tomato_sauce)

tasks_with_tomato_sauce_parent = [
    add_cheese, add_ham, add_olives, add_mushroom]
for task in tasks_with_tomato_sauce_parent:
    # Specify direction using verbose method on relevant task
    apply_tomato_sauce.set_downstream(task)

# Specify direction using bitshift operator
tasks_with_tomato_sauce_parent >> bake_pizza

# Specify direction using verbose method
bake_pizza.set_upstream(prepare_oven)
