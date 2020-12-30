'''
Correlated sub-query


Sub-queries are used to retrieve information from another table, or query, that is separate to the main query.

A friend is working on a project looking at earthquake hazards around the world. She requires a table that lists all countries, their continent and the average magnitude earthquake by country. This query will need to access data from the Nations and Earthquakes tables.

Instructions 1/2
50 XP

- Add the average magnitude column in the sub-query.
- Add the Nations country code column reference in the sub-query.

'''

SELECT UNContinentRegion,
CountryName,
(SELECT AVG(Magnitude) - - Add average magnitude
 FROM Earthquakes e
 - - Add country code reference
 WHERE n.Code2=e.Country) AS AverageMagnitude
FROM Nations n
ORDER BY UNContinentRegion DESC,
AverageMagnitude DESC


'''
Instructions 2/2
50 XP

Question

Why is the query from Step 1 an example of a correlated sub-query?

Possible Answers

    - The sub-query can be run independently of the outer query.

    - The sub-query does not reference the outer query.

    - The sub-query references the outer query.

    - ORDER BY is used to sort the results by a column in the outer query.

Answer : The sub-query references the outer query.

'''
