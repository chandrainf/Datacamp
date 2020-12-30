'''
Aliasing - team BMI


A basketball statistician would like to know the average Body Mass Index (BMI) per NBA team, in particular, any team with an average BMI of 25 or more. To include Team in the query, you will need to join the Players table to the PlayerStats table. The query will require aliasing to:

    - Easily identify joined tables and associated columns.
    - Identify sub-queries.
    - Avoid ambiguity in column names.
    - Identify new columns.

Instructions
100 XP

- Alias the new average BMI column as AvgTeamBMI.
- Alias the PlayerStats table as ps.
- Alias the sub-query as p.
- The PlayerStats table and sub-query are joining on the column PlayerName. Add the aliases to the joining PlayerName columns.

'''

SELECT Team,
   ROUND(AVG(BMI), 2) AS AvgTeamBMI - - Alias the new column
FROM PlayerStats as ps - - Alias PlayerStats table
INNER JOIN
		(SELECT PlayerName, Country,
			Weight_kg/SQUARE(Height_cm/100) BMI
		 FROM Players) as p - - Alias the sub-query
             -- Alias the joining columns
	ON ps.PlayerName = p.PlayerName 
GROUP BY Team
HAVING AVG(BMI) >= 25;
