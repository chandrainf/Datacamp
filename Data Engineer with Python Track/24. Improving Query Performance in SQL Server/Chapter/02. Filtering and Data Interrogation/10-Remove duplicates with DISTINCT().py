'''
Remove duplicates with DISTINCT()


You want to know the closest city to earthquakes with a magnitude of 8 or higher. You can get this information from the Earthquakes table. However, a simple query returns duplicate rows because some cities have experienced more than one magnitude 8 or higher earthquake.

You can remove duplicates by using the DISTINCT() clause. Once you have your results, you would like to know how many times each city has experienced an earthquake of magnitude 8 or higher.

Note that IS NOT NULL is being used because many earthquakes do not occur near any populated area, thankfully.

Instructions 1/3
35 XP

- Add the closest city and view the output of the query to confirm duplicated rows.

'''
SELECT NearestPop, -- Add the closest city
Country
FROM Earthquakes
WHERE Magnitude >= 8
AND NearestPop IS NOT NULL
ORDER BY NearestPop


'''
Instructions 2/3
35 XP

- Add DISTINCT() to the column representing the closest city to remove duplicates.
- Add the filtering condition for earthquakes with a magnitude of 8 or more.

'''
SELECT DISTINCT(NearestPop), -- Remove duplicate city
Country
FROM Earthquakes
WHERE Magnitude >= 8 - - Add filter condition
AND NearestPop IS NOT NULL
ORDER BY NearestPop


'''
Instructions 3/3
30 XP

- Get the number of cities near earthquakes of magnitude 8 or more.
- Add column groupings.

'''

SELECT NearestPop,
Country,
COUNT(NearestPop) NumEarthquakes - - Number of cities
FROM Earthquakes
WHERE Magnitude >= 8
AND Country IS NOT NULL
GROUP BY NearestPop, Country - - Group columns
ORDER BY NumEarthquakes DESC
