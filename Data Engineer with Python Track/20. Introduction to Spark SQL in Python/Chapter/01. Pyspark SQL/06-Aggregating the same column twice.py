'''
Aggregating the same column twice


There are cases where dot notation can be more cumbersome than SQL. This exercise calculates the first and last times for each train line. The following code does this using dot notation.

    from pyspark.sql.functions import min, max, col
    expr = [min(col("time")).alias('start'), max(col("time")).alias('end')]
    dot_df = df.groupBy("train_id").agg(*expr)
    dot_df.show()

    +--------+-----+-----+
    |train_id|start|  end|
    +--------+-----+-----+
    |     217|6:06a|6:59a|
    |     324|7:59a|9:05a|
    +--------+-----+-----+

Your mission is to achieve this same result using a SQL query. The dataframe df has been registered as a table named schedule.

Instructions
100 XP

- Write a SQL query that gives an identical result to the dot notation query.

'''
# Write a SQL query giving a result identical to dot_df
query = "SELECT train_id, min(time) AS start, max(time) AS end FROM schedule GROUP BY train_id"
sql_df = spark.sql(query)
sql_df.show()
