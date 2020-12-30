'''
Grouping and aggregating data


Often you will want to compute a metric over a set of values that share a common characteristic, like the average price of a house in a certain region. To achieve this, you would need to group the data by region and compute an aggregate metric on that subgroup of data.

We’ve already seen in the video a couple of these aggregation metrics, on landingprices.csv_. We’ll inspect a few more now and apply them to _~/workspace/mnt/data_lake/landing/purchased.csv_. In particular, you’ll use the spark.sql aggregation functions avg() to compute the average value of some column in a group, stddev_samp() to compute the standard (sample) deviation and max() (which we alias as sfmax so as not to shadow Python’s built-in max()) to retrieve the largest value of some column in a group.

Instructions
100 XP

- Use the .groupBy() method to group the data by the “Country” column.
- In these groups, compute the average of the “Salary” column and name the resulting column “average_salary”.
- Compute the standard deviation of the “Salary” column in each group in the same aggregation.
- Retrieve the largest “Salary” in each group, in the same aggregation, and name the resulting column “highest_salary”.

'''
from pyspark.sql.functions import col, avg, stddev_samp, max as sfmax

aggregated = (purchased
              # Group rows by 'Country'
              .groupBy(col('Country'))
              .agg(
                  # Calculate the average salary per group
                  avg('Salary').alias('average_salary'),
                  # Calculate the standard deviation per group
                  stddev_samp('Salary'),
                  # Retain the highest salary per group
                  sfmax('Salary').alias('highest_salary')
              )
              )

aggregated.show()
