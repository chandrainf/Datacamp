'''
Creating a SparkSession


We've already created a SparkSession for you called spark, but what if you're not sure there already is one? Creating multiple SparkSessions and SparkContexts can cause issues, so it's best practice to use the SparkSession.builder.getOrCreate() method. This returns an existing SparkSession if there's already one in the environment, or creates a new one if necessary!

Instructions
100 XP

- Import SparkSession from pyspark.sql.
- Make a new SparkSession called my_spark using SparkSession.builder.getOrCreate().
- Print my_spark to the console to verify it's a SparkSession.

'''

# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession

# Create my_spark
my_spark = SparkSession.builder.getOrCreate()

# Print my_spark
print(my_spark)
