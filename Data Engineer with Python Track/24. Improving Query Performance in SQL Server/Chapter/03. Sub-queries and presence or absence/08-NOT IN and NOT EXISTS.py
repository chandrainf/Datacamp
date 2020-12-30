'''
NOT IN and NOT EXISTS


NOT IN and NOT EXISTS do the opposite of IN and EXISTS respectively. They are used to check if the data present in one table is absent in another.

You are interested to know if there are some countries in the Nations table that do not appear in the Cities table. There may be many reasons for this. For example, all the city populations from a country may be too small to be listed, or there may be no city data for a particular country at the time the data was compiled.

You will compare the queries using country codes.

Instructions 1/2
50 XP

- Add the operator to compare the outer query with the sub-query.
- Add the country code column to the sub-query.

'''

SELECT WorldBankRegion,
   CountryName
FROM Nations
WHERE Code2 NOT IN - - Add the operator to compare queries
    (SELECT CountryCode - - Country code column
     FROM Cities);


'''
Instructions 2/2
50 XP

- Add the country capital column to the outer query.
- Add the operator to compare the outer query with the sub-query.
- Add the two country code columns being compared in the sub-query.

'''

SELECT WorldBankRegion,
   CountryName,
       Code2,
    Capital, -- Country capital column
       Pop2017
FROM Nations AS n
WHERE NOT EXISTS - - Add the operator to compare queries
   (SELECT 1
     FROM Cities AS c
     WHERE n.Code2 = c.CountryCode)
    -- Columns being compared
