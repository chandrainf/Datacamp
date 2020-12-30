'''
Defining a schema


In the last exercise, you read a CSV file using PySpark. Because you didn’t define a schema, all column values were parsed as strings which can be cumbersome and inefficient to process. You are usually better off defining the data types in a schema yourself.

To do this, you use classes from the pyspark.sql.types module. Its StructType() class expects a list of StructField() instances that allow you to add fields to a schema. Various other types, such as ByteType() and IntegerType() are also defined in this module and can be used to specify the data types of each field. In this exercise, all of these classes have been imported for you.

In the ratings.csv dataset from the previous exercise, the rating values in the columns “absorption_rate” and “comfort” are expressed on a scale from 1 to 5, like with Amazon’s web store. Because of that, they easily fit into a ByteType(), which can hold values between -128 and 127. The other columns are better left as StringType()s.

Feel free to explore the previous Spark DataFrame in the console using df.show() so you can map each column to the correct type.

Instructions
100 XP

- Define the schema for the spreadsheet that has the columns “brand”, “model”, “absorption_rate” and “comfort”, in that order.
- Pass the predefined schema while loading the CSV file using the .schema() method.

'''
# Define the schema
schema = StructType([
    StructField("brand", StringType(), nullable=False),
    StructField("model", StringType(), nullable=False),
    StructField("absorption_rate", ByteType(), nullable=True),
    StructField("comfort", ByteType(), nullable=True)
])

df = (spark
      .read
      .options(header="true")
      # Pass the predefined schema to the Reader
      .schema(schema)
      .csv("/home/repl/workspace/mnt/data_lake/landing/ratings.csv"))
pprint(df.dtypes)
