'''
Gathering Pokémon without a loop


A list containing 720 Pokémon has been loaded into your session as poke_names. Another list containing each Pokémon's corresponding generation has been loaded as poke_gens.

A for loop has been created to filter the Pokémon that belong to generation one or two, and collect the number of letters in each Pokémon's name:

    gen1_gen2_name_lengths_loop = []

    for name,gen in zip(poke_names, poke_gens):
        if gen < 3:
            name_length = len(name)
            poke_tuple = (name, name_length)
            gen1_gen2_name_lengths_loop.append(poke_tuple)


Instructions
100 XP

- Eliminate the above for loop using list comprehension and the map() function:
    - Use list comprehension to collect each Pokémon that belongs to generation 1 or generation 2. Save this as gen1_gen2_pokemon.
    - Use the map() function to collect the number of letters in each Pokémon's name within the gen1_gen2_pokemon list. Save this map object as name_lengths_map.
    - Combine gen1_gen2_pokemon and name_length_map into a list called gen1_gen2_name_lengths.

'''
# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name, gen in zip(
    poke_names, poke_gens) if gen < 3]

# Create a map object that stores the name lengths
name_lengths_map = map(len, gen1_gen2_pokemon)

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]

print(gen1_gen2_name_lengths_loop[:5])
print(gen1_gen2_name_lengths[:5])
