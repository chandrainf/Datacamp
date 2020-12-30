'''
Trimming strings I


Messy strings can be a problem because sometimes, it is not easy to analyze them without cleaning them.

When analyzing the airports table, you realize that some values of the airport_name column are messy strings. These strings have leading and trailing spaces.

The TRIM() function can help you to remove these additional spaces for the airports table.

Instructions
100 XP

- Examine the content of the airports table to see the leading and trailing spaces.
- Use the appropriate function to remove the leading and trailing spaces.
- Select the source table where the data is.

'''
SELECT
	airport_code,
	-- Use the appropriate function to remove the extra spaces
    TRIM(airport_name) AS airport_name,
	airport_city,
    airport_state   
-- Select the source table
FROM airports
