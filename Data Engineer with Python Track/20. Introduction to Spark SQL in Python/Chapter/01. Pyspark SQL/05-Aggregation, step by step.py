'''
Aggregation, step by step


Whether to use dot notation or SQL is a personal preference. However, as demonstrated in the video exercise, there are cases where SQL is simpler. Also as demonstrated in the video lesson, there are also cases where the dot notation gives a counterintuitive result, such as when a second aggregation on a column clobbers a prior aggregation on that column. As mentioned in the video, the basic syntax of agg in pyspark is only able to do a single aggregation on each column at a time.

The following exercises calculate the time of the first departure for each train line.

The first two queries match. However, the second two do not. Can you determine why?

Instructions
100 XP

- Fill in the blanks to get the first pair of commands to display the identical result.
- The fourth result, named result, is a naive attempt at replicating the previous line. However, it is counter-intuitively different. How? Fill in the blank to print the name of the second column of result.

'''
# Give the identical result in each command
spark.sql(
    'SELECT train_id, MIN(time) AS start FROM schedule GROUP BY train_id').show()  # SQL
df.groupBy('train_id').agg({'time': 'min'}).withColumnRenamed(
    'min(time)', 'start').show()  # Dot Notation

# Print the second column of the result
spark.sql('SELECT train_id, MIN(time), MAX(time) FROM schedule GROUP BY train_id').show()  # SQL
result = df.groupBy('train_id').agg(
    {'time': 'min', 'time': 'max'})  # Dot Notation
result.show()
print(result.columns[1])
