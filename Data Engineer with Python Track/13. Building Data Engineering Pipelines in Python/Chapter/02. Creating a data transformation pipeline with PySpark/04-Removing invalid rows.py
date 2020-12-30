'''
Removing invalid rows

Data scientists spend a lot of their time cleaning data, because most data sources they work with are not ready for analytics. Hence, the second step in the data transformation pipeline is cleaning the data.

In the previous exercise you have dealt with incorrect data types. In this exercise, you will use Spark to clean a DataFrame, as it contains invalid rows, a common problem with real data.

You’ve seen in the videos how to clean landing/prices_with_invalid_rows.csv. Now do the same for landing/ratings_with_invalid_rows.csv, step by step.

A SparkSession named spark has already been loaded for you.

Instructions
100 XP

- Remove any invalid rows by passing the correct keyword (and associated value) to the reader’s .options() method

'''
# Specify the option to drop invalid rows
ratings = (spark
           .read
           .options(header=True, mode="DROPMALFORMED")
           .csv("/home/repl/workspace/mnt/data_lake/landing/ratings_with_invalid_rows.csv"))
ratings.show()
