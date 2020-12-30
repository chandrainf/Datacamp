'''
Limit the rows with TOP


Your seismologist friend that is doing a study on earthquakes in South East Asia has asked you to subset a query that you provided her. She wants two additional queries for earthquakes recorded in Indonesia and Papua New Guinea. The first returning the ten shallowest earthquakes and the second the upper quartile of the strongest earthquakes.

Instructions 1/2
50 XP

-Limit the number of rows to ten.
-Order the results from shallowest to deepest.


'''
SELECT TOP 10 - - Limit the number of rows to ten
Latitude,
Longitude,
Magnitude,
Depth,
NearestPop
FROM Earthquakes
WHERE Country = 'PG'
OR Country = 'ID'
ORDER BY Depth
-- Order results from shallowest to deepest


'''
Instructions 2/2
50 XP

-Limit rows to the upper quartile.
-Order the results from strongest to weakest earthquake

'''
SELECT TOP 25 PERCENT - - Limit rows to the upper quartile
Latitude,
Longitude,
Magnitude,
Depth,
NearestPop
FROM Earthquakes
WHERE Country = 'PG'
OR Country = 'ID'
ORDER BY Magnitude DESC
-- Order the results
