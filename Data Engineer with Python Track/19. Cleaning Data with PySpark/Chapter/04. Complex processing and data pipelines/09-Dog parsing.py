'''
Dog parsing


You've done a considerable amount of cleanup on the initial dataset, but now need to analyze the data a bit deeper. There are several questions that have now come up about the type of dogs seen in an image and some details regarding the images. You realize that to answer these questions, you need to process the data into a specific type. Before you can use it, you'll need to create a schema / type to represent the dog details.

The joined_df DataFrame is as you last defined it, and the pyspark.sql.types have all been imported.

Instructions
100 XP

- Select the column representing the dog details from the DataFrame and show the first 10 un-truncated rows.
- Create a new schema as you've done before, using breed, start_x, start_y, end_x, and end_y as the names. Make sure to specify the proper data types for each field in the schema (any number value is an integer).

'''
# Select the dog details and show 10 untruncated rows
print(joined_df.select('dog_list').show(10, truncate=False))

# Define a schema type for the details in the dog list
DogType = StructType([
    StructField("breed", StringType(), False),
    StructField("start_x", IntegerType(), False),
    StructField("start_y", IntegerType(), False),
    StructField("end_x", IntegerType(), False),
    StructField("end_y", IntegerType(), False)
])
