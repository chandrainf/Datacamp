'''
Comparing Pokédexes



Two Pokémon trainers, Ash and Misty, would like to compare their individual collections of Pokémon. Let's see what Pokémon they have in common and what Pokémon Ash has that Misty does not.

Both Ash and Misty's Pokédex (their collection of Pokémon) have been loaded into your session as lists called ash_pokedex and misty_pokedex. They have been printed into the console for your convenience.

Instructions
100 XP

- Convert both lists (ash_pokedex and misty_pokedex) to sets called ash_set and misty_set respectively.
- Find the Pokémon that both Ash and Misty have in common using a set method.
- Find the Pokémon that are within Ash's Pokédex but are not within Misty's Pokédex with a set method.
- Use a set method to find the Pokémon that are unique to either Ash or Misty (i.e., the Pokémon that exist in exactly one of the Pokédexes but not both).

'''

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

# Find the Pokémon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)
