'''
SELECT what you need


Your friend is a seismologist, and she is doing a study on earthquakes in South East Asia. She asks you for a query that returns coordinate locations, strength, depth and nearest city of all earthquakes in Papua New Guinea and Indonesia.

All the information you need is in the Earthquakes table, and your initial interrogation of the data tells you that the column for the country code is Country and that the Codes for Papua New Guinea and Indonesia are PG and ID respectively.

Instructions 1/2
50 XP

'''

-SELECT all rows and columns from the Earthquakes table.
-Look at the results of the query to determine which other columns to select.

SELECT *
FROM Earthquakes


'''
Instructions 2/2
50 XP

-Complete the query to select only the required columns and filter for only the requested countries.

'''

SELECT Latitude, -- Y location coordinate column
Longitude, -- X location coordinate column
Magnitude, -- Earthquake strength column
Depth, -- Earthquake depth column
NearestPop - - Nearest city column
FROM Earthquakes
WHERE Country = 'PG' - - Papua New Guinea country code
OR Country = 'ID'
-- Indonesia country code
