'''
Concatenating cities and states


In the previous exercise, you used the + operator to combine two columns into one. This time you need to do the same, but using the CONCAT() function.

To get this format for the concatenation: 'Las Vegas, Nevada', you will need to use the CASE expression in case the state column has NULL values.

Instructions
100 XP

- Concatenate the names of the cities with the states using the CONCAT() function, while using a CASE statement that returns '' when state is NULL and performs a normal concatenation otherwise.

'''

SELECT
		client_name,
		client_surname,
    -- Use the function to concatenate the city and the state
		CONCAT(
				city,
				CASE WHEN state IS NULL THEN '' 
				ELSE CONCAT(', ', state) END) AS city_state
FROM clients
