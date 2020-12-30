'''
Removing invalid rows


Now that you've successfully removed the commented rows, you have received some information about the general format of the data. There should be at minimum 5 tab separated columns in the DataFrame. Remember that your original DataFrame only has a single column, so you'll need to split the data on the tab (\t) characters.

The DataFrame annotations_df is already available, with the commented rows removed. The spark.sql.functions library is available under the alias F. The initial number of rows available in the DataFrame is stored in the variable initial_count.

Instructions
100 XP

- Create a new variable tmp_fields using the annotations_df DataFrame column '_c0' splitting it on the tab character.
- Create a new column in annotations_df named 'colcount' representing the number of fields defined in the previous step.
- Filter out any rows from annotations_df containing fewer than 5 fields.
- Count the number of rows in the DataFrame and compare to the initial_count.

'''
# Split _c0 on the tab character and store the list in a variable
tmp_fields = F.split(annotations_df['_c0'], '\t')

# Create the colcount column on the DataFrame
annotations_df = annotations_df.withColumn('colcount', F.size(tmp_fields))

# Remove any rows containing fewer than 5 fields
annotations_df_filtered = annotations_df.filter(
    ~ (annotations_df['colcount'] > 4))

# Count the number of rows
final_count = annotations_df_filtered.count()
print("Initial count: %d\nFinal count: %d" % (initial_count, final_count))
