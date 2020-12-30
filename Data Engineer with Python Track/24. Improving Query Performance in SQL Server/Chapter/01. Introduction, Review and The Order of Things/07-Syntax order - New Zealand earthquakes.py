'''
Syntax order - New Zealand earthquakes


When executing a query, the processing order of the main SQL syntax is different from the written order in the query.

You want a simple query that returns all the recorded earthquakes in New Zealand that had a magnitude of 7.5 or higher. You think the query out in a sentence before creating it.

From the Earthquakes table, filter for only rows where Country equals 'NZ' and Magnitude greater than or equal to 7.5. Then, select the columns Date, Place, NearestPop, and Magnitude. Order the final results from the largest Magnitude to the smallest Magnitude.

The sample code is arranged in the order that matches the above sentence, which is the same as the SQL syntax processing order in the database. You will need to reorder it so that it runs without error.

Instructions
100 XP

- Complete the required query using FROM, WHERE, SELECT and ORDER BY.
- Rearrange the query so that the syntax is in the order that it will run without error.

'''
/*
Returns earthquakes in New Zealand with a magnitude of 7.5 or more
*/

SELECT Date, Place, NearestPop, Magnitude
FROM Earthquakes
WHERE Country = 'NZ' AND Magnitude >= 7.5
ORDER BY Magnitude DESC
