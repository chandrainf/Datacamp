'''
Reading a CSV file


Loading the data is the first step in building a data transformation pipeline. “Comma separated values” (CSV) is a file commonly used file format for data exchange. You’re now going to use Spark to read a CSV file.

You’ve seen in the videos how to load landing/prices.csv. Now let’s do the same for landing/ratings.csv, step by step. Remember, the actual data lake is made available to you under ~/workspace/mnt/data_lake.

A SparkSession named spark has already been loaded for you.

Instructions
100 XP

- Create a DataFrameReader object using the spark.read property.
- Make the reader object use the header of the CSV file to name the columns automatically, by passing in the correct keyword arguments to the reader’s .options() method

'''
# Read a csv file and set the headers
df = (spark.read
      .options(header=True)
      .csv("/home/repl/workspace/mnt/data_lake/landing/ratings.csv"))
df.show()
