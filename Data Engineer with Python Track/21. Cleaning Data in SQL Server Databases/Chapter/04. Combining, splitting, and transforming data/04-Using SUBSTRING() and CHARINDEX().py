'''
Using SUBSTRING() and CHARINDEX()


In this lesson, you learned how to split one column into more columns.

The clients_split table has one column, city_state, that stores the cities where the clients live and the state of the city. The values of this column have this appearance: 'Chicago, Illinois'.

You need to split this column into two new columns, one for the city and the other one for the state. You think about using SUBSTRING() in combination with CHARINDEX() and LEN().

Instructions
100 XP

- Extract the name of the city using SUBSTRING() and CHARINDEX().
- Extract the name of the state using SUBSTRING(), CHARINDEX() and LEN().

'''
SELECT
	client_name,
	client_surname,
    -- Extract the name of the city
	SUBSTRING(city_state, 1, CHARINDEX(', ', city_state) - 1) AS city,
    -- Extract the name of the state
    SUBSTRING(city_state, CHARINDEX(', ', city_state) + 1, LEN(city_state)) AS state
FROM clients_split
