'''
SQL and Parquet


Parquet files are perfect as a backing data store for SQL queries in Spark. While it is possible to run the same queries directly via Spark's Python functions, sometimes it's easier to run SQL queries alongside the Python options.

For this example, we're going to read in the Parquet file we created in the last exercise and register it as a SQL table. Once registered, we'll run a quick query against the table (aka, the Parquet file).

The spark object and the AA_DFW_ALL.parquet file are available for you automatically.

Instructions
100 XP

- Import the AA_DFW_ALL.parquet file into flights_df.
- Use the createOrReplaceTempView method to alias the flights table.
- Run a Spark SQL query against the flights table.

'''
# Read the Parquet file into flights_df
flights_df = spark.read.parquet('AA_DFW_ALL.parquet')

# Register the temp table
flights_df.createOrReplaceTempView('flights')

# Run a SQL query of the average flight duration
avg_duration = spark.sql(
    'SELECT avg(flight_duration) from flights').collect()[0]
print('The average flight time is: %d' % avg_duration)
