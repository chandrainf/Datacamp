'''
Creating columns


In this chapter, you'll learn how to use the methods defined by Spark's DataFrame class to perform common data operations.

Let's look at performing column-wise operations. In Spark you can do this using the .withColumn() method, which takes two arguments. First, a string with the name of your new column, and second the new column itself.

The new column must be an object of class Column. Creating one of these is as easy as extracting a column from your DataFrame using df.colName.

Updating a Spark DataFrame is somewhat different than working in pandas because the Spark DataFrame is immutable. This means that it can't be changed, and so columns can't be updated in place.

Thus, all these methods return a new DataFrame. To overwrite the original DataFrame you must reassign the returned DataFrame using the method like so:

df = df.withColumn("newCol", df.oldCol + 1)
The above code creates a DataFrame with the same columns as df plus a new column, newCol, where every entry is equal to the corresponding entry from oldCol, plus one.

To overwrite an existing column, just pass the name of the column as the first argument!

Remember, a SparkSession called spark is already in your workspace.

Instructions
100 XP

-Use the spark.table() method with the argument "flights" to create a DataFrame containing the values of the flights table in the .catalog. Save it as flights.
-Show the head of flights using flights.show(). The column air_time contains the duration of the flight in minutes.
-Update flights to include a new column called duration_hrs, that contains the duration of each flight in hours.

'''
# Create the DataFrame flights
flights = spark.table("flights")

# Show the head
print(flights.show())

# Add duration_hrs
flights = flights.withColumn("duration_hrs", flights.air_time / 60)
