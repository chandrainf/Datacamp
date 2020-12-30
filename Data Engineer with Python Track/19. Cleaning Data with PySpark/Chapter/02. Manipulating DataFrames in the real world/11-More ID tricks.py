'''
More ID tricks


Once you define a Spark process, you'll likely want to use it many times. Depending on your needs, you may want to start your IDs at a certain value so there isn't overlap with previous runs of the Spark task. This behavior is similar to how IDs would behave in a relational database. You have been given the task to make sure that the IDs output from a monthly Spark task start at the highest value from the previous month.

The spark session and two DataFrames, voter_df_march and voter_df_april, are available in your workspace. The pyspark.sql.functions library is available under the alias F.

Instructions
100 XP

- Determine the highest ROW_ID in voter_df_march and save it in the variable previous_max_ID. The statement .rdd.max()[0] will get the maximum ID.
- Add a ROW_ID column to voter_df_april starting at the value of previous_max_ID.
- Show the ROW_ID's from both Data Frames and compare.

'''
# Determine the highest ROW_ID and save it in previous_max_ID
previous_max_ID = voter_df_march.select('ROW_ID').rdd.max()[0]

# Add a ROW_ID column to voter_df_april starting at the desired value
voter_df_april = voter_df_april.withColumn(
    'ROW_ID', F.monotonically_increasing_id() + previous_max_ID)

# Show the ROW_ID from both DataFrames and compare
voter_df_march.select('ROW_ID').show()
voter_df_april.select('ROW_ID').show()
