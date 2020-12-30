'''
Creating a UDF for vector data


A dataframe df is available, having a column output of type vector. Its first five rows are shown in the console.

Instructions
100 XP

- Create a UDF called first_udf. It selects the first element of a vector column. Set the result to a default value of 0.0 for any item that is not a vector containing at least one item and cast the output as a float.
- Use the select operation on df to apply first_udf to the output column.

'''

# Selects the first element of a vector column
first_udf = udf(lambda x:
                float(x.indices[0])
                if (x and hasattr(x, "toArray") and x.numNonzeros())
                else 0.0,
                FloatType())

# Apply first_udf to the output column
df.select(first_udf("output").alias("result")).show(5)
