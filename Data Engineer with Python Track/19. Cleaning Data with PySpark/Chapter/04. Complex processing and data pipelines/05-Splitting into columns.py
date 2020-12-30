'''
Splitting into columns


You've cleaned up your data considerably by removing the invalid rows from the DataFrame. Now you want to perform some further transformations by generating specific meaningful columns based on the DataFrame content.

You have the spark context and the latest version of the annotations_df DataFrame. pyspark.sql.functions is available under the alias F.

Instructions
100 XP

- Split the content of the '_c0' column on the tab character and store in a variable called split_cols.
- Add the following columns based on the first four entries in the variable above: folder, filename, width, height on a DataFrame named split_df.
- Add the split_cols variable as a column.

'''
# Split the content of _c0 on the tab character (aka, '\t')
split_cols = F.split(annotations_df["_c0"], '\t')

# Add the columns folder, filename, width, and height
split_df = annotations_df.withColumn('folder', split_cols.getItem(0))
split_df = split_df.withColumn('filename', split_cols.getItem(1))
split_df = split_df.withColumn('width', split_cols.getItem(2))
split_df = split_df.withColumn('height', split_cols.getItem(3))

# Add split_cols as a column
split_df = split_df.withColumn('split_cols', split_cols)
