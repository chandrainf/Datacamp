'''
Adding an ID Field


When working with data, you sometimes only want to access certain fields and perform various operations. In this case, find all the unique voter names from the DataFrame and add a unique ID number. Remember that Spark IDs are assigned based on the DataFrame partition - as such the ID values may be much greater than the actual number of rows in the DataFrame.

With Spark's lazy processing, the IDs are not actually generated until an action is performed and can be somewhat random depending on the size of the dataset.

The spark session and a Spark DataFrame df containing the DallasCouncilVotes.csv.gz file are available in your workspace. The pyspark.sql.functions library is available under the alias F.

Instructions
100 XP

- Select the unique entries from the column VOTER NAME and create a new DataFrame called voter_df.
- Count the rows in the voter_df DataFrame.
- Add a ROW_ID column using the appropriate Spark function.
- Show the rows with the 10 highest ROW_IDs.

'''
# Select all the unique council voters
voter_df = df.select(df["VOTER NAME"]).distinct()

# Count the rows in voter_df
print("\nThere are %d rows in the voter_df DataFrame.\n" % voter_df.count())

# Add a ROW_ID
voter_df = voter_df.withColumn('ROW_ID', F.monotonically_increasing_id())

# Show the rows with 10 highest IDs in the set
voter_df.orderBy(voter_df.ROW_ID.desc()).show(n=10)
