'''
Selecting and renaming columns


Transformations are, after ingestion, the next step in data engineering pipelines. Data gets transformed, because certain insights need to be derived. Clear column names help in achieving that goal.

You’ve seen in the videos how to select and rename columns of the landing/prices.csv file. Now do the same for landing/ratings.csv, step by step.

A SparkSession named spark has already been loaded for you and the CSV file was read in a DataFrame called ratings.

Instructions
100 XP

- Select the columns “brand”, “model” and “absorption_rate” from the ratings DataFrame.
- Rename the “absorption_rate” column to “absorbency”.
- Show only the distinct values of the resulting DataFrame.

'''
from pyspark.sql.functions import col

# Select the columns and rename the "absorption_rate" column
result = ratings.select([col("brand"),
                         col("model"),
                         col("absorption_rate").alias("absorbency")])

# Show only unique values
result.distinct().show()
