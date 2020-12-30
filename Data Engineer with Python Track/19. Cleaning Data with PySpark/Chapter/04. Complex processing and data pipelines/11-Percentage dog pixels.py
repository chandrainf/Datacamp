'''
Percentage dog pixels


The final task for parsing the dog annotation data is to determine the percentage of pixels in each image that represents a dog (or dogs). You'll need to use the various techniques you've learned in this course to help calculate this information and add it as columns for later analysis.

To calculate the percentage of pixels, first calculate the total number of pixels representing each dog then sum them for the image. You can calculate the bounding box with the formula:

    (Xend - Xstart) * (Yend - Ystart)

NOTE: You can ignore the possibility of overlapping bounding boxes in this instance.

For the percentage, calculate the total number of "dog" pixels divided by the total size of the image, multiplied by 100.
The joined_df DataFrame is as you last used it. pyspark.sql.functions is aliased to F.

Instructions
100 XP

- Define a Python function to take a list of tuples (the dog objects) and calculate the total number of "dog" pixels per image.
- Create a UDF of the function and use it to create a new column called 'dog_pixels' on the DataFrame.
- Create another column, 'dog_percent', representing the percentage of 'dog_pixels' in the image. Make sure this is between 0-100%. Use the string name of the column alone (ie, "columnname" rather than df.columnname).
- Show the first 10 rows with more than 60% 'dog_pixels' in the image. Use a SQL style string for this (ie, 'columnname > ____').

'''

# Define a UDF to determine the number of pixels per image


def dogPixelCount(doglist):
    totalpixels = 0
    for dog in doglist:
        totalpixels += (dog[3] - dog[1]) * (dog[4] - dog[2])
    return totalpixels


# Define a UDF for the pixel count
udfDogPixelCount = F.udf(dogPixelCount, IntegerType())
joined_df = joined_df.withColumn('dog_pixels', udfDogPixelCount('dogs'))

# Create a column representing the percentage of pixels
joined_df = joined_df.withColumn(
    'dog_percent', (joined_df.dog_pixels / (joined_df.width * joined_df.height)) * 100)

# Show the first 10 annotations with more than 60% dog
joined_df.where('dog_percent > 60').show(10)
