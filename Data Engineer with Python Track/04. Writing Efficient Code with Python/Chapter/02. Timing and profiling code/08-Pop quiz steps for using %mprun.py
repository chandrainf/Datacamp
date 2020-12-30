'''
Pop quiz: steps for using %mprun


Suppose you have a list of superheroes (named heroes) along with each hero's height (in centimeters) and weight (in kilograms) loaded as NumPy arrays (named hts and wts, respectively). You also have a convert_units() function saved in a file titled hero_funcs.py.

What are the necessary steps you need to take in order to profile the convert_units() function acting on your superheroes data if you'd like to see the line-by-line memory consumption of convert_units()?

Answer the question
50XP

Possible Answers

    - Use the command from hero_funcs import convert_units to load the function you'd like to profile.

    - Use %load_ext memory_profiler to load the memory_profiler within your IPython session.

    - Use %mprun -f convert_units convert_units(heroes, hts, wts) to get line-by-line memory allocations.

    - All of the above.

Answer : All of the above.

'''
