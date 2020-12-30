'''
Joining and filtering


Just as you might not always want all the data in a single table, you might not want all columns and rows that result from a JOIN. In this exercise, you'll use SQL to refine a data import.

Weather exacerbates some housing problems more than others. Your task is to focus on water leak reports in hpd311calls and assemble a dataset that includes the day's precipitation levels from weather to see if there is any relationship between the two. The provided SQL gets all columns in hpd311calls, but you'll need to modify it to get the necessary weather column and filter rows with a WHERE clause.

pandas is loaded as pd, and the database engine, engine, has been created.

Instructions 1/2
50 XP

-Complete query to get the prcp column in weather and join weather to hpd311calls on their date and created_date columns, respectively.
-Use read_sql() to load the results of the query into the leak_calls data frame.

'''
# Query to get hpd311calls and precipitation values
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
    ON hpd311calls.created_date = weather.date;"""

# Load query results into the leak_calls data frame
leak_calls = pd.read_sql(query, engine)

# View the data frame
print(leak_calls.head())


'''
Instructions 2/2
50 XP

Modify query to get only rows that have 'WATER LEAK' as their complaint_type.

'''
# Query to get water leak calls and daily precipitation
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
    ON hpd311calls.created_date = weather.date
 WHERE hpd311calls.complaint_type = 'WATER LEAK';"""

# Load query results into the leak_calls data frame
leak_calls = pd.read_sql(query, engine)

# View the data frame
print(leak_calls.head())
