'''
Filtering Data


Now that you have a bit of SQL know-how under your belt, it's easier to talk about the analogous operations using Spark DataFrames.

Let's take a look at the .filter() method. As you might suspect, this is the Spark counterpart of SQL's WHERE clause. The .filter() method takes either an expression that would follow the WHERE clause of a SQL expression as a string, or a Spark Column of boolean (True/False) values.

For example, the following two expressions will produce the same output:

    flights.filter("air_time > 120").show()
    flights.filter(flights.air_time > 120).show()

Notice that in the first case, we pass a string to .filter(). In SQL, we would write this filtering task as SELECT * FROM flights WHERE air_time > 120. Spark's .filter() can accept any expression that could go in the WHEREclause of a SQL query (in this case, "air_time > 120"), as long as it is passed as a string. Notice that in this case, we do not reference the name of the table in the string -- as we wouldn't in the SQL request.

In the second case, we actually pass a column of boolean values to .filter(). Remember that flights.air_time > 120 returns a column of boolean values that has True in place of those records in flights.air_time that are over 120, and False otherwise.

Remember, a SparkSession called spark is already in your workspace, along with the Spark DataFrame flights.

Instructions
100 XP

- Use the .filter() method to find all the flights that flew over 1000 miles two ways:
    - First, pass a SQL string to .filter() that checks whether the distance is greater than 1000. Save this as long_flights1.
    - Then pass a column of boolean values to .filter() that checks the same thing. Save this as long_flights2.
- Use .show() to print heads of both DataFrames and make sure they're actually equal!

'''
# Filter flights by passing a string
long_flights1 = flights.filter("distance > 1000")

# Filter flights with a boolean column
long_flights2 = flights.filter(flights.distance > 1000)

# Examine the data to check they're equal
print(long_flights1.show())
print(long_flights2.show())
