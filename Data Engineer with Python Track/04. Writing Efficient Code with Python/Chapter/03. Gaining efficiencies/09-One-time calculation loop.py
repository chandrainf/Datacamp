'''
One-time calculation loop


A list of integers that represents each Pokémon's generation has been loaded into your session called generations. You'd like to gather the counts of each generation and determine what percentage each generation accounts for out of the total count of integers.

The below loop was written to accomplish this task:

  for gen,count in gen_counts.items():
      total_count = len(generations)
      gen_percent = round(count / total_count * 100, 2)
      print(
        'generation {}: count = {:3} percentage = {}'
        .format(gen, count, gen_percent)
      )

Let's make this loop more efficient by moving a one-time calculation outside the loop.

Instructions
100 XP

- Import Counter from the collections module.
- Use Counter() to collect the count of each generation from the generations list. Save this as gen_counts.
- Write a better for loop that places a one-time calculation outside (above) the loop. Use the exact same syntax as the original for loop (simply copy and paste the one-time calculation above the loop).

'''
# Import Counter
from collections import Counter

# Collect the count of each generation
gen_counts = Counter(generations)

# Improve for loop by moving one calculation above the loop
total_count = len(generations)

for gen, count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))
