'''
Further parsing


You've molded this dataset into a significantly different format than it was before, but there are still a few things left to do. You need to prep the column data for use in later analysis and remove a few intermediary columns.

The spark context is available and pyspark.sql.functions is aliased as F. The types from pyspark.sql.types are already imported. The split_df DataFrame is as you last left it. Remember, you can use .printSchema() on a DataFrame in the console area to view the column names and types.

Instructions
100 XP

- Create a new function called retriever that takes two arguments, the split columns (cols) and the total number of columns (colcount). This function should return a list of the entries that have not been defined as columns yet (i.e., everything after item 4 in the list).
- Define the function as a Spark UDF, returning an Array of strings.
- Create the new column dog_list using the UDF and the available columns in the DataFrame.
- Remove the columns _c0, colcount, and split_cols.

'''


def retriever(cols, colcount):
    # Return a list of dog data
    return cols[4:colcount]


# Define the method as a UDF
udfRetriever = F.udf(retriever, ArrayType(StringType()))

# Create a new column using your UDF
split_df = split_df.withColumn('dog_list', udfRetriever(
    split_df['split_cols'], split_df['colcount']))

# Remove the original column, split_cols, and the colcount
split_df = split_df.drop('_c0').drop('colcount').drop('split_cols')
