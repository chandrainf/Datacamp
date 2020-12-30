'''
Uncorrelated sub-query


A sub-query is another query within a query. The sub-query returns its results to an outer query to be processed.

You want a query that returns the region and countries that have experienced earthquakes centered at a depth of 400km or deeper. Your query will use the Earthquakes table in the sub-query, and Nations table in the outer query.

Instructions 1/2
50 XP

- Add the country code column to the outer query.
- Add the country code column to the sub-query.
- Filter for a depth of 400km or more.

'''

SELECT UNStatisticalRegion,
CountryName
FROM Nations
WHERE Code2 - - Country code for outer query
IN(SELECT Country - - Country code for sub-query
    FROM Earthquakes
    WHERE depth >= 400) - - Depth filter
ORDER BY UNStatisticalRegion


'''
Instructions 2/2
50 XP

Question

Why is the query from Step 1 an example of an uncorrelated sub-query?

Possible Answers

    -The sub-query does not reference the outer query.

    -The sub-query cannot be run independently of the outer query.

    -The outer query is referenced in the sub-query.

    -The sub-query is used as a WHERE filter condition for the outer query. Only uncorrelated sub-queries can be used like this.

Answer : The sub-query does not reference the outer query.

'''
