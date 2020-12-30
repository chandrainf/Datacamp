'''
Combining Pokémon names and types


Three lists have been loaded into your session from a dataset that contains 720 Pokémon:

    - The names list contains the names of each Pokémon.
    - The primary_types list contains the corresponding primary type of each Pokémon.
    - The secondary_types list contains the corresponding secondary type of each Pokémon (nan if the Pokémon has only one type).

We want to combine each Pokémon's name and types together so that you easily see a description of each Pokémon. Practice using zip() to accomplish this task.

Instructions 1/3
35 XP

- Combine the names list and the primary_types list into a new list object (called names_type1).

'''
# Combine names and primary_types
names_type1 = [*zip(names, primary_types)]
print(*names_type1[:5], sep='\n')


'''
Instructions 2/3
35 XP

Combine names, primary_types, and secondary_types (in that order) using zip() and unpack the zip object into a new list.

'''
# Combine all three lists together
names_types = [*zip(names, primary_types, secondary_types)]
print(*names_types[:5], sep='\n')


'''
Instructions 3/3
30 XP

Use zip() to combine the first five items from the names list and the first three items from the primary_types list.

'''
# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:5], primary_types[:3])]

print(*differing_lengths, sep='\n')
