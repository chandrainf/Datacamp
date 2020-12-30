'''
Redefining a view


Unlike inserting and updating, redefining a view doesn't mean modifying the actual data a view holds. Rather, it means modifying the underlying query that makes the view. In the last video, we learned of two ways to redefine a view: (1) CREATE OR REPLACE and (2) DROP then CREATE. CREATE OR REPLACE can only be used under certain conditions.

The artist_title view needs to be appended to include a column for the label field from the labels table.

Instructions 1/2
50 XP

Question :

Can the CREATE OR REPLACE statement be used to redefine the artist_title view?

Possible Answers

    - Yes, as long as the label column comes at the end.

    - No, because the new query requires a JOIN with the labels table.

    - No, because a new column that did not exist previously is being added to the view.

    - Yes, as long as the label column has the same data type as the other columns in artist_title

Answer : Yes, as long as the label column comes at the end.

'''
