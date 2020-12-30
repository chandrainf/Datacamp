'''
Using CAST() and CONVERT()


In this lesson, you learned that your tables could store data with different types than you want. Sometimes you will need to convert these types to the correct ones to perform the operations you want.

The series table has a column named num_ratings that stores integer numbers, but this time it was designed as VARCHAR(5). You want to calculate the average of the num_ratings column, but you think that this column is an integer number.

You prepare the following query:

    SELECT AVG(num_ratings)
    FROM series
    WHERE num_ratings BETWEEN 0 AND 5000

Instructions 1/2
50 XP

- Run the query given above to check there are errors.
Use CAST() to convert the type of num_ratings to integer.

'''
-- Use CAST() to convert the num_ratings column
SELECT AVG(CAST(num_ratings AS INT))
FROM series
-- Use CAST() to convert the num_ratings column
WHERE CAST(num_ratings AS INT) BETWEEN 0 AND 5000

'''
Instructions 2/2
50 XP

- Now, use CONVERT() instead of CAST() to convert the type of the num_ratings column to integer.

'''
-- Use CONVERT() to convert the num_ratings column
SELECT AVG(CONVERT(INT, num_ratings))
FROM series
-- Use CONVERT() to convert the num_ratings column
WHERE CONVERT(INT, num_ratings) BETWEEN 0 AND 5000
