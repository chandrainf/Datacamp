'''
Checking phone numbers


As you learned in this lesson, the underscore _ symbol matches any single character.

You want to prepare a script that checks every contact_number value from the series table to get those numbers that don't start with three fives followed by a hyphen as such 555-, then three characters followed by another hyphen and finally, another four characters (555-###-####).

Can you find them?

Instructions
100 XP

- Select the contact number.
- Get the numbers of contacts that don't match the pattern.
- Write the pattern that the numbers have to match.

'''
SELECT 
	name, 
    -- Contact number
    contact_number
FROM series
-- Get the numbers that don't match the pattern
WHERE contact_number NOT LIKE 
	-- Write the pattern
	'555-___-____'