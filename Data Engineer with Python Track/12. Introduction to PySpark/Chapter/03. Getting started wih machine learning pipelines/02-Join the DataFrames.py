'''
Join the DataFrames


In the next two chapters you'll be working to build a model that predicts whether or not a flight will be delayed based on the flights data we've been working with. This model will also include information about the plane that flew the route, so the first step is to join the two tables: flights and planes!

Instructions
100 XP

- First, rename the year column of planes to plane_year to avoid duplicate column names.
- Create a new DataFrame called model_data by joining the flights table with planes using the tailnum column as the key.

'''
# Rename year column
planes = planes.withColumnRenamed('year', 'plane_year')

# Join the DataFrames
model_data = flights.join(planes, on='tailnum', how="leftouter")
