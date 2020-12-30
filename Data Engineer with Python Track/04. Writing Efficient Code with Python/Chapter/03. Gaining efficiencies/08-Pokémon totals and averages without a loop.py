'''
Pokémon totals and averages without a loop


A list of 720 Pokémon has been loaded into your session called names. Each Pokémon's corresponding statistics has been loaded as a NumPy array called stats. Each row of stats corresponds to a Pokémon in names and each column represents an individual Pokémon stat (HP, Attack, Defense, Special Attack, Special Defense, and Speed respectively.)

You want to gather each Pokémon's total stat value (i.e., the sum of each row in stats) and each Pokémon's average stat value (i.e., the mean of each row in stats) so that you find the strongest Pokémon.

The below for loop was written to collect these values:

    poke_list = []

    for pokemon,row in zip(names, stats):
        total_stats = np.sum(row)
        avg_stats = np.mean(row)
        poke_list.append((pokemon, total_stats, avg_stats))


Instructions
100 XP

- Replace the above for loop using NumPy:
    - Create a total stats array (total_stats_np) using the .sum() method and specifying the correct axis.
    - Create an average stats array (avg_stats_np) using the .mean() method and specifying the correct axis.
    - Create a final output list (poke_list_np) by combining the names list, the total_stats_np array, and the avg_stats_np array.

'''
# Create a total stats array
total_stats_np = stats.sum(axis=1)

# Create an average stats array
avg_stats_np = stats.mean(axis=1)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]

print(poke_list_np == poke_list, '\n')
print(poke_list_np[:3])
print(poke_list[:3], '\n')
top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))
