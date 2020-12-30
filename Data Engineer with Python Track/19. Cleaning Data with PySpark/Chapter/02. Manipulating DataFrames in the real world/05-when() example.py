'''
when() example


The when() clause lets you conditionally modify a Data Frame based on its content. You'll want to modify our voter_df DataFrame to add a random number to any voting member that is defined as a "Councilmember".

The voter_df DataFrame is defined and available to you. The pyspark.sql.functions library is available as F. You can use F.rand() to generate the random value.

Instructions
100 XP

- Add a column to voter_df named random_val with the results of the F.rand() method for any voter with the title Councilmember.
- Show some of the DataFrame rows, noting whether the .when() clause worked.

'''
# Add a column to voter_df for any voter with the title **Councilmember**
voter_df = voter_df.withColumn('random_val',
                               when(voter_df.TITLE == 'Councilmember', F.rand()))

# Show some of the DataFrame rows, noting whether the when clause worked
voter_df.show()
