'''
Detecting and excluding inaccurate data


In this lesson, you also learned that if you don't detect inaccurate data before analyzing, this data can disrupt your results.

The series table has a boolean column named is_adult, that stores whether the series is for adults or not. There is also another column, min_age, that stores the minimum age the audience should have. Unfortunately, there are contradictory values, because some rows with a TRUE value in its is_adult column have a number smaller than 18 in its min_age column.

Can you find these rows with inaccurate data?

Instructions 1/2
50 XP

- Detect the series with a true value in its is_adult column that have a value smaller than 18 in its min_age column.

'''
SELECT * FROM series
-- Detect series for adults
WHERE is_adult = 1
-- Detect series with the minimum age smaller than 18
AND min_age < 18

'''
Instructions 2/2
50 XP

- Now exclude the series with a true value in its is_adult column that have a value smaller than 18 in its min_age column.

'''
SELECT * FROM series
-- Filter series for adults
WHERE is_adult = 1
-- Exclude series with the minimum age greater or equals to 18
AND min_age >= 18