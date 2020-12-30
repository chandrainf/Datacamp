'''
Converting to 2NF


Let's try normalizing a bit more. In the last exercise, you created a table holding customer_ids and car_ids. This has been expanded upon and the resulting table, customer_rentals, has been loaded for you. Since you've got 1NF down, it's time for 2NF.

Instructions 1/2
50 XP

Question :

Why doesn't customer_rentals meet 2NF criteria?

Possible Answers

    - Because the end_date doesn't depend on all the primary keys.

    - Because there can only be at most two primary keys.

    - Because there are non-key attributes describing the car that only depend on one primary key, car_id.

Answer : Because there are non-key attributes describing the car that only depend on one primary key, car_id.

'''


'''
Instructions 2/2
50 XP

- Create a new table for the non-key columns that were conflicting with 2NF criteria.
- Drop those non-key columns from customer_rentals.
'''

CREATE TABLE cars(
    car_id VARCHAR(256) NULL,
    model VARCHAR(128),
    manufacturer VARCHAR(128),
    type_car VARCHAR(128),
    condition VARCHAR(128),
    color VARCHAR(128)
)

-- Drop columns in customer_rentals to satisfy 2NF
ALTER TABLE customer_rentals
DROP COLUMN model,
DROP COLUMN manufacturer,
DROP COLUMN type_car,
DROP COLUMN condition,
DROP COLUMN color
