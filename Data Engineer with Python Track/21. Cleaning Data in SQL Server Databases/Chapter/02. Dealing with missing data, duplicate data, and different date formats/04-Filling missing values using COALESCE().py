'''
Filling missing values using COALESCE()


In the previous exercise, you used the ISNULL() function to replace the NULL values of a column with another value.

Now, you want to create a new column, location, that returns the values of the airport_city column, and in case it has NULL values, return the value of airport_state. Finally, if airport_state is also NULL, you want to return the string 'Unknown'.

To do it, you can use COALESCE(), that evaluates the arguments between parenthesis and returns the first argument that is not NULL.

Instructions
100 XP

- Use COALESCE() to return the first non NULL value of airport_city, airport_state, or 'Unknown'.

'''
SELECT
airport_code,
airport_name,
-- Replace the missing values
COALESCE(airport_city, airport_state, 'Unknown') AS location
FROM airports