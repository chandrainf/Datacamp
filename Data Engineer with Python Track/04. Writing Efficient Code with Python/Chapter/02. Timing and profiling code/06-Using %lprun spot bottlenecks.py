'''
Using %lprun: spot bottlenecks


Profiling a function allows you to dig deeper into the function's source code and potentially spot bottlenecks. When you see certain lines of code taking up the majority of the function's runtime, it is an indication that you may want to deploy a different, more efficient technique.

Lets dig deeper into the convert_units() function.

    def convert_units(heroes, heights, weights):

        new_hts = [ht * 0.39370  for ht in heights]
        new_wts = [wt * 2.20462  for wt in weights]

        hero_data = {}

        for i,hero in enumerate(heroes):
            hero_data[hero] = (new_hts[i], new_wts[i])

        return hero_data

Load the line_profiler package into your IPython session. Then, use %lprun to profile the convert_units() function acting on your superheroes data. Remember to use the special syntax for working with %lprun (you'll have to provide a -f flag specifying the function you'd like to profile).

The convert_units() function, heroes list, hts array, and wts array have been loaded into your session. After you've finished coding, answer the following question:

What percentage of time is spent on the new_hts list comprehension line of code relative to the total amount of time spent in the convert_units() function?

Instructions
50 XP

Possible Answers

    - 0% - 10%

    - 11% - 20%

    - 21% - 50%

    - 51% - 100%

Answer : 11% - 20%

'''
