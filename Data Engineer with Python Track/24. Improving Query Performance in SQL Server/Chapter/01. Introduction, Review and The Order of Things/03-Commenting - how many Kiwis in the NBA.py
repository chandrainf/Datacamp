'''
Commenting - how many Kiwis in the NBA?


You and a friend would like to know how many New Zealanders (affectionately known as Kiwis) play in the NBA. Your friend attempts to write a query, but it is not very well formatted and contains several errors. You re-write the query, but you want to keep his original for comparison and future reference.

This exercise requires you to create line comments and comment out blocks of code

Instructions
100 XP

- Add the line comment First attempt, contains errors and inconsistent formatting on line 2.
- Block comment out your friend's query on lines 3 and 11.
- Add the line comment Second attempt - errors corrected and formatting fixed on line 14.
- Remove the block comment syntax from your query on lines 15 and 23.

'''
-- Your friend's query
-- First attempt, contains errors and inconsistent formatting
/*
select PlayerName, p.Country, sum(ps.TotalPoints)
AS TotalPoints
FROM PlayerStats ps inner join Players On ps.PlayerName = p.PlayerName
WHERE p.Country = 'New Zeeland'
Group
by PlayerName, Country
order by Country
*/

-- Your query
-- Second attempt - errors corrected and formatting fixed

SELECT p.PlayerName, p.Country,
SUM(ps.TotalPoints) AS TotalPoints
FROM PlayerStats ps
INNER JOIN Players p
ON ps.PlayerName = p.PlayerName
WHERE p.Country = 'New Zealand'
GROUP BY p.PlayerName, p.Country
