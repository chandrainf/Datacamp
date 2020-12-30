'''
Excluding out of range values


In the previous exercise, you detected the rows with a number of ratings that were out of range.

The logical operator BETWEEN, and the comparison operators >, <, and =, can help you to exclude the rows with out of range values.

This time, you want to get all the rows from the series table, ranging from 0 to 5000.

Instructions 1/2
50 XP

- Use BETWEEN to detect all the rows from the series table where num_ratings is a value ranging from 0 to 5000.

'''
SELECT * FROM series
-- Exclude the out of range values
WHERE num_ratings BETWEEN 0 AND 5000



'''
Instructions 2/2
50 XP

- Similarly, use <, >, and = to detect the rows from the series table where num_ratings is between 0 and 5000.

'''
SELECT * FROM series
-- Exclude the out of range values
WHERE num_ratings >= 0 AND num_ratings <= 5000

'''
