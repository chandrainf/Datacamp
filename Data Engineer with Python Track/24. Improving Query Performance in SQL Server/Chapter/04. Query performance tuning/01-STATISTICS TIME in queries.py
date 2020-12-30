'''
STATISTICS TIME in queries


A friend is writing a training course on how the command STATISTICS TIME can be used to tune query performance and asks for your help to complete a presentation. He requires two queries that return NBA team details where the host city had a 2017 population of more than two million.

NBA team details can be queried from the NBA Season 2017-2018 database and city populations can be queried by adding in tables from the Earthquakes database.

Each query uses a different filter on the Teams table.

Query 1

    - Filters the Teams table using IN and three sub-queries

Query 2

    - Filters the Teams table using EXISTS

Instructions 1/4
25 XP

-Turn on STATISTICS TIME.

'''

SET STATISTICS TIME ON - - Turn the time command on


'''
Instructions 2/4
25 XP

For Query 1:

- Add the filter operator for each sub-query.
- Add the table from the Earthquakes database to the first query.

'''
-- Query 1
SELECT *
FROM Teams
-- Sub-query 1
WHERE City IN - - Sub-query filter operator
(SELECT CityName
 FROM Cities) - - Table from Earthquakes database
-- Sub-query 2
AND City IN - - Sub-query filter operator
(SELECT CityName
 FROM Cities
 WHERE CountryCode IN('US', 'CA'))
-- Sub-query 3
AND City IN - - Sub-query filter operator
(SELECT CityName
 FROM Cities
 WHERE Pop2017 > 2000000)


'''
Instructions 3/4
25 XP

For Query 2

- Add the filter operator for the sub-query.
- Add the two city name columns being compared to the sub-query.

'''

-- Query 2
SELECT *
FROM Teams AS t
WHERE EXISTS - - Sub-query filter operator
(SELECT 1
 FROM Cities AS c
 WHERE t.City=c.CityName - - Columns being compared
 AND c.CountryCode IN('US', 'CA')
 AND c.Pop2017 > 2000000)


'''
Instructions 4/4
25 XP

- Turn off STATISTICS TIME.

'''

SET STATISTICS TIME OFF-- Turn the time command off
