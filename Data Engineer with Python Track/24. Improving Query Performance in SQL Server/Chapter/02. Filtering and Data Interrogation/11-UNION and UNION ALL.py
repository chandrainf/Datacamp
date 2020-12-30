'''
UNION and UNION ALL


You want a query that returns all cities listed in the Earthquakes database. It should be an easy query on the Cities table. However, to be sure you get all cities in the database you will append the query to the Nations table to include capital cities as well. You will use UNION to remove any duplicate rows.

Out of curiosity, you want to know if there were any duplicate rows. If you do the same query but append with UNION ALL instead, and compare the number of rows returned in each query, UNION ALL will return more rows if there are duplicates.

Instructions 1/3
35 XP

- Add the city column from the Cities table to the first query.
- Append queries using UNION
- Add the column for the Nation capital to the second query.
- Check how many rows were returned.

'''

SELECT CityName AS NearCityName, -- City name column
CountryCode
FROM Cities

UNION - - Append queries

SELECT Capital AS NearCityName, -- Nation capital column
Code2 AS CountryCode
FROM Nations


'''
Instructions 2/3
35 XP

- Now append the same queries using UNION ALL.
- Add the column for the country code to the second query.

'''

SELECT CityName AS NearCityName,
CountryCode
FROM Cities

UNION ALL - - Append queries

SELECT Capital AS NearCityName,
Code2 AS CountryCode - - Country code column
FROM Nations


'''
Instructions 3/3
30 XP

Question

Which of the following is true concerning using UNION ALL and UNION on the queries in Step 1 and Step 2. Run the code in the console and experiment appending queries with UNION and UNION ALL.

Possible Answers

    - Using UNION and UNION ALL returns the same number of rows.

    - From looking at the tables, I would not expect any duplicate rows with UNION ALL.

    - More rows are returned with UNION ALL therefore, UNION must be removing duplicates.

    - More rows are returned with UNION therefore, UNION must be adding duplicates.

Answer : More rows are returned with UNION ALL therefore, UNION must be removing duplicates.

'''
