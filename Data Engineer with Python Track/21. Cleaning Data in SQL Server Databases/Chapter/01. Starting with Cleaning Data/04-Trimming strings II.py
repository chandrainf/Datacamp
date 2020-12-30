'''
Trimming strings II


In the previous exercise, you used TRIM() to remove the leading and trailing spaces for the values of the airport_name column.

Suppose that the TRIM() function is not available because you are using an older version of SQL Server 2017, so you this time you need to use LTRIM() and RTRIM().

How can you remove these extra spaces?

Instructions
100 XP

- Use the appropriate functions to remove the leading and trailing spaces.
- Select the source table where the data is.

'''
SELECT
	airport_code,
	-- Use the appropriate function to remove the extra spaces
    RTRIM(LTRIM(airport_name)) AS airport_name,
	airport_city,
    airport_state   
-- Select the source table
FROM airports
