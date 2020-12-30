'''
Finding common word sequences


Previously we saw how to create a query that finds word sequences of length three ("3-tuples"). We used that query as a subquery in a traditional SQL query to find the most common 3-tuples in the text document. You will now perform a similar task to find the most common 5-tuples.

Dataframe text_df is available. It contains the first five chapters of the Sherlock Holmes text. It has columns: word, id, part, title. The id column is an integer such that a word that comes later in the document has a larger id than a word that comes before it. The part column separates the data into chapters. The dataframe text_df is also registered as temporary table called text. Our objective is to create a dataset where each row corresponds to a 5-tuple, having a count indicating how many times the tuple occurred in the dataset.

Instructions
100 XP

- Create a query query that finds the 10 most common 5-tuples in the dataset.

'''
# Find the top 10 sequences of five words
query = """
SELECT w1, w2, w3, w4, w5, COUNT(*) AS count FROM (
   SELECT word AS w1,
   LEAD(word,1) OVER(PARTITION BY part ORDER BY id) AS w2,
   LEAD(word,2) OVER(PARTITION BY part ORDER BY id) AS w3,
   LEAD(word,3) OVER(PARTITION BY part ORDER BY id) AS w4,
   LEAD(word,4) OVER(PARTITION BY part ORDER BY id) AS w5
   FROM text
)
GROUP BY w1, w2, w3, w4, w5
ORDER BY count DESC
LIMIT 10 """
df = spark.sql(query)
df.show()
