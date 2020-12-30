'''
Practicing caching: part 1


In the next few exercises, you'll experiment with different ways of caching two DataFrames.

A dataframe df1 is loaded from a csv file. Several processing steps are performed on it. As df1 is to be used more than once, it is a candidate for caching.

A second dataframe df2 is created by performing additional compute-intensive steps on df1. It is also a candidate for caching.

Because df2 depends on df1 the question arises: is it better to cache df1, or to cache df2?

In this exercise, we'll try caching df1. Note the amount of time that each action takes. We'll be comparing these in the next exercise.

Instructions
100 XP

- Cache df1 only.
- Run a first action on df1 and repeat it, then run an action df2 and repeat it. This has been done for you.
- Confirm whether or not df1 is cached.

'''
# Unpersists df1 and df2 and initializes a timer
prep(df1, df2)

# Cache df1
df1.cache()

# Run actions on both dataframes
run(df1, "df1_1st")
run(df1, "df1_2nd")
run(df2, "df2_1st")
run(df2, "df2_2nd", elapsed=True)

# Prove df1 is cached
print(df1.is_cached)
