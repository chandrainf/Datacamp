'''
Filtering column content with Python


You've looked at using various operations on DataFrame columns - now you can modify a real dataset. The DataFrame voter_df contains information regarding the voters on the Dallas City Council from the past few years. This truncated DataFrame contains the date of the vote being cast and the name and position of the voter. Your manager has asked you to clean this data so it can later be integrated into some desired reports. The primary task is to remove any null entries or odd characters and return a specific set of voters where you can validate their information.

This is often one of the first steps in data cleaning - removing anything that is obviously outside the format. For this dataset, make sure to look at the original data and see what looks out of place for the VOTER_NAME column.

The pyspark.sql.functions library is already imported under the alias F.

Instructions
100 XP

- Show the distinct VOTER_NAME entries.
- Filter voter_df where the VOTER_NAME is 1-20 characters in length.
- Filter out voter_df where the VOTER_NAME contains an _.
- Show the distinct VOTER_NAME entries again.

'''

# Show the distinct VOTER_NAME entries
voter_df.select('VOTER_NAME').distinct().show(40, truncate=False)

# Filter voter_df where the VOTER_NAME is 1-20 characters in length
voter_df = voter_df.filter(
    'length(VOTER_NAME) > 0 and length(VOTER_NAME) < 20')

# Filter out voter_df where the VOTER_NAME contains an underscore
voter_df = voter_df.filter(~ F.col('VOTER_NAME').contains('_'))

# Show the distinct VOTER_NAME entries again
voter_df.select('VOTER_NAME').distinct().show(40, truncate=False)
