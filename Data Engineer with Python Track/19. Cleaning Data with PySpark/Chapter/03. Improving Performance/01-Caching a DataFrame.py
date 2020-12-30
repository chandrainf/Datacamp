'''
Caching a DataFrame


You've been assigned a task that requires running several analysis operations on a DataFrame. You've learned that caching can improve performance when reusing DataFrames and would like to implement it.

You'll be working with a new dataset consisting of airline departure information. It may have repetitive data and will need to be de-duplicated.

The DataFrame departures_df is defined, but no actions have been performed.

Instructions
100 XP

- Cache the unique rows in the departures_df DataFrame.
- Perform a count query on departures_df, noting how long the operation takes.
- Count the rows again, noting the variance in time of a cached DataFrame.

'''
start_time = time.time()

# Add caching to the unique rows in departures_df
departures_df = departures_df.distinct().cache()

# Count the unique rows in departures_df, noting how long the operation takes
print("Counting %d rows took %f seconds" %
      (departures_df.count(), time.time() - start_time))

# Count the rows again, noting the variance in time of a cached DataFrame
start_time = time.time()
print("Counting %d rows again took %f seconds" %
      (departures_df.count(), time.time() - start_time))
