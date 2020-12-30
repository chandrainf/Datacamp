'''
Holistic conversion loop


A list of all possible Pokémon types has been loaded into your session as pokemon_types. It's been printed in the console for convenience.

You'd like to gather all the possible pairs of Pokémon types. You want to store each of these pairs in an individual list with an enumerated index as the first element of each list. This allows you to see the total number of possible pairs and provides an indexed label for each pair.

The below loop was written to accomplish this task:

    enumerated_pairs = []

    for i,pair in enumerate(possible_pairs, 1):
        enumerated_pair_tuple = (i,) + pair
        enumerated_pair_list = list(enumerated_pair_tuple)
        enumerated_pairs.append(enumerated_pair_list)

Let's make this loop more efficient using a holistic conversion.

Instructions
100 XP

- combinations from the itertools module has been loaded into your session. Use it to create a list called possible_pairs that contains all possible pairs of Pokémon types (each pair has 2 Pokémon types).
- Create an empty list called enumerated_tuples above the for loop.
- Within the for loop, append each enumerated_pair_tuple to the empty list you created in the above step.
- Use a built-in function to convert each tuple in enumerated_tuples to a list.

'''
# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumerated_tuples
enumerated_tuples = []

# Add a line to append each enumerated_pair_tuple to the empty list above
for i, pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_pair_list = list(enumerated_pair_tuple)
    enumerated_tuples.append(enumerated_pair_list)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)
