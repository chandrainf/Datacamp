'''
Extending the book dimension


In the video, we saw how the book dimension differed between the star and snowflake schema. The star schema's dimension table for books, dim_book_star, has been loaded and below is the snowflake schema of the book dimension. 

In this exercise, you are going to extend the star schema to meet part of the snowflake schema's criteria. Specifically, you will create dim_author from the data provided in dim_book_star.

Instructions 1/2
50 XP

- Create dim_author with a column for author.
- Insert all the distinct authors from dim_book_star into dim_author.

'''
-- Create a new table for dim_author with an author column
CREATE TABLE dim_author(
    author varchar(256)  NOT NULL
)

-- Insert authors
INSERT INTO dim_author
SELECT DISTINCT author FROM dim_book_star

'''
Instructions 2/2
50 XP

Alter dim_author to have a primary key called author_id.
Output all the columns of dim_author.

'''
-- Create a new table for dim_author with an author column
CREATE TABLE dim_author(
    author varchar(256)  NOT NULL
)

-- Insert authors
INSERT INTO dim_author
SELECT DISTINCT author FROM dim_book_star

-- Add a primary key
ALTER TABLE dim_author ADD COLUMN author_id SERIAL PRIMARY KEY

-- Output the new table
SELECT * FROM dim_author
