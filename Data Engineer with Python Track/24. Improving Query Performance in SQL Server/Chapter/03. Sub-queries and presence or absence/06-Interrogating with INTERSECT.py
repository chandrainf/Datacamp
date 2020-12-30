'''
Interrogating with INTERSECT


INTERSECT and EXCEPT are very useful for data interrogation.

The Earthquakes and NBA Season 2017-2018 databases both contain information on countries and cities. You are interested to know which countries are represented by players in the 2017-2018 NBA season and you believe you can get the results you require by querying the relevant tables across these two databases.

Use the INTERSECT operator between queries, but be careful and think about the results. Although both tables contain a country name column to compare, these are separate databases and the data may be stored differently.

Instructions 1/2
50 XP

- INTERSECT CountryName from a table in the Earthquakes database and Country from a table in the NBA Season 2017-2018 database.

'''
SELECT CountryName
FROM Nations - - Table from Earthquakes database

INTERSECT - - Operator for the intersect between tables

SELECT Country
FROM Players
-- Table from NBA Season 2017-2018 database


'''
Instructions 2/2
50 XP

Question

With one exception, all NBA teams are USA based, so why does USA not appear in the results? Are there no Americans playing in the NBA?

To help get your answer, use the two queries below;

    1. Delete the query in the query console.
    2. Copy and paste one of the queries into the query console.
    3. Select Run Code to view the results.
    4. Repeat steps 1 to 4 for the other query.

SELECT * 
FROM Nations
WHERE CountryName LIKE 'U%'
SELECT *
FROM Players
WHERE Country LIKE 'U%'

Possible Answers

    - The outer query should be using the Code3 column from the Nations table, not CountryName.

    - The values do not match. In the Nations table, the value for country name is stored as United States of America, and in the Players table, the value is stored as USA.

    - The original query contains filters on the Nations and Players tables for countries other than the USA.

    - INTERSECT is not the correct operator to use. The correct operator to use for this question is EXCEPT.

Answer : The values do not match. In the Nations table, the value for country name is stored as United States of America, and in the Players table, the value is stored as USA.

'''
