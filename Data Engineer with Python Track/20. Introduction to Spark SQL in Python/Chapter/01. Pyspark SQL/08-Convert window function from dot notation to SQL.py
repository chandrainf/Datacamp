'''
Convert window function from dot notation to SQL


We are going to add a column to a train schedule so that each row contains the number of minutes for the train to reach its next stop.

    - We have a dataframe df where df.columns == ['train_id', 'station', 'time'].
    - df is registered as a SQL table named schedule.
    - The following window function query uses dot notation. It gives a new dataframe dot_df.

    window = Window.partitionBy('train_id').orderBy('time')
    dot_df = df.withColumn('diff_min', 
                        (unix_timestamp(lead('time', 1).over(window),'H:m') 
                        - unix_timestamp('time', 'H:m'))/60)

Note the use of the unix_timestamp function, which is equivalent to the UNIX_TIMESTAMP SQL function.

Please be aware of the scaffolding in the sample code. Formatting the answer according to the scaffolding will ensure that your submitted answer is not erroneously rejected due to a formatting issue.

Instructions
100 XP

- Create a SQL query to obtain an identical result to dot_df. Please format the query according to the scaffolding.

'''
# Create a SQL query to obtain an identical result to dot_df
query = """SELECT *, 
           (UNIX_TIMESTAMP(LEAD(time, 1) OVER (PARTITION BY train_id ORDER BY time),'H:m') - UNIX_TIMESTAMP(time, 'H:m'))/60 AS diff_min 
           FROM
           schedule """
sql_df = spark.sql(query)
sql_df.show()
