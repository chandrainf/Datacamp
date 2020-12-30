'''
String to integer


Now you'll use the .cast() method you learned in the previous exercise to convert all the appropriate columns from your DataFrame model_data to integers!

To convert the type of a column using the .cast() method, you can write code like this:

    dataframe = dataframe.withColumn("col", dataframe.col.cast("new_type"))
Instructions
100 XP

-Use the method .withColumn() to .cast() the following columns to type "integer". Access the columns using the df.col notation:
    -model_data.arr_delay
    -model_data.air_time
    -model_data.month
    -model_data.plane_year

'''
# Cast the columns to integers
model_data = model_data.withColumn("arr_delay",
                                   model_data.arr_delay.cast("integer"))
model_data = model_data.withColumn("air_time",
                                   model_data.air_time.cast("integer"))
model_data = model_data.withColumn("month",
                                   model_data.month.cast("integer"))
model_data = model_data.withColumn("plane_year",
                                   model_data.plane_year.cast("integer"))
