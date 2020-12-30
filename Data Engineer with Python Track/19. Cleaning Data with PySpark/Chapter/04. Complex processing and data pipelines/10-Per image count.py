'''
Per image count


Your next task in building a data pipeline for this dataset is to create a few analysis oriented columns. You've been asked to calculate the number of dogs found in each image based on your dog_list column created earlier. You have also created the DogType which will allow better parsing of the data within some of the data columns.

The joined_df is available as you last defined it, and the DogType StructType is defined. pyspark.sql.functions is available under the F alias.

Instructions
100 XP

- Create a Python function to split each entry in dog_list to its appropriate parts. Make sure to convert any strings into the appropriate types or the DogType will not parse correctly.
- Create a UDF using the above function.
- Use the UDF to create a new column called dogs. Drop the previous column in the same command.
- Show the number of dogs in the new column for the first 10 rows.

'''
# Create a function to return the number and type of dogs as a tuple


def dogParse(doglist):
    dogs = []
    for dog in doglist:
        (breed, start_x, start_y, end_x, end_y) = dog.split(',')
        dogs.append((breed, int(start_x), int(
            start_y), int(end_x), int(end_y)))
    return dogs


# Create a UDF
# ArrayType(schemaName)
udfDogParse = F.udf(dogParse, ArrayType(DogType))

# Use the UDF to list of dogs and drop the old column
joined_df = joined_df.withColumn(
    'dogs', udfDogParse('dog_list')).drop('dog_list')

# Show the number of dogs in the first 10 rows
joined_df.select(F.size('dogs')).show(10)
