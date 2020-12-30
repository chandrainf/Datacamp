'''
Removing missing values


It is common to find missing values in your data. SQL Server represents missing values with NULL.

IS NULL and IS NOT NULL enable you to select or remove the rows where missing values are represented by NULL.

The airport_city column of the airports table has some NULL values. Try to find them!

Instructions 1/2
50 XP

- Use IS NOT NULL to return all the rows from the airports table where airport_city is not missing.

'''
SELECT *
-- Select the appropriate table
FROM airports
-- Exclude the rows where airport_city is NULL
WHERE airport_city IS NOT NULL

'''
Instructions 2/2
50 XP

- Now, use IS NULL to return all the rows from the airports table where airport_city is missing.

'''
SELECT *
-- Select the appropriate table
FROM airports
-- Return only the rows where airport_city is NULL
WHERE airport_city IS NULL
