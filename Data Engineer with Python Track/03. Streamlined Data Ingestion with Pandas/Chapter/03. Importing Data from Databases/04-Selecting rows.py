'''
Selecting rows


SQL WHERE clauses return records whose values meet the given criteria. Passing such a query to read_sql() results in a data frame loaded with only records we are interested in, so there is less filtering to do later on.

The hpd311calls table in data.db has data on calls about various housing issues, from maintenance problems to information requests. In this exercise, you'll use SQL to focus on calls about safety.

pandas has been loaded as pd, and a database engine, engine, has been created for data.db.

Instructions
100 XP

- Create a query that selects all columns of records in hpd311calls that have 'SAFETY' as their complaint_type.
- Use read_sql() to query the database and assign the result to the variable safety_calls.
- Run the last section of code to create a graph of safety call counts in each borough.

'''
# Create query to get hpd311calls records about safety
query = """SELECT *
		     FROM hpd311calls
            WHERE complaint_type = 'SAFETY';"""

# Query the database and assign result to safety_calls
safety_calls = pd.read_sql(query, engine)

# Graph the number of safety calls by borough
call_counts = safety_calls.groupby('borough').unique_key.count()
call_counts.plot.barh()
plt.show()
