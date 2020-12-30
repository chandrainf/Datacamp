'''
Grouping and Aggregating II


In addition to the GroupedData methods you've already seen, there is also the .agg() method. This method lets you pass an aggregate column expression that uses any of the aggregate functions from the pyspark.sql.functions submodule.

This submodule contains many useful functions for computing things like standard deviations. All the aggregation functions in this submodule take the name of a column in a GroupedData table.

Remember, a SparkSession called spark is already in your workspace, along with the Spark DataFrame flights. The grouped DataFrames you created in the last exercise are also in your workspace.

Instructions
100 XP

- Import the submodule pyspark.sql.functions as F.
- Create a GroupedData table called by_month_dest that's grouped by both the month and dest columns. Refer to the two columns by passing both strings as separate arguments.
- Use the .avg() method on the by_month_dest DataFrame to get the average dep_delay in each month for each destination.
- Find the standard deviation of dep_delay by using the .agg() method with the function F.stddev().

'''
# Import pyspark.sql.functions as F
import pyspark.sql.functions as F

# Group by month and dest
by_month_dest = flights.groupBy('month', 'dest')

# Average departure delay by month and destination
by_month_dest.avg('dep_delay').show()

# Standard deviation of departure delay
by_month_dest.agg(F.stddev("dep_delay")).show()
