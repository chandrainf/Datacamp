'''
INTERSECT


INTERSECT is one of the easier and more intuitive methods used to check if data in one table is present in another.

You want to know which, if any, country capitals are listed as the nearest city to recorded earthquakes. You can get this information by comparing the Nations table with the Earthquakes table.

Instructions
100 XP

- Add the table with country capital cities to the left query.
- Add the operator that compares the two queries.
- Add the city name column from the Earthquakes table.

'''

SELECT Capital
FROM Nations - - Table with capital cities

INTERSECT - - Add the operator to compare the two queries

SELECT NearestPop - - Add the city name column
FROM Earthquakes
