'''
Adding foreign keys


Foreign key references are essential to both the snowflake and star schema. When creating either of these schemas, correctly setting up the foreign keys is vital because they connect dimensions to the fact table. They also enforce a one-to-many relationship, because unless otherwise specified, a foreign key can appear more than once in a table and primary key can appear only once.

The fact_booksales table has three foreign keys: book_id, time_id, and store_id. In this exercise, the four tables that make up the star schema below have been loaded. However, the foreign keys still need to be added. 

Instructions
100 XP

- In the constraint called sales_book, set book_id as a foreign key.
- In the constraint called sales_time, set time_id as a foreign key.
- In the constraint called sales_store, set store_id as a foreign key.

'''
-- Add the book_id foreign key
-- Add the book_id foreign key
ALTER TABLE fact_booksales ADD CONSTRAINT sales_book
FOREIGN KEY(book_id) REFERENCES dim_book_star(book_id)

-- Add the time_id foreign key
ALTER TABLE fact_booksales ADD CONSTRAINT sales_time
FOREIGN KEY(time_id) REFERENCES dim_time_star(time_id)

-- Add the store_id foreign key
ALTER TABLE fact_booksales ADD CONSTRAINT sales_store
FOREIGN KEY(store_id) REFERENCES dim_store_star(store_id)
