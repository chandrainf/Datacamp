'''
Using %timeit: specifying number of runs and loops


A list of 480 superheroes has been loaded into your session (called heroes). You'd like to analyze the runtime for converting this heroes list into a set. Instead of relying on the default settings for %timeit, you'd like to only use 5 runs and 25 loops per each run.

What is the correct syntax when using %timeit and only using 5 runs with 25 loops per each run?

Instructions
50 XP

Possible Answers

    - timeit -runs5 -loops25 set(heroes)

    - %%timeit -r5 -n25 set(heroes)

    - %timeit set(heroes), 5, 25

    - %timeit -r5 -n25 set(heroes)

Answer : %timeit -r5 -n25 set(heroes)

'''
