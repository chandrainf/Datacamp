'''
Querying the star schema


The novel genre hasn't been selling as well as your company predicted. To help remedy this, you've been tasked to run some analytics on the novel genre to find which areas the Sales team should target. To begin, you want to look at the total amount of sales made in each state from books in the novel genre.

Luckily, you've just finished setting up a data warehouse with the following star schema:



The tables from this schema have been loaded.

Instructions
100 XP

- Select state from the appropriate table and the total sales_amount.
- Complete the JOIN on book_id.
- Complete the JOIN to connect the dim_store_star table
- Conditionally select for books with the genre novel.
- Group the results by state.

'''
-- Output each state and their total sales_amount
SELECT dim_store_star.state, sum(sales_amount)
FROM fact_booksales
	-- Join to get book information
    JOIN dim_book_star on fact_booksales.book_id = dim_book_star.book_id
	-- Join to get store information
    JOIN dim_store_star on fact_booksales.store_id = dim_store_star.store_id
 -- Get all books with in the novel genre
WHERE  
    dim_book_star.genre = 'novel'
-- Group results by state
GROUP BY
    dim_store_star.state;
