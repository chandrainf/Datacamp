'''
Removing blank spaces


You can also find missing data represented with blank spaces ''.

The comparison operators = and <> can help you to select or remove the rows when missing values are represented with blank spaces ''.

The airport_city column of the airports table has some blank spaces. Try to find them!

Instructions 1/2
50 XP

- Use <> to return all the rows from the airports table where airport_city is not missing.

'''

SELECT *
-- Select the appropriate table
FROM airports
-- Exclude the rows where airport_city is missing
WHERE airport_city <> ''

'''
Instructions 2/2
50 XP

Now, use = to return all the rows from the airports table where airport_city is missing.

'''
SELECT *
-- Select the appropriate table
FROM airports
-- Return only the rows where airport_city is missing
WHERE airport_city = ''
