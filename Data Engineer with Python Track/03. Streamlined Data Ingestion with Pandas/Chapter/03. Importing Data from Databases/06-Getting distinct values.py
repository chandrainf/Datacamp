'''
Getting distinct values


Sometimes an analysis doesn't need every record, but rather unique values in one or more columns. Duplicate values can be removed after loading data into a data frame, but it can also be done at import with SQL's DISTINCT keyword.

Since hpd311calls contains data about housing issues, we would expect most records to have a borough listed. Let's test this assumption by querying unique complaint_type/borough combinations.

pandas has been imported as pd, and the database engine has been created as engine.

Note: The SQL checker is quite picky about column positions and expects fields to be selected in the specified order.

Instructions
100 XP

- Create a query that gets DISTINCT values for borough and complaint_type (in that order) from hpd311calls.
- Use read_sql() to load the results of the query to a data frame, issues_and_boros.
- Print the data frame to check if the assumption that all issues besides literature requests appear with boroughs listed.

'''
# Create query for unique combinations of borough and complaint_type
query = """
SELECT DISTINCT borough, 
       complaint_type
  FROM hpd311calls;
"""

# Load results of query to a data frame
issues_and_boros = pd.read_sql(query, engine)

# Check assumption about issues and boroughs
print(issues_and_boros)
