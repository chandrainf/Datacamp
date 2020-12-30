'''
Practicing array column


The SQL function udf is available, as well as a dataframe df_before is available, of type DataFrame[doc: array<string>, in: array<string>, out: array<string>].

The TRIVIAL_TOKENS variable is a set. It contains certain words that we want to remove.

Instructions
100 XP

- Show the rows of df_before where doc contains the item 5.
- Create a udf that removes items in TRIVIAL_TOKENS from an array column. The order does not need to be preserved.
- Remove tokens from the in and out columns in df2 that appear in TRIVIAL_TOKENS.

'''
# Show the rows where doc contains the item '5'
df_before.where(array_contains('doc', '5')).show()

# UDF removes items in TRIVIAL_TOKENS from array
rm_trivial_udf = udf(lambda x:
                     list(set(x) - TRIVIAL_TOKENS) if x
                     else x,
                     ArrayType(StringType()))

# Remove trivial tokens from 'in' and 'out' columns of df2
df_after = df_before.withColumn('in', rm_trivial_udf('in'))\
                    .withColumn('out', rm_trivial_udf('out'))

# Show the rows of df_after where doc contains the item '5'
df_after.where(array_contains('doc', '5')).show()
