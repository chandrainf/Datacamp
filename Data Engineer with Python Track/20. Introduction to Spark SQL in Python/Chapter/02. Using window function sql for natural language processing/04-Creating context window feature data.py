'''
Creating context window feature data


The moving window technique is useful for machine learning algorithms models that use context window feature data.

A table text having columns id, word, part, title is available in your workspace. It contains chapters 9, 10, 11 and 12 of the Sherlock Holmes book. The words are already processed and organized into one word per row. Each word has a unique integer index provided by the column id. The id column is lower for words that appear earlier in the text and greater for words appearing later in the text.

The first 10 rows of the dataset for chapter 12 are printed to the console as Table1. The first ten rows of the desired result, constrained to show part 12 (Chapter 12) are printed to the console as Table2. In Table2, the "given" word for the row is provided in column w3. Columns w1 and w2 give the two words immediately prior to the given word. Columns w4 and w5 give the two words immediately after the given word.

Note how w1 and w2 are null for the first row. This is because there are not any words prior to w3 (here, "xii") that are within part 12.

Don't hesitate to refer to the slides available at the right of the console if you forget how something was done in the video.

Instructions
100 XP

- Get the word for each row, along with the previous two words and the subsequent two words.

'''
# Word for each row, previous two and subsequent two words
query = """
SELECT
part,
LAG(word, 2) OVER(PARTITION BY part ORDER BY id) AS w1,
LAG(word, 1) OVER(PARTITION BY part ORDER BY id) AS w2,
word AS w3,
LEAD(word, 1) OVER(PARTITION BY part ORDER BY id) AS w4,
LEAD(word, 2) OVER(PARTITION BY part ORDER BY id) AS w5
FROM text
"""
spark.sql(query).where("part = 12").show(10)
