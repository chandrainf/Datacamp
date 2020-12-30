'''
Syntax order - Japan earthquakes


Your friend is impressed by your querying skills. She decides to create a query on her own that shows all earthquakes in Japan that were a magnitude of 8 or higher. She has constructed a query based on how she thought about what she requires. Her query will produce an error because of the incorrect ordering of the syntax. Also, the code requires reformatting to make it easy to read.

FROM Earthquakes WHERE Country = 'JP' AND Magnitude >= 8 SELECT Date, Place ,NearestPop, Magnitude ORDER BY Magnitude DESC;

You will fix the query for her with a better coding format and correct the SQL syntax order.

Instructions
100 XP

-Rearrange the query with the correct syntax order in the format provided.

'''
-- Your query
SELECT Date,
Place,
NearestPop,
Magnitude
FROM Earthquakes
WHERE Country = 'JP'
AND Magnitude >= 8
ORDER BY Magnitude DESC
