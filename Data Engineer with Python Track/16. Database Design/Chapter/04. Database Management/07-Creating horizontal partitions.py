'''
Creating horizontal partitions


In the video, you also learned about horizontal partitioning.

The example of horizontal partitioning showed the syntax necessary to create horizontal partitions in PostgreSQL. If you need a reminder, you can have a look at the slides.

In this exercise, however, you'll be using a list partition instead of a range partition. For list partitions, you form partitions by checking whether the partition key is in a list of values or not.

To do this, we partition by LIST instead of RANGE. When creating the partitions, you should check if the values are IN a list of values.

We'll be using the following columns in this exercise:

    film_id: the unique identifier of the film
    title: the title of the film
    release_year: the year it's released

Instructions 1/3
35 XP

- Create the table film_partitioned, partitioned on the field release_year.

'''

-- Create a new table called film_partitioned
CREATE TABLE film_partitioned(
    film_id INT,
    title TEXT NOT NULL,
    release_year TEXT
)
PARTITION BY LIST(release_year)


'''
Instructions 2/3
35 XP

- Create three partitions: one for each release year: 2017, 2018, and 2019. Call the partition for 2019 film_2019, etc.

'''
-- Create a new table called film_partitioned
CREATE TABLE film_partitioned(
    film_id INT,
    title TEXT NOT NULL,
    release_year TEXT
)
PARTITION BY LIST(release_year)

-- Create the partitions for 2019, 2018, and 2017
CREATE TABLE film_2019
PARTITION OF film_partitioned FOR VALUES IN('2019')

CREATE TABLE film_2018
PARTITION OF film_partitioned FOR VALUES IN('2018')

CREATE TABLE film_2017
PARTITION OF film_partitioned FOR VALUES IN('2017')

'''
Instructions 3/3
30 XP

Occupy the new table the three fields required from the film table.

'''
-- Create a new table called film_partitioned
CREATE TABLE film_partitioned(
    film_id INT,
    title TEXT NOT NULL,
    release_year TEXT
)
PARTITION BY LIST(release_year)

-- Create the partitions for 2019, 2018, and 2017
CREATE TABLE film_2019
PARTITION OF film_partitioned FOR VALUES IN('2019')

CREATE TABLE film_2018
PARTITION OF film_partitioned FOR VALUES IN('2018')

CREATE TABLE film_2017
PARTITION OF film_partitioned FOR VALUES IN('2017')

-- Insert the data into film_partitioned
INSERT INTO film_partitioned
SELECT film_id, title, release_year FROM film

-- View film_partitioned
SELECT * FROM film_partitioned
