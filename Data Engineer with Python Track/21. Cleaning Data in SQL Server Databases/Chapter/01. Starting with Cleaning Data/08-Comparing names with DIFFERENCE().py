'''
Comparing names with DIFFERENCE()


In the previous exercise, you used SOUNDEX() to check the names of the statisticians from the flight_statistics table.

This time, you want to do something similar, but using the DIFFERENCE() function. DIFFERENCE() returns 4 when there is a similar or identically matching between two strings, and 0 when there is little or no similarity,

If the result of DIFFERENCE() between two strings is 4, but the texts you are comparing are different, you will find the data you need to clean.

Instructions
100 XP

- Select the distinct values of statistician_name and statistician_surname columns from S1.
- Inner join the flight_statistics table as S2 on similar-sounding first names and surnames on instances where the DIFFERENCE between each table's column is 4.
- Filter out values where the statistician_name and statistician_surname columns are different from each other in S1 and S2 respectively.

'''
SELECT
-- First name and surnames of the statisticians
DISTINCT S1.statistician_name, S1.statistician_surname
-- Join flight_statistics with itself
FROM flight_statistics S1 INNER JOIN flight_statistics S2
-- The DIFFERENCE of the first name and surname has to be equals to 4
ON DIFFERENCE(S1.statistician_name, S2.statistician_name) = 4
AND DIFFERENCE(S1.statistician_surname, S2.statistician_surname) = 4
-- The texts of the first name or the texts of the surname have to be different
WHERE S1.statistician_name <> S2.statistician_name
OR S1.statistician_surname <> S2.statistician_surname
