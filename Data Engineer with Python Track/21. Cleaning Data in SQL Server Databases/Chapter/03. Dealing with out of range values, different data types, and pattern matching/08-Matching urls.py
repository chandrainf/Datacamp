'''
Matching urls


In this lesson you learned that SQL Server provides the LIKE operator, which determines if a string matches a specified pattern.

You need to verify the URLs of the official sites of every series. You prepare a script that checks every official_site value from the series table to analyze possible wrong URLs.

To make it easier, suppose that the format of the URLs you have to validate must start with 'www.', although we know that there are URLs that have other beginnings.

Instructions
100 XP

- Select the URLs of the official sites.
- Get the URLs that don't match the pattern.
- Write the pattern.

'''
SELECT
	name,
    -- URL of the official site
	official_site
FROM series
-- Get the URLs that don't match the pattern
WHERE official_site NOT LIKE
	-- Write the pattern
	'www.%'
