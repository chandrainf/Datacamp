'''
Label the data


A dataframe df is available having columns endword: string, features: vector, and outvec: vector. You are to select the rows where endword equals "him", and add a column label having the integer value 1. Then, use the union operation to add an equal number of rows having endword not equals to him, such that these additional rows have label = 0.

As a reminder, in SQL the not equals comparison is done using <>.

Instructions
100 XP

- Import the lit function.
- Select the rows where endword is 'him' and add a integer column label having the value 1.
- Select the rows where endword is not 'him' and add a integer column label having the value 0.
- Union these two sets, using a number of negative examples equal to the number of positive examples.

'''
# Import the lit function
from pyspark.sql.functions import lit

# Select the rows where endword is 'him' and label 1
df_pos = df.where("endword = 'him'")\
           .withColumn('label', lit(1))

# Select the rows where endword is not 'him' and label 0
df_neg = df.where("endword <> 'him'")\
           .withColumn('label', lit(0))

# Union pos and neg in equal number
df_examples = df_pos.union(df_neg.limit(df_pos.count()))
print("Number of examples: ", df_examples.count())
df_examples.where("endword <> 'him'").sample(False, .1, 42).show(5)
