'''
Conditionally replacing values


Another common situation is that you have values that you want to replace or that don’t make any sense as we saw in the video. You can select the column to be transformed by using the .withColumn() method, conditionally replace those values using the pyspark.sql.functions.when function when values meet a given condition or leave them unaltered when they don’t with the .otherwise() method.

In this exercise, you will do just that by transforming the “comfort” column of the ratings DataFrame (already loaded) by replacing its numeric values with the string "sufficient" when the comfort value is bigger than 3, and "insufficient" when it is not.

Instructions
100 XP

- Use the .withColumn() method to relabel the column named “comfort”.
- Use the when() function to replace values of the “comfort” column larger than 3 with the string "sufficient".
- Use the .otherwise() method to replace remaining values with "insufficient".

'''

from pyspark.sql.functions import col, when

# Add/relabel the column
categorized_ratings = ratings.withColumn(
    "comfort",
    # Express the condition in terms of column operations
    when(col("comfort") > 3, "sufficient").otherwise("insufficient"))

categorized_ratings.show()
