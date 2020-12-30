'''
Counting Pokémon from a sample


A sample of 500 Pokémon has been generated, and three lists from this sample have been loaded into your session:

    - The names list contains the names of each Pokémon in the sample.
    - The primary_types list containing the corresponding primary type of each Pokémon in the sample.
    - The generations list contains the corresponding generation of each Pokémon in the sample.

You want to quickly gather a few counts from these lists to better understand the sample that was generated. Use Counter from the collections module to explore what types of Pokémon are in your sample, what generations they come from, and how many Pokémon have a name that starts with a specific letter.

Counter has already been imported into your session for convenience.

Instructions
100 XP

- Collect the count of each primary type from the sample.
- Collect the count of each generation from the sample.
- Use list comprehension to collect the first letter of each Pokémon in the names list. Save this as starting_letters.
- Collect the count of starting letters from the starting_letters list. Save this as starting_letters_count.

'''
# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [name[:1] for name in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)
