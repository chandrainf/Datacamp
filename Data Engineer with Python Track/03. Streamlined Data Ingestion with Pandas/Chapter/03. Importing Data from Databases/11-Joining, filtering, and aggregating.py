'''
Joining, filtering, and aggregating


In this exercise, you'll use what you've learned to assemble a dataset to investigate how the number of heating complaints to New York City's 311 line varies with temperature.

In addition to the hpd311calls table, data.db has a weather table with daily high and low temperature readings for NYC. We want to get each day's count of heat/hot water calls with temperatures joined in. This can be done in one query, which we'll build in parts.

In part one, we'll get just the data we want from hpd311calls. Then, in part two, we'll modify the query to join in weather data.

pandas has been imported as pd, and the database engine has been created as engine.

Instructions 1/2
50 XP

- Complete the query to get created_date and counts of records whose complaint_type is HEAT/HOT WATER from hpd311calls by date.
- Create a data frame,df, containing the results of the query.

'''

# Query to get heat/hot water call counts by created_date
query = """
SELECT hpd311calls.created_date, 
       COUNT(*)
  FROM hpd311calls 
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
 GROUP BY hpd311calls.created_date;
"""

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())


'''
Instructions 2/2
50 XP

- Modify the query to join tmax and tmin from the weather table. (There is only one record per date in weather, so we do not need SQL's MAX and MIN functions here.) Join the tables on created_date in hpd311calls and date in weather.

'''
# Modify query to join tmax and tmin from weather by date
query = """
SELECT hpd311calls.created_date, 
       COUNT(*), 
       weather.tmax, 
       weather.tmin
  FROM hpd311calls 
       JOIN weather 
       ON hpd311calls.created_date = weather.date
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
 GROUP BY hpd311calls.created_date;
 """

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())
