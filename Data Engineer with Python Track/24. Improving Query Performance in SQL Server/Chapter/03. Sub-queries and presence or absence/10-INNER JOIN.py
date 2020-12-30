'''
INNER JOIN

An insurance company that specializes in sports franchises has asked you to assess the geological hazards of cities hosting NBA teams. You believe you can get this information by querying the Teams and Earthquakes tables across the Earthquakes and NBA Season 2017-2018 databases respectively. Your initial query will use EXISTS to compare tables. The second query will use a more appropriate operator.

Instructions 1/3
35 XP

- Add the table for the outer query.
- Add the operator to compare the outer query with the sub-query.
- Add the table for the sub-query.
-Check the results. Only columns from the Teams table are returned.

'''

-- Initial query
SELECT TeamName,
TeamCode,
City
FROM Teams AS t - - Add table
WHERE EXISTS - - Operator to compare queries
(SELECT 1
 FROM Earthquakes AS e - - Add table
 WHERE t.City=e.NearestPop)


'''
Instructions 2/3
35 XP

Something doesn't look right. You'll need columns from the Earthquakes and Teams tables to makes sense of the results.

    -Add the place description and country code where the earthquake occurred.
    -Add the operator to compare the tables.

'''

-- Second query
SELECT t.TeamName,
t.TeamCode,
t.City,
e.Date,
e.place, -- Place description
e.Country - - Country code
FROM Teams AS t
INNER JOIN Earthquakes AS e - - Operator to compare tables
ON t.City = e.NearestPop


'''
Instructions 3/3
30 XP

Question

In this exercise, what does the INNER JOIN help you to determine that EXISTS could not?

Possible Answers

    - Queries that use EXISTS are slower than queries that use INNER JOIN.

    - The INNER JOIN returned two rows, so there must be duplicate rows in the Teams table.

    - The NBA team based in San Antonio, USA has a high risk of earthquake hazards.

    - The earthquakes occurred in San Antonio, Chile, not San Antonio, USA.

Answer : The earthquakes occurred in San Antonio, Chile, not San Antonio, USA.

'''
