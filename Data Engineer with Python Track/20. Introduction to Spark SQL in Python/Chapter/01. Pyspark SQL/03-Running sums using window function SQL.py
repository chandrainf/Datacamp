'''
Running sums using window function SQL


A window function is like an aggregate function, except that it gives an output for every row in the dataset instead of a single row per group.

You can do aggregation along with window functions. A running sum using a window function is simpler than what is required using joins. The query duration can also be much faster.

A table called schedule, having columns train_id, station, time, and diff_min is provided for you. The diff_min column gives the elapsed time between the current station and the next station on the line.

Instructions
100 XP

- Run a query that adds an additional column to the records in this dataset called running_total. The column running_total SUM()s the difference between station time given by the diff_min column.
- Run the query and display the result.

'''
# Add col running_total that sums diff_min col in each group
query = """
SELECT train_id, station, time, diff_min,
SUM(diff_min) OVER (PARTITION BY train_id ORDER BY time) AS running_total
FROM schedule
"""

# Run the query and display the result
spark.sql(query).show()
