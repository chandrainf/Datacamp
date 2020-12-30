'''
Unique 5-tuples in sorted order


A previous lesson taught an operation that eliminates duplicates, fetching unique records. In a previous exercise you obtained common 5-tuples. We will combine these two capabilities to find the unique 5-tuples, sorted alphabetically in descending order.

The table text contains the first four chapters of the Sherlock Holmes text. It has the following columns: word, id, and part.

Instructions
100 XP

- Retrieve the last ten unique 5-tuples sorted alphabetically in descending order.

'''
# Unique 5-tuples sorted in descending order
query = """
SELECT DISTINCT w1, w2, w3, w4, w5 FROM (
   SELECT word AS w1,
   LEAD(word,1) OVER(PARTITION BY part ORDER BY id ) AS w2,
   LEAD(word,2) OVER(PARTITION BY part ORDER BY id ) AS w3,
   LEAD(word,3) OVER(PARTITION BY part ORDER BY id ) AS w4,
   LEAD(word,4) OVER(PARTITION BY part ORDER BY id ) AS w5
   FROM text
)
ORDER BY w1 DESC, w2 DESC, w3 DESC, w4 DESC, w5 DESC 
LIMIT 10
"""
df = spark.sql(query)
df.show()
