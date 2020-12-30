'''
Syntax order - very large earthquakes


When a query is executed it will stop at the first error it encounters and will return an error message. Because a query is processed in a stepped order the first error it stops at will be related to the processing order.

FROM is processed first and checks that the queried table(s) exist in the database.
WHERE is always processed after FROM if a row filtering condition is specified. Column(s) having the filtering condition applied must exist.
SELECT is only processed once the data is ready to be extracted and displayed or returned to the user.
This exercise has three queries—each contains errors. Your job is to find the errors and fix them.

Note that the red text below the query result tab is a description of the error.

Instructions 1/3
35 XP

Select Run Code and look at the error produced. Fix the error and select Submit Answer.

'''
/*
Returns the location of the epicenter of earthquakes with a 9 + magnitude
*/

-- Replace Countries with the correct table name
SELECT n.CountryName AS Country
	, e.NearestPop AS ClosestCity
    ,e.Date
    ,e.Magnitude
FROM Nations AS n
INNER JOIN Earthquakes AS e
	ON n.Code2 = e.Country
WHERE e.Magnitude >= 9
ORDER BY e.Magnitude DESC;







'''
Instructions 2/3
35 XP

Select Run Code and look at the error produced. Fix the error and select Submit Answer.

/*
Returns the location of the epicenter of earthquakes with a 9+ magnitude
*/

'''
-- Replace Magnatud with the correct column name
SELECT n.CountryName AS Country
	,e.NearestPop AS ClosestCity
    ,e.Date
    ,e.Magnitude
FROM Nations AS n
INNER JOIN Earthquakes AS e
	ON n.Code2 = e.Country
WHERE e.Magnitude >= 9
ORDER BY e.Magnitude DESC;









'''
Instructions 3/3
30 XP

Select Run Code and look at the error produced. Fix the error and select Submit Answer.

'''

/*
Location of the epicenter of earthquakes with a 9+ magnitude
*/

-- Replace City with the correct column name
SELECT n.CountryName AS Country
	,e.NearestPop AS ClosestCity
    ,e.Date
    ,e.Magnitude
FROM Nations AS n
INNER JOIN Earthquakes AS e
	ON n.Code2 = e.Country
WHERE e.Magnitude >= 9
ORDER BY e.Magnitude DESC;

