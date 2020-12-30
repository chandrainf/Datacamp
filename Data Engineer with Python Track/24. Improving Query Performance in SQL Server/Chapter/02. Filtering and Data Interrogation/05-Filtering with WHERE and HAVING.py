'''
Filtering with WHERE and HAVING


WHERE and HAVING can be used as filters in the same query. But how we use them, where we use them and what we use them for is quite different.

You want a query that returns the total points contribution of a teams Power Forwards where their total points contribution is greater than 3000.

Instructions
100 XP

- Apply a filter condition for only rows where position equals Power Forward (PF).
- Apply a grouped row filter for total points greater than 3000.

'''

SELECT Team,
SUM(TotalPoints) AS TotalPFPoints
FROM PlayerStats
-- Filter for only rows with power forwards
WHERE Position = 'PF'
GROUP BY Team
-- Filter for total points greater than 3000
HAVING SUM(TotalPoints) > 3000
