'''
Commenting - player BMI


Adding comments is a good way to convey what the query is about or information about certain parts of the query.

The sample code is a query on the Players table that returns player name, country of origin and a calculated Body Mass Index (BMI). The WHERE condition is filtering for only players from North America.

You will add the following comment.

    Returns the Body Mass Index (BMI) for all North American players from the 2017-2018 NBA season

Also, you believe that ORDER BY is unnecessary in this query so it will be commented out and a comment added on the same line indicating it is not required.

Instructions
100 XP

- Create a comment block on lines 1 and 4.
- Add the above comment to the block.
- Comment out the ORDER BY statement and add Order by not required comment on the same line.
- Add ; directly after 'Canada' to indicate the new ending of the query.

'''
from the 2017-2018 NBA season
/*
Returns the Body Mass Index(BMI) for all North American players
*/

SELECT PlayerName, Country,
ROUND(Weight_kg/SQUARE(Height_cm/100), 2) BMI
FROM Players
WHERE Country = 'USA'
OR Country = 'Canada'
-- ORDER BY BMI
