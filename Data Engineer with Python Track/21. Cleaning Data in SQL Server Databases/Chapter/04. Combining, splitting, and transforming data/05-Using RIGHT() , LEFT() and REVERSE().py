'''
Using RIGHT() , LEFT() and REVERSE()


In the previous exercise, you used SUBSTRING() and CHARINDEX() to split the city_state column into two new columns.

This time you need to do the same, but using the LEFT(), RIGHT(), and REVERSE() functions.

Instructions
100 XP

- Extract the name of the city using LEFT() and CHARINDEX().
- Extract the name of the state using RIGHT(), CHARINDEX() and REVERSE().

'''

SELECT
	client_name,
	client_surname,
    -- Extract the name of the city
	LEFT(city_state, CHARINDEX(', ', city_state) - 1) AS city,
    -- Extract the name of the state
    RIGHT(city_state, CHARINDEX(' ,', REVERSE(city_state)) - 1) AS state
FROM clients_split
