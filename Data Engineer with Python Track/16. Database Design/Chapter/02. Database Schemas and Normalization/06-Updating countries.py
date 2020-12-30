'''
Updating countries


Going through the company data, you notice there are some inconsistencies in the store addresses. These probably occurred during data entry, where people fill in fields using different naming conventions. This can be especially seen in the country field, and you decide that countries should be represented by their abbreviations. The only countries in the database are Canada and the United States, which should be represented as USA and CA.

In this exercise, you will compare the records that need to be updated in order to do this task on the star and snowflake schema. dim_store_star and dim_country_sf have been loaded.

Instructions 1/2
50 XP

- Output all the records that need to be updated in the star schema so that countries are represented by their abbreviations.

'''
-- Output records that need to be updated in the star schema
SELECT * FROM dim_store_star
WHERE country != 'USA' AND country != 'CA'


'''
Instructions 2/2
50 XP

Question

How many records would need to be updated in the snowflake schema?

Possible Answers

    - 18 records

    - 2 records

    - 1 record

    - 0 records

Answer : 1 record

'''
