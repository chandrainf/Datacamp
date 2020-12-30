'''
Practicing caching: the SQL


Previously, we examined two DataFrames: df1 and df2 (which is created from df1). We tried caching df1, but not df2. In this exercise, we'll examine the effects of caching df2, but not df1.

Once again, note the amount of time that each action takes. We'll be comparing these in the next exercise. Which tasks are sped up? Which are slowed down?

Instructions
100 XP

- Cache df2, but not df1.
- Run a first action on df1 and repeat it, then run an action df2 and repeat it. This has been done for you.

'''
# Unpersist df1 and df2 and initializes a timer
prep(df1, df2)

# Persist df2 using memory and disk storage level
df2.persist(storageLevel=pyspark.StorageLevel.MEMORY_AND_DISK)

# Run actions both dataframes

run(df1, "df1_1st")
run(df1, "df1_2nd")
run(df2, "df2_1st")
run(df2, "df2_2nd", elapsed=True)
