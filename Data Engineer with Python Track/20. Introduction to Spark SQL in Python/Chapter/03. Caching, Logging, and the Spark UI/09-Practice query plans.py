'''
Practice query plans


A dataframe text_df is available. This dataframe is registered as a table called table1.

Instructions
100 XP

- Run explain on text_df.
- Run explain on a SQL query that does a "SELECT COUNT(*) as count" on table1.
- Run explain on a SQL query that counts the number of unique words in table1.

'''
# Run explain on text_df
text_df.explain()

# Run explain on "SELECT COUNT(*) AS count FROM table1"
spark.sql("SELECT COUNT(*) AS count FROM table1").explain()

# Run explain on "SELECT COUNT(DISTINCT word) AS words FROM table1"
spark.sql("SELECT COUNT(DISTINCT word) AS words FROM table1").explain()
