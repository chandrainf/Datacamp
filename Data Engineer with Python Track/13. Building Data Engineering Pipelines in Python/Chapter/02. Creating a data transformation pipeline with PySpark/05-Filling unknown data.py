'''
Filling unknown data


What if almost all fields in a row are valid, except one or two. What do you do in this case? Sometimes, these fields are not critical and can be left empty, sometimes they can be given a default value. Let’s try to pass a default value.

You’ve seen in the videos how to clean landing/prices_with_incomplete_rows.csv. Now let’s do the same for landing/ratings_with_incomplete_rows.csv, step by step.

A SparkSession named spark has already been loaded for you, as well as the DataFrame ratings.

Instructions
100 XP

Fill the incomplete rows, by supplying the default numeric value of 4 for the comfort column.

'''
print("BEFORE")
ratings.show()

print("AFTER")
# Replace nulls with arbitrary value on column subset
ratings = ratings.fillna(4, subset=["comfort"])
ratings.show()
