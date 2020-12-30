'''
Filtering on multiple conditions


So far, you've selectively imported records that met a single condition, but it's also common to filter datasets on multiple criteria. In this exercise, you'll do just that.

The weather table contains daily high and low temperatures and precipitation amounts for New York City. Let's focus on inclement weather, where there was either an inch or more of snow or the high was at or below freezing (32° Fahrenheit). To do this, you'll need to build a query that uses the OR operator to look at values in both columns.

pandas is loaded as pd, and a database engine, engine, has been created.

Instructions
100 XP

- Create a query that selects records in weather where tmax is less than or equal to 32 degrees OR snow is greater than or equal to 1 inch.
- Use read_sql() to query the database and assign the result to the variable wintry_days.
- View summary statistics with the describe() method to make sure all records in the data frame meet the given criteria.

'''

# Create query for records with max temps <= 32 or snow >= 1
query = """
SELECT * 
  FROM weather
 WHERE tmax <= 32
    OR snow >= 1;
"""

# Query database and assign result to wintry_days
wintry_days = pd.read_sql(query, engine)

# View summary stats about the temperatures
print(wintry_days.describe())
