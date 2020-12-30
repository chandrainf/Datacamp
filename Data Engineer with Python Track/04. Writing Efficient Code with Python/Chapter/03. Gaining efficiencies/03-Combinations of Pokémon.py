'''
Combinations of Pokémon


Ash, a Pokémon trainer, encounters a group of five Pokémon. These Pokémon have been loaded into a list within your session (called pokemon) and printed into the console for your convenience.

Ash would like to try to catch some of these Pokémon, but his Pokédex can only store two Pokémon at a time. Let's use combinations from the itertools module to see what the possible pairs of Pokémon are that Ash could catch.

Instructions
100 XP

- Import combinations from itertools.
- Create a combinations object called combos_obj that contains all possible pairs of Pokémon from the pokemon list. A pair has 2 Pokémon.
- Unpack combos_obj into a list called combos_2.
- Ash upgraded his Pokédex so that it can now store four Pokémon. Use combinations to collect all possible combinations of 4 different Pokémon. Save these combinations directly into a list called combos_4 using the star character (*).

'''
# Import combinations from itertools
from itertools import combinations

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)
