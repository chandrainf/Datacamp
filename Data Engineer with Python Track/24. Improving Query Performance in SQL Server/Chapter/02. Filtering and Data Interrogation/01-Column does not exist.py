'''
Column does not exist

When using WHERE as a filter condition, it is important to think about the processing order in the query. In this exercise, you want a query that returns NBA players with average total rebounds of 12 or more per game. The following formula calculates average total rebounds from the PlayerStats table;

    Average Total Rebounds = \dfrac{(Defensive Rebounds + Offensive Rebounds)}{Games Played}

The first query in Step 1 returns an error. Select Run Code to view the error. The second query, in Step 2, will give you the results you want, without error, by using a sub-query.

Note that GamesPlayed is CAST AS numeric to ensure we get decimal points in our output, as opposed to whole numbers.

Instructions 1/2
50 XP

- Try to understand what the error is telling you when you run the first query, then comment out the query block on lines 2 and 9.

'''
-- First query
/*
SELECT PlayerName,
Team,
Position,
(DRebound+ORebound)/CAST(GamesPlayed AS numeric) AS AvgRebounds
FROM PlayerStats
WHERE AvgRebounds >= 12
*/


'''
Instructions 2/2
50 XP

- In the sub-query calculate average total rebounds in a new column, AvgRebounds.
- Add the new column to the SELECT statement.
- Apply a filter condition for 12 or more average total rebounds.

'''
-- Second query

-- Add the new column to the select statement
SELECT PlayerName,
Team,
Position,
AvgRebounds - - Add the new column
FROM
-- Sub-query starts here
(SELECT
 PlayerName,
 Team,
 Position,
 -- Calculate average total rebounds
 (ORebound+DRebound)/CAST(GamesPlayed AS numeric) AS AvgRebounds
 FROM PlayerStats) tr
WHERE AvgRebounds >= 12
-- Filter rows
