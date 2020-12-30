'''
Sub-query vs INNER JOIN


Often the results from a correlated sub-query can be replicated using an INNER JOIN. Depending on what your requirements are, using an INNER JOIN may be more efficient because it only makes one pass through the data whereas the correlated sub-query must execute for each row in the outer query.

You want to find out the 2017 population of the biggest city for every country in the world. You can get this information from the Earthquakes database with the Nations table as the outer query and Cities table in the sub-query.

You will first create this query as a correlated sub-query then rewrite it using an INNER JOIN.

Instructions 1/2
50 XP

- Add the 2017 population column from the Cities table.
- Add the outer query country code column to the sub-query.
- Add the outer query table.

'''

SELECT
n.CountryName,
(SELECT MAX(c.Pop2017) - - Add 2017 population column
 FROM Cities AS c
 - - Outer query country code column
 WHERE c.CountryCode=n.Code2) AS BiggestCity
FROM Nations AS n
-- Outer query table


'''
Instructions 2/2
50 XP

- Join the Nations table to the sub-query.
- Add the joining country code columns from the Nations table and sub-query.

'''

SELECT n.CountryName,
c.BiggestCity
FROM Nations AS n
INNER JOIN - - Join the Nations table and sub-query
(SELECT CountryCode,
 MAX(Pop2017) AS BiggestCity
 FROM Cities
 GROUP BY CountryCode) AS c
ON n.Code2 = c.CountryCode
-- Add the joining columns
