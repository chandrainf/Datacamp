'''
EXCEPT


EXCEPT does the opposite of INTERSECT. It is used to check if data, present in one table, is absent in another.

You want to know which countries have no recorded earthquakes. You can get this information by comparing the Nations table with the Earthquakes table.

Instructions
100 XP

- Add the country code column from the Nations table.
- Add the operator that compares the two queries.
- Add the table with country codes to the right query.

'''
SELECT Code2 - - Add the country code column
FROM Nations

EXCEPT - - Add the operator to compare the two queries

SELECT Country
FROM Earthquakes
-- Table with country codes
