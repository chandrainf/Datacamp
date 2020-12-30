'''
Aggregate dot SQL


The following code uses SQL to set the value of a dataframe called df.

    df = spark.sql("""
    SELECT *, 
    LEAD(time,1) OVER(PARTITION BY train_id ORDER BY time) AS time_next 
    FROM schedule
    """)

        - The LEAD clause has an equivalent function in pyspark.sql.functions.
        - The PARTITION BY, and ORDER BY clauses each have an equivalent dot notation function that is called on the Window object.
        - The following imports are available:
            - from pyspark.sql import Window
            - from pyspark.sql.functions import lead

Instructions
100 XP

- Create a dataframe called dot_df that contains the identical result as df, using dot notation instead of SQL.

'''
# Obtain the identical result using dot notation
dot_df = df.withColumn('time_next', lead('time', 1)
                       .over(Window.partitionBy('train_id')
                             .orderBy('time')))
