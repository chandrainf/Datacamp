'''
Sort operator in execution plans


Execution plans can tell us if and where a query used an internal sorting operation. Internal sorting is often required when using an operator in a query that checks for and removes duplicate rows.

You are given an execution plan of a query that returns all cities listed in the Earthquakes database. The query appends queries from the Nations and Cities tables. Use the following execution plan to determine if the appending operator used is UNION or UNION ALL

Execution plan for appending queries exercise

Instructions
100 XP

- Add the operator that the execution plan indicates was used to append the queries.

'''

SELECT CityName AS NearCityName,
CountryCode
FROM Cities

___ - - Append queries

SELECT Capital AS NearCityName,
Code2 AS CountryCode
FROM Nations
