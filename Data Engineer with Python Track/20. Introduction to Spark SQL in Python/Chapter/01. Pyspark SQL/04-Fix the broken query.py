'''
Fix the broken query


This query runs correctly, but gives an incorrect result in one of the rows because of an omission in the OVER clause. Can you locate the bug? Can you modify the query to make it give a reasonable result?

Instructions
100 XP

- Provide the row number of the erroneous row as an integer.
- Provide the clause (as a string) that when added to the OVER clause fixes the problem.

'''
query = """
SELECT 
ROW_NUMBER() OVER (ORDER BY time) AS row,
train_id, 
station, 
time, 
LEAD(time,1) OVER (ORDER BY time) AS time_next 
FROM schedule
"""
spark.sql(query).show()

# Give the number of the bad row as an integer
bad_row = 7

# Provide the missing clause, SQL keywords in upper case
clause = "PARTITION BY train_id"
