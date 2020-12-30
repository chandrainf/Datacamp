'''
IDs with different partitions


You've just completed adding an ID field to a DataFrame. Now, take a look at what happens when you do the same thing on DataFrames containing a different number of partitions.

To check the number of partitions, use the method .rdd.getNumPartitions() on a DataFrame.

The spark session and two DataFrames, voter_df and voter_df_single, are available in your workspace. The instructions will help you discover the difference between the DataFrames. The pyspark.sql.functions library is available under the alias F.

Instructions
100 XP

- Print the number of partitions on each DataFrame.
- Add a ROW_ID field to each DataFrame.
- Show the top 10 IDs in each DataFrame

'''
# Print the number of partitions in each DataFrame
print("\nThere are %d partitions in the voter_df DataFrame.\n" %
      voter_df.rdd.getNumPartitions())
print("\nThere are %d partitions in the voter_df_single DataFrame.\n" %
      voter_df_single.rdd.getNumPartitions())

# Add a ROW_ID field to each DataFrame
voter_df = voter_df.withColumn('ROW_ID', F.monotonically_increasing_id())
voter_df_single = voter_df_single.withColumn(
    'ROW_ID', F.monotonically_increasing_id())

# Show the top 10 IDs in each DataFrame
voter_df.orderBy(voter_df.ROW_ID.desc()).show(n=10)
voter_df_single.orderBy(voter_df_single.ROW_ID.desc()).show(10)
