'''
Creating and refreshing a materialized view


The syntax for creating materialized and non-materialized views are quite similar because they are both defined by a query. One key difference is that we can refresh materialized views, while no such concept exists for non-materialized views. It's important to know how to refresh a materialized view, otherwise the view will remain a snapshot of the time the view was created.

In this exercise, you will create a materialized view from the table genres. A new record will then be inserted into genres. To make sure the view has the latest data, it will have to be refreshed.

Instructions
100 XP

-Create a materialized view called genre_count that holds the number of reviews for each genre.
-Refresh genre_count so that the view is up-to-date.

'''
-- Create a materialized view called genre_count
CREATE MATERIALIZED VIEW genre_count AS
SELECT genre, COUNT(*)
FROM genres
GROUP BY genre

INSERT INTO genres
VALUES(50000, 'classical')

-- Refresh genre_count
REFRESH MATERIALIZED VIEW genre_count

SELECT * FROM genre_count
