'''
Creating and querying a view


Have you ever found yourself running the same query over and over again? Maybe, you used to keep a text copy of the query in your desktop notes app, but that was all before you knew about views!

In these Pitchfork reviews, we're particularly interested in high-scoring reviews and if there's a common thread between the works that get high scores. In this exercise, you'll make a view to help with this analysis so that we don't have to type out the same query often to get these high-scoring reviews.

Instructions 1/2
50 XP

- Create a view called high_scores that holds reviews with scores above a 9.

'''
-- Create a view for reviews with a score above 9
CREATE VIEW high_scores AS
SELECT * FROM REVIEWS
WHERE score > 9


'''
Instructions 2/2
50 XP

-Count the number of records in high_scores that are self-released in the label field of the labels table.

'''
-- Create a view for reviews with a score above 9
CREATE VIEW high_scores AS
SELECT * FROM REVIEWS
WHERE score > 9

-- Count the number of self-released works in high_scores
SELECT COUNT(*) FROM high_scores
INNER JOIN labels ON labels.reviewid = high_scores.reviewid
WHERE label = 'self-released'
