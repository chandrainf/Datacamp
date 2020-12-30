'''
Split and explode a text column


A dataframe clauses_df with 100 rows is provided. It has a column clause and a row id. Each clause is a string containing one or more words separated by spaces.

Instructions
100 XP

- Split the clause column into a column called words, containing an array of individual words.
- Explode the words column into a column called word.
- Count the resulting number of rows.

'''
# Split the clause column into a column called words
split_df = clauses_df.select(split('clause', ' ').alias('words'))
split_df.show(5, truncate=False)

# Explode the words column into a column called word
exploded_df = split_df.select(explode('words').alias('word'))
exploded_df.show(10)

# Count the resulting number of rows in exploded_df
print("\nNumber of rows: ", exploded_df.count())
