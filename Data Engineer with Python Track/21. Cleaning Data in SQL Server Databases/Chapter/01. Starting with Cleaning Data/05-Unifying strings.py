'''
Unifying strings


Sometimes it's common to find messy strings when having different values for the same thing. Although all of these values can be valid, it is better to unify them to perform better analysis.

You run this query to filter all the airports located in the city of 'Chicago':

	SELECT * FROM airports
	WHERE airport_code IN ('ORD', 'MDW')

In the results, you see that there are inconsistent values for 'Chicago' in the airport_city column, with values such as 'ch'. You will treat these inconsistent values by replacing them.

Instructions 1/3
35 XP

- Replace 'ch' with 'Chicago' - notice how 'Chicago' became 'Chicagoicago'.

'''

SELECT
	airport_code,
	airport_name,
    -- Use the appropriate function to unify the values
    REPLACE(airport_city, 'ch', 'Chicago') AS airport_city,
	airport_state
FROM airports  
WHERE airport_code IN ('ORD', 'MDW')


'''
Instructions 2/3
35 XP

Use CASE to replace 'ch' with 'Chicago' in all the rows that are not 'Chicago'.
Do not change airport_city otherwise.

'''
SELECT airport_code, airport_name, 
	-- Use the CASE statement
	CASE
        -- Unify the values
		WHEN airport_city <> 'Chicago' THEN REPLACE(airport_city, 'ch', 'Chicago')
		ELSE airport_city 
	END AS airport_city,
    airport_state
FROM airports
WHERE airport_code IN ('ORD', 'MDW')



'''
Instructions 3/3
30 XP

- Unify 'Chicago' and 'ch' to 'CH' by replacing 'Chicago' with 'ch' and converting the output to upper case.

'''
SELECT 
	airport_code, airport_name,
    	-- Convert to uppercase
    	UPPER(
            -- Replace 'Chicago' with 'ch'.
          	REPLACE(airport_city, 'Chicago', 'ch')
        ) AS airport_city,
    airport_state
FROM airports
WHERE airport_code IN ('ORD', 'MDW')
