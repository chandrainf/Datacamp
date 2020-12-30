'''
Applying a UDF to vector data


A dataframe is available called df having a column output of type vector. Its first five rows are shown in the console.

A UDF get_first_udf is available that selects the first element of a vector column.

Instructions
100 XP

- Create a new dataframe called df_new by adding a new column to df. Call the new column label .
-Show the first five rows of df_new.

'''
# Add label by applying the get_first_udf to output column
df_new = df.withColumn('label', get_first_udf('output'))

# Show the first five rows
df_new.show(5)
