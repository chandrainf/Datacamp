'''
Load entire tables


In the last exercise, you saw that data.db has two tables. weather has historical weather data for New York City. hpd311calls is a subset of call records made to the city's 311 help line about housing issues.

In this exercise, you'll use the read_sql() function in pandas to load both tables. read_sql() accepts a string of either a SQL query to run, or a table to load. It also needs a way to connect to the database, like the engine in the provided code.

Instructions 1/2
50 XP

- Use read_sql() to load the hpd311calls table by name, without any SQL.

'''
# Load libraries
import pandas as pd
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine('sqlite:///data.db')

# Load hpd311calls without any SQL
hpd_calls = pd.read_sql("hpd311calls", engine)

# View the first few rows of data
print(hpd_calls.head())


'''
Instructions 2/2
50 XP

Use read_sql() and a SELECT * ... SQL query to load the entire weather table.

'''
# Create the database engine
engine = create_engine("sqlite:///data.db")

# Create a SQL query to load the entire weather table
query = """
SELECT * 
  FROM weather;
"""
# Load weather with the SQL query
weather = pd.read_sql(query, engine)

# View the first few rows of data
print(weather.head())
