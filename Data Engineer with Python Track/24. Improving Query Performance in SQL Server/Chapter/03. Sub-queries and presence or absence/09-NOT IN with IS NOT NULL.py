'''
NOT IN with IS NOT NULL


You want to know which country capitals have never been the closest city to recorded earthquakes. You decide to use NOT IN to compare Capital from the Nations table, in the outer query, with NearestPop, from the Earthquakes table, in a sub-query.

Instructions 1/2
50 XP

- Add the country capital name column to the outer query.
- Add the city name column to the sub-query.
- Check how many rows the query returns. Does this mean that earthquakes have been recorded near every capital city in the world?


'''
SELECT WorldBankRegion,
CountryName,
Capital - - Capital city name column
FROM Nations
WHERE Capital NOT IN
(SELECT NearestPop - - City name column
 FROM Earthquakes)


'''
Instructions 2/2
50 XP

The column in the SELECT statement of the sub-query contains NULL values and will require a filter to remove the NULL values from the query.

    -Add the WHERE filter condition to the sub-query to get the query working correctly.

'''
SELECT WorldBankRegion,
CountryName,
Capital
FROM Nations
WHERE Capital NOT IN
(SELECT NearestPop
 FROM Earthquakes
 WHERE  NearestPop IS NOT NULL)
-- filter condition
