'''
Querying the snowflake schema


Imagine that you didn't have the data warehouse set up. Instead, you'll have to run this query on the company's operational database, which means you'll have to rewrite the previous query with the following snowflake schema:



The tables in this schema have been loaded. Remember, our goal is to find the amount of money made from the novel genre in each state.

Instructions
100 XP

- Select state from the appropriate table and the total sales_amount.
- Complete the two JOINS to get the genre_id's.
- Complete the three JOINS to get the state_id's.
- Conditionally select for books with the genre novel.
- Group the results by state.

'''
-- Output each state and their total sales_amount
SELECT dim_state_sf.state, SUM(sales_amount)
FROM fact_booksales

     -- Joins for the genre
    JOIN dim_book_sf on fact_booksales.book_id = dim_book_sf.book_id
    JOIN dim_genre_sf on dim_book_sf.genre_id = dim_genre_sf.genre_id
    
     -- Joins for the state 
    JOIN dim_store_sf on fact_booksales.store_id = dim_store_sf.store_id 
    JOIN dim_city_sf on dim_store_sf.city_id = dim_city_sf.city_id
	JOIN dim_state_sf on  dim_city_sf.state_id = dim_state_sf.state_id
    
 -- Get all books with in the novel genre and group the results by state
WHERE  
    dim_genre_sf.genre = 'novel'
    
GROUP BY
   dim_state_sf.state;
