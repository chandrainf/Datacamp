'''
Create a new column


In the last exercise, you converted the column plane_year to an integer. This column holds the year each plane was manufactured. However, your model will use the planes' age, which is slightly different from the year it was made!

Instructions
100 XP

- Create the column plane_age using the .withColumn() method and subtracting the year of manufacture (column plane_year) from the year (column year) of the flight.

'''
# Create the column plane_age
model_data = model_data.withColumn(
    "plane_age", model_data.year - model_data.plane_year)
