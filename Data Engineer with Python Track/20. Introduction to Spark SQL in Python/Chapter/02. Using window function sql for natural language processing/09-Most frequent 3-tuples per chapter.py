'''
Most frequent 3-tuples per chapter


We will now use a query as a subquery in a larger query. Spark SQL supports advanced features of SQL. Previously you learned how to find the most common word sequences over an entire book having 12 chapters. Now you will obtain the most frequent 3-tuple for each of the 12 chapters. You will do this using a window function to retrieve the top row per group.

There is a table having columns word, id, chapter.

  1. The chapter column corresponds to the number of a chapter.
  2. The word column corresponds to a single word in the document.
  3. The id column corresponds to the word position in the document.

We also have the following query:

  subquery = """
  SELECT chapter, w1, w2, w3, COUNT(*) as count
  FROM
  (
      SELECT
      chapter,
      word AS w1,
      LEAD(word, 1) OVER(PARTITION BY chapter ORDER BY id ) AS w2,
      LEAD(word, 2) OVER(PARTITION BY chapter ORDER BY id ) AS w3
      FROM text
  )
  GROUP BY chapter, w1, w2, w3
  ORDER BY chapter, count DESC
  """
  spark.sql(subquery).show(5)
  +-------+---+-----+----+-----+
  |chapter| w1|   w2|  w3|count|
  +-------+---+-----+----+-----+
  |      1| up|   to| the|    6|
  |      1|one|   of| the|    6|
  |      1| in|front|  of|    5|
  |      1| up|  and|down|    5|
  |      1| it|  was|   a|    5|
  +-------+---+-----+----+-----+
  only showing top 5 rows

From this table you can determine that the first row of the desired result will be:

  +-------+---+-----+----+-----+
  |chapter| w1|   w2|  w3|count|
  +-------+---+-----+----+-----+
  |      1| up|   to| the|    6|
  +-------+---+-----+----+-----+

Your task is to use subquery as a subquery in a larger query to obtain the most frequent 3-tuple per chapter. The desired result will have the same schema, but having one row per chapter. Use ROW_NUMBER() to obtain the row number per row per chapter.

Instructions
100 XP

- Get the most frequent 3-tuple per chapter.

'''
#   Most frequent 3-tuple per chapter
query = """
SELECT chapter, w1, w2, w3, count FROM
(
  SELECT
  chapter,
  ROW_NUMBER() OVER (PARTITION BY chapter ORDER BY count DESC) AS row,
  w1, w2, w3, count
  FROM ( %s )
)
WHERE row = 1
ORDER BY chapter ASC
""" % subquery

spark.sql(query).show()
