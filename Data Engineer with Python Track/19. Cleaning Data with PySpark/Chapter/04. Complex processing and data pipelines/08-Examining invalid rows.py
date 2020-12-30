'''
Examining invalid rows


You've successfully filtered out the rows using a join, but sometimes you'd like to examine the data that is invalid. This data can be stored for later processing or for troubleshooting your data sources.

You want to find the difference between two DataFrames and store the invalid rows.

The spark object is defined and pyspark.sql.functions are imported as F. The original DataFrame split_df and the joined DataFrame joined_df are available as they were in their previous states.

Instructions
100 XP

- Determine the row counts for each DataFrame.
- Create a DataFrame containing only the invalid rows.
- Validate the count of the new DataFrame is as expected.
- Determine the number of distinct folder rows removed.

'''
# Determine the row counts for each DataFrame
split_count = split_df.count()
joined_count = joined_df.count()

# Create a DataFrame containing the invalid rows
invalid_df = split_df.join(F.broadcast(joined_df), 'folder', how='left_anti')

# Validate the count of the new DataFrame is as expected
invalid_count = invalid_df.count()
print(" split_df:\t%d\n joined_df:\t%d\n invalid_df: \t%d" %
      (split_count, joined_count, invalid_count))

# Determine the number of distinct folder rows removed
invalid_folder_count = invalid_df.select('folder').distinct().count()
print("%d distinct invalid folders found" % invalid_folder_count)
