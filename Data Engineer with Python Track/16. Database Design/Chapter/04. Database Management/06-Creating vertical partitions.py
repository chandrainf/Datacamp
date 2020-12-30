'''
Creating vertical partitions


In the video, you learned about vertical partitioning and saw an example.

For vertical partitioning, there is no specific syntax in PostgreSQL. You have to create a new table with particular columns and copy the data there. Afterward, you can drop the columns you want in the separate partition. If you need to access the full table, you can do so by using a JOIN clause.

In this exercise and the next one, you'll be working with the example database called pagila. It's a database that is often used to showcase PostgreSQL features. The database contains several tables. We'll be working with the film table. In this exercise, we'll use the following columns:

    - film_id: the unique identifier of the film
    - long_description: a lengthy description of the film

Instructions 1/2
50 XP

-Create a new table film_descriptions containing 2 fields: film_id, which is of type INT, and long_description, which is of type TEXT.
-Occupy the new table with values from the film table.

'''

-- Create a new table called film_descriptions
CREATE TABLE film_descriptions(
    film_id int,
    long_description text
)

-- Copy the descriptions from the film table
INSERT INTO film_descriptions
SELECT film_id, long_description FROM film

'''
Instructions 2/2
50 XP

- Drop the field long_description from the film table.
- Join the two resulting tables to view the original table.
'''

-- Create a new table called film_descriptions
CREATE TABLE film_descriptions(
    film_id INT,
    long_description TEXT
)

-- Copy the descriptions from the film table
INSERT INTO film_descriptions
SELECT film_id, long_description FROM film

-- Drop the descriptions from the original table
ALTER TABLE film DROP COLUMN long_description

-- Join to view the original table
SELECT * FROM film
JOIN film_descriptions USING(film_id)
