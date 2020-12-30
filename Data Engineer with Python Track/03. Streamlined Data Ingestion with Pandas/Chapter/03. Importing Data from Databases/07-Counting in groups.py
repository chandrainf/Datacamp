'''
Counting in groups
In previous exercises, you pulled data from tables, then summarized the resulting data frames in pandas to create graphs. By using COUNT and GROUP BY in a SQL query, we can pull those summary figures from the database directly.

The hpd311calls table has a column, complaint_type, that categorizes call records by issue, such as heating or plumbing. In order to graph call volumes by issue, you'll write a SQL query that COUNTs records by complaint type.

pandas has been imported as pd, and the database engine for data.db has been created as engine.

Instructions
100 XP

- Create a SQL query that gets the complaint_type column and counts of all records from hpd311calls, grouped by complaint_type.
- Create a data frame with read_sql() of call counts by issue, calls_by_issue.
- Run the last section of code to graph the number of calls for each housing issue.

'''

# Create query to get call counts by complaint_type
query = """
SELECT complaint_type, 
       COUNT(*)
  FROM hpd311calls
 GROUP BY complaint_type;
"""

# Create data frame of call counts by issue
calls_by_issue = pd.read_sql(query, engine)

# Graph the number of calls for each housing issue
calls_by_issue.plot.barh(x="complaint_type")
plt.show()
