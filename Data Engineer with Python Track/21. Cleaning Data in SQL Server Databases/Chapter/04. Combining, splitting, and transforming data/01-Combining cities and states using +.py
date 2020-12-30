'''
Combining cities and states using +


In this lesson, you learned how to combine columns into one.

The clients table has one column, city, to store the cities where the clients live, and another column, state, to store the state of the city.

	| client_id | client_name | client_surname | city      | state    |
	|-----------|-------------|----------------|-----------|----------|
	| 1         | Miriam      | Antona         | Las Vegas | Nevada   |
	| 2         | Astrid      | Harper         | Chicago   | Illinois |
	| 3         | David       | Madden         | Phoenix   | Arizona  |
	| ...       | ...         | ...            | ...       | ...      |

You need to combine city and state columns into one, to have the following format: 'Las Vegas, Nevada'.

You will use + operator to do it.

Instructions 1/2
50 XP

- Concatenate the names of the cities with the states using the + operator without worrying about NULL values.

'''
SELECT
	client_name,
	client_surname,
    -- Concatenate city with state
	city + ', ' + state AS city_state
FROM clients


'''
Instructions 2/2
50 XP

- Replace each instance of NULL in city and state with an ISNULL() function, so that if either column has a NULL value, an empty string '' is returned instead.

'''
SELECT 
	client_name,
	client_surname,
    -- Consider the NULL values
	ISNULL(city, '') + ISNULL(', ' + state, '') AS city_state
FROM clients

