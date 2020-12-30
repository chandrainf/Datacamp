'''
The database schema

By now, you know that SQL databases always have a database schema. In the video on databases, you saw the following diagram:

Database Schema for Customer and Order

A PostgreSQL database is set up in your local environment, which contains this database schema. It's been filled with some example data. You can use pandas to query the database using the read_sql() function. You'll have to pass it a database engine, which has been defined for you and is called db_engine.

The pandas package imported as pd will store the query result into a DataFrame object, so you can use any DataFrame functionality on it after fetching the results from the database.

Instructions
100 XP

- Complete the SELECT statement so it selects the first_name and the last_name in the "Customer" table. Make sure to order by the last name first and the first name second.
Use the .head() method to show the first 3 rows of data.
Use .info() to show some general information about data.


'''

# Complete the SELECT statement
data = pd.read_sql("""
SELECT first_name, last_name FROM "Customer"
ORDER BY last_name, first_name
""", db_engine)

print(data.head(3))

# Show the info of the DataFrame
print(data.info())
