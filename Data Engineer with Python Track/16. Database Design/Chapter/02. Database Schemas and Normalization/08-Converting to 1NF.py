'''
Converting to 1NF


In the next three exercises, you'll be working through different tables belonging to a car rental company. Your job is to explore different schemas and gradually increase the normalization of these schemas through the different normal forms. At this stage, we're not worried about relocating the data, but rearranging the tables.

A table called customers has been loaded, which holds information about customers and the cars they have rented.

Instructions 1/2
50 XP
Question
Does the customers table meet 1NF criteria?

Possible Answers

    - Yes, all the records are unique.

    - No, because there are multiple values in cars_rented and invoice_id

    - No, because the non-key columns such as don't depend on customer_id, the primary key.

Answer : No, because there are multiple values in cars_rented and invoice_id

'''

'''
Instructions 2/2
50 XP

- cars_rented holds one or more car_ids and invoice_id holds multiple values. Create a new table to hold individual car_ids and invoice_ids of the customer_ids who've rented those cars.
- Drop two columns from customers table to satisfy 1NF

'''
-- Create a new table to hold the cars rented by customers
CREATE TABLE cust_rentals(
    customer_id INT NOT NULL,
    car_id VARCHAR(128) NULL,
    invoice_id VARCHAR(128) NULL
)

-- Drop column from customers table to satisfy 1NF
ALTER TABLE customers
DROP COLUMN cars_rented,
DROP COLUMN invoice_id
