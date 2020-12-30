'''
Creating a view from other views


Views can be created from queries that include other views. This is useful when you have a complex schema, potentially due to normalization, because it helps reduce the JOINS needed. The biggest concern is keeping track of dependencies, specifically how any modifying or dropping of a view may affect other views.

In the next few exercises, we'll continue using the Pitchfork reviews data. There are two views of interest in this exercise. top_15_2017 holds the top 15 highest scored reviews published in 2017 with columns reviewid,title, and score. artist_title returns a list of all reviewed titles and their respective artists with columns reviewid, title, and artist. From these views, we want to create a new view that gets the highest scoring artists of 2017.

Instructions 1/2
50 XP

- Create a view called top_artists_2017 with one column artist holding the top artists in 2017.
- Join the views top_15_2017 and artist_title.
-Output top_artists_2017.

'''
-- Create a view with the top artists in 2017
CREATE VIEW top_artists_2017 AS
-- with only one column holding the artist field
SELECT artist_title.artist FROM artist_title
INNER JOIN top_15_2017
ON artist_title.reviewid = top_15_2017.reviewid

-- Output the new view
SELECT * FROM top_artists_2017

'''
Instructions 2/2
50 XP

Question :

Which is the DROP command that would drop both top_15_2017 and top_artists_2017?

Possible Answers

    - DROP VIEW top_15_2017 CASCADE;

    - DROP VIEW top_15_2017 RESTRICT;

    - DROP VIEW top_artists_2017 RESTRICT;

    - DROP VIEW top_artists_2017 CASCADE;

Answer : DROP VIEW top_15_2017 CASCADE;

'''
