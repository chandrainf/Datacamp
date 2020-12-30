'''
Detecting out of range values


Sometimes you can find out of range values in your data. If you don't detect them before analyzing, they can disrupt your results.

The logical operator BETWEEN, and the comparison operators > and <, can help you to detect the rows with out of range values.

The num_ratings column of the series table stores the number of ratings each series has received. The total amount of people surveyed is 5000. However, this column has some out of range values, i.e., there are values greater than 5000 or smaller than 0.

Try to find them!

Instructions 1/2
50 XP

-Find rows in series where num_ratings is not between 0 and 5000.

'''
SELECT * FROM series
-- Detect the out of range values
WHERE num_ratings NOT BETWEEN 0 AND 5000

'''
Instructions 2/2
50 XP

Similarly, use < and > to detect the rows from the series table where num_ratings is not between 0 and 5000.

'''
SELECT * FROM series
-- Detect the out of range values
WHERE num_ratings < 0 OR num_ratings > 5000