'''
Comparing names with SOUNDEX()


Messy strings like 'Ilynois' instead of 'Illinois' can cause problems when analyzing data. That is why it is important to detect them.

When analyzing the flight_statistics table, you realize that some statistician_name and statistician_surname are written in a different way, such as Miriam Smith and Myriam Smyth. You are afraid there are more differences like this, so you want to check all these names.

You think about comparing with SOUNDEX() the names of the statisticians. If the result of SOUNDEX() is the same, but the texts you are comparing are different, you will find the data you need to clean.

Instructions
100 XP

- Select the distinct values of statistician_name and statistician_surname columns from S1.
- Inner join the flight_statistics table as S2 on similar-sounding first names and surnames using SOUNDEX().
- Filter out values where the statistician_name and statistician_surname columns are different from each other in S1 and S2, respectively.


'''
SELECT
-- First name and surname of the statisticians
DISTINCT S1.statistician_name, S1.statistician_surname
-- Join flight_statistics with itself
FROM flight_statistics S1 INNER JOIN flight_statistics S2
-- The SOUNDEX result of the first name and surname have to be the same
ON SOUNDEX(S1.statistician_name) = SOUNDEX(S2.statistician_name)
AND SOUNDEX(S1.statistician_surname) = SOUNDEX(S2.statistician_surname)
-- The texts of the first name or the texts of the surname have to be different
WHERE S1.statistician_name <> S2.statistician_name
OR S1.statistician_surname <> S2.statistician_surname
