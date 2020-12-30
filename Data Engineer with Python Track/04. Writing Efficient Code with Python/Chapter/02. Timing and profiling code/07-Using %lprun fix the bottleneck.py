'''
Using %lprun: fix the bottleneck


In the previous exercise, you profiled the convert_units() function and saw that the new_hts list comprehension could be a potential bottleneck. Did you notice that the new_wts list comprehension also accounted for a similar percentage of the runtime? This is an indication that you may want to create the new_hts and new_wts objects using a different technique.

Since the height and weight of each hero is stored in a numpy array, you can use array broadcasting rather than list comprehension to convert the heights and weights. This has been implemented in the below function:

    def convert_units_broadcast(heroes, heights, weights):

        # Array broadcasting instead of list comprehension
        new_hts = heights * 0.39370
        new_wts = weights * 2.20462

        hero_data = {}

        for i,hero in enumerate(heroes):
            hero_data[hero] = (new_hts[i], new_wts[i])

        return hero_data

Load the line_profiler package into your IPython session. Then, use %lprun to profile the convert_units_broadcast() function acting on your superheroes data. The convert_units_broadcast() function, heroes list, hts array, and wts array have been loaded into your session. After you've finished coding, answer the following question:

What percentage of time is spent on the new_hts array broadcasting line of code relative to the total amount of time spent in the convert_units_broadcast() function?

Instructions
50 XP

Possible Answers

    -0% - 10%

    -11% - 20%

    -21% - 50%

    -51% - 100%

Answer : 0% - 10%

'''
