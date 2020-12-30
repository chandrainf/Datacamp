'''
Practicing creating a UDF


Sometimes your data needs a transformation that is not supported by built-in functions. This is where a custom user defined function ("UDF") is suitable.

The SQL function udf is available.

A dataframe df2 is available, of type DataFrame[doc: array<string>, in: array<string>, out: array<string>]. It's doc column contains trivial tokens.

The following displays the first 20 rows of df2 where doc contains '1':

df2.where(array_contains('doc','1')).show()
You have two objectives to fulfill:

Ensure that the transformed data consists of nonempty vectors.
A dataframe has a column that contains arrays of string, where each array has a single item. You'd like to transform this column to a string.

Instructions
100 XP

- Create a udf that returns true if and only if the value is a nonempty vector, using numNonzeros()
- Create a udf that returns the first element of the array and returns its string representation.

'''
# Returns true if the value is a nonempty vector
nonempty_udf = udf(lambda x:
                   True if (x and hasattr(x, "toArray") and x.numNonzeros())
                   else False, BooleanType())

# Returns first element of the array as string
s_udf = udf(lambda x: str(x[0]) if (x and type(x) is list and len(x) > 0)
            else '', StringType())
