'''
Bringing it all together: Star Wars profiling


A list of 480 superheroes has been loaded into your session (called heroes) as well as a list of each hero's corresponding publisher (called publishers).

You'd like to filter the heroes list based on a hero's specific publisher, but are unsure which of the below functions is more efficient.

    def get_publisher_heroes(heroes, publishers, desired_publisher):

        desired_heroes = []

        for i,pub in enumerate(publishers):
            if pub == desired_publisher:
                desired_heroes.append(heroes[i])

        return desired_heroes

    def get_publisher_heroes_np(heroes, publishers, desired_publisher):

        heroes_np = np.array(heroes)
        pubs_np = np.array(publishers)

        desired_heroes = heroes_np[pubs_np == desired_publisher]

        return desired_heroes

Instructions 1/4
25 XP

- Use the get_publisher_heroes() function and the get_publisher_heroes_np() function to collect heroes from the Star Wars universe. The desired_publisher for Star Wars is 'George Lucas'.

'''
# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(
    heroes, publishers, 'George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))


'''
Instructions 2/4
25 XP

Question

Within your IPython console, load the line_profiler and use %lprun to profile the two functions for line-by-line runtime. When using %lprun, use each function to gather the Star Wars heroes as you did in the previous step. After you've finished profiling, answer the following question:

Which function has the fastest runtime?

Possible Answers

    - get_publisher_heroes() is faster.

    - get_publisher_heroes_np() is faster.

    - Both functions have the same runtime.

Answer : get_publisher_heroes_np() is faster.

'''


'''
Instructions 3/4
25 XP

Question

Within your IPython console, load the memory_profiler and use %mprun to profile the two functions for line-by-line memory consumption.
The get_publisher_heroes() function and get_publisher_heroes_np() function have been saved within a file titled hero_funcs.py (i.e., you can import both functions from hero_funcs). When using %mprun, use each function to gather the Star Wars heroes as you did in the previous step. After you've finished profiling, answer the following question:

Which function uses the least amount of memory?

Possible Answers

    - get_publisher_heroes() consumes less memory.

    - get_publisher_heroes_np() consumes less memory.

    - Both functions have the same memory consumption.

Answer : Both functions have the same memory consumption.

'''


'''
Instructions 4/4
25 XP

Question

Based on your runtime profiling and memory allocation profiling, which function would you choose to gather Star Wars heroes?

Possible Answers

    - I would use get_publisher_heroes().

    - I would use get_publisher_heroes_np().

    - I could use either function since their runtimes, and memory usage were identical.

Answer : I would use get_publisher_heroes_np().

'''
