'''
Extending the snowflake schema


The company is thinking about extending their business beyond bookstores in Canada and the US. Particularly, they want to expand to a new continent. In preparation, you decide a continent field is needed when storing the addresses of stores.

Luckily, you have a snowflake schema in this scenario. As we discussed in the video, the snowflake schema is typically faster to extend while ensuring data consistency. Along with dim_country_sf, a table called dim_continent_sf has been loaded. It contains the only continent currently needed, North America, and a primary key. In this exercise, you'll need to extend dim_country_sf to reference dim_continent_sf.

Instructions
100 XP

- Add a continent_id column to dim_country_sf with a default value of 1. Note thatNOT NULL DEFAULT(1) constrains a value from being null and defaults its value to 1.
- Make that new column a foreign key reference to dim_continent_sf's continent_id.

'''
-- Add a continent_id column with default value of 1
ALTER TABLE dim_country_sf
ADD continent_id int NOT NULL DEFAULT(1);

 -- Add the foreign key constraint
ALTER TABLE dim_country_sf ADD CONSTRAINT country_continent
   FOREIGN KEY(continent_id) REFERENCES dim_continent_sf(continent_id);

 -- Output updated table
SELECT * FROM dim_country_sf;
