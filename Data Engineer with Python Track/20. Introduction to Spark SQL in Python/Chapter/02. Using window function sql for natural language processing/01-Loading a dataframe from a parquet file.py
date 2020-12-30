'''
Loading a dataframe from a parquet file


A dataframe file called sherlock_sentences.parquet is available in your workspace. Each row of this dataframe contains a single clause. Each clause is a sequence of words that is separated from other clauses by punctuation, such as periods, quotes, and other natural language delimiters that signify a sentence or sentence fragment. Your mission, if you choose to accept it, is to load this file.

Instructions
100 XP

- Load sherlock_sentences.parquet.
- Filter on "id > 70", and show the first 5 rows.

'''
# Load the dataframe
df = spark.read.load('sherlock_sentences.parquet')

# Filter and show the first 5 rows
df.where('id > 70').show(5, truncate=False)