'''
Using user defined functions in Spark


You've seen some of the power behind Spark's built-in string functions when it comes to manipulating DataFrames. However, once you reach a certain point, it becomes difficult to process the data in a without creating a rat's nest of function calls. Here's one place where you can use User Defined Functions to manipulate our DataFrames.

For this exercise, we'll use our voter_df DataFrame, but you're going to replace the first_name column with the first and middle names.

The pyspark.sql.functions library is available under the alias F. The classes from pyspark.sql.types are already imported.

Instructions
100 XP

- Edit the getFirstAndMiddle() function to return a space separated string of names, except the last entry in the names list.
- Define the function as a user-defined function. It should return a string type.
- Create a new column on voter_df called first_and_middle_name using your UDF.
- Show the Data Frame.

'''


def getFirstAndMiddle(names):
    # Return a space separated string of names
    return ' '.join(names[:-1])


# Define the method as a UDF
udfFirstAndMiddle = F.udf(getFirstAndMiddle, StringType())

# Create a new column using your UDF
voter_df = voter_df.withColumn(
    'first_and_middle_name', udfFirstAndMiddle(voter_df.splits))

# Show the DataFrame
voter_df.show()
