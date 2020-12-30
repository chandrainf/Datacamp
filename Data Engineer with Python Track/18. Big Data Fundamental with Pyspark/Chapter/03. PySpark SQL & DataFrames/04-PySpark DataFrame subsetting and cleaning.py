'''
PySpark DataFrame subsetting and cleaning


After data inspection, it is often necessary to clean the data which mainly involves subsetting, renaming the columns, removing duplicated rows etc., PySpark DataFrame API provides several operators to do this. In this exercise, your job is to subset 'name', 'sex' and 'date of birth' columns from people_df DataFrame, remove any duplicate rows from that dataset and count the number of rows before and after duplicates removal step.

Remember, you already have SparkSession spark and people_df DataFrames available in your workspace.

Instructions
100 XP

- Select 'name', 'sex' and 'date of birth' columns from people_df and create people_df_sub DataFrame.
- Print the first 10 observations in the people_df DataFrame.
- Remove duplicate entries from people_df_sub DataFrame and create people_df_sub_nodup DataFrame.
- How many rows are there before and after duplicates are removed?

'''
# Select name, sex and date of birth columns
people_df_sub = people_df.select('name', 'sex', 'date of birth')

# Print the first 10 observations from people_df_sub
people_df_sub.show(10)

# Remove duplicate entries from people_df_sub
people_df_sub_nodup = people_df_sub.dropDuplicates()

# Count the number of rows
print("There were {} rows before removing duplicates, and {} rows after removing duplicates".format(
    people_df_sub.count(), people_df_sub_nodup.count()))
