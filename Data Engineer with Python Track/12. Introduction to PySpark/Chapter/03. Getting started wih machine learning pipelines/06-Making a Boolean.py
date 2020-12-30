'''
Making a Boolean


Consider that you're modeling a yes or no question: is the flight late? However, your data contains the arrival delay in minutes for each flight. Thus, you'll need to create a boolean column which indicates whether the flight was late or not!

Instructions
100 XP

- Use the .withColumn() method to create the column is_late. This column is equal to model_data.arr_delay > 0.
- Convert this column to an integer column so that you can use it in your model and name it label (this is the default name for the response variable in Spark's machine learning routines).
- Filter out missing values (this has been done for you).

'''

# Create is_late
model_data = model_data.withColumn("is_late", model_data.arr_delay > 0)

# Convert to an integer
model_data = model_data.withColumn("label", model_data.is_late.cast("integer"))

# Remove missing values
model_data = model_data.filter(
    "arr_delay is not NULL and dep_delay is not NULL and air_time is not NULL and plane_year is not NULL")
