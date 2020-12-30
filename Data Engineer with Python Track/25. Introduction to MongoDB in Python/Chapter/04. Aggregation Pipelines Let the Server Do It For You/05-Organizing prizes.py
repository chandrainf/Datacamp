'''
Organizing prizes


In the slides at the beginning of this lesson, we saw a two-stage aggregation pipeline to determine the number of prizes awarded in total. How many prizes were awarded (at least partly) to organizations?

Instructions
100 XP

- Fill out pipeline to determine the number of prizes awarded (at least partly) to organizations. To do this, you'll first need to $match on the "gender" that designates organizations.
- Then, use a field path to project the number of prizes for each organization as the "$size" of the "prizes" array. Recall that to specify the value of a field "<my_field>", you use the field path "$<my_field>".
- Finally, use a single group {"_id": None} to sum over the values of all organizations' prize counts.

'''

# Count prizes awarded (at least partly) to organizations as a sum over sizes of "prizes" arrays.
pipeline = [
    {'$match': {'gender': "org"}},
    {"$project": {"n_prizes": {"$size": '$prizes'}}},
    {"$group": {"_id": None, "n_prizes_total": {"$sum": '$n_prizes'}}}
]

print(list(db.laureates.aggregate(pipeline)))
