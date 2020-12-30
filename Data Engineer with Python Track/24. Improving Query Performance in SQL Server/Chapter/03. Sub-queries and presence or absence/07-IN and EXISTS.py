'''
IN and EXISTS


You want to know which, if any, country capitals are listed as the nearest city to recorded earthquakes. You can get this information using INTERSECT and comparing the Nations table with the Earthquakes table. However, INTERSECT requires that the number and order of columns in the SELECT statements must be the same between queries and you would like to include additional columns from the outer query in the results.

You attempt two queries, each with a different operator that gives you the results you require.

Instructions 1/2
50 XP

- Add the 2017 country population and capital city name columns to the outer query.
- Add the operator to compare the outer query with the sub-query.


'''
-- First attempt
SELECT CountryName,
       Pop2017, -- 2017 country population
	   Capital, -- Capital city
       WorldBankRegion
FROM Nations
WHERE Capital IN - - Add the operator to compare queries
        (SELECT NearestPop
	     FROM Earthquakes);


'''
Instructions 2/2
50 XP

- Update the query with the 2016 population instead of the 2017 population.
- Add the operator to compare the outer query with the sub-query.
- Add the two city name columns, being compared, in the sub-query.


'''

-- Second attempt
SELECT CountryName,
	   Capital,
       Pop2016, -- 2016 country population
       WorldBankRegion
FROM Nations AS n
WHERE Exists -- Add the operator to compare queries
	  (SELECT 1
	   FROM Earthquakes AS e
	   WHERE n.Capital = e.NearestPop); -- Columns being compared
