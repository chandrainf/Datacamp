'''
Joining with ratings


In the video exercise, you saw how to use transformations in PySpark by joining the film and ratings tables to create a new column that stores the average rating per customer. In this exercise, you're going to create more synergies between the film and ratings tables by using the same techniques you learned in the video exercise to calculate the average rating for every film.

The PySpark DataFrame with films, film_df and the PySpark DataFrame with ratings, rating_df, are available in your workspace.

Instructions
100 XP

- Take the mean rating per film_id, and assign the result to ratings_per_film_df.
- Complete the .join() statement to join on the film_id column.
- Show the first 5 results of the resulting DataFrame.

'''
# Use groupBy and mean to aggregate the column
ratings_per_film_df = rating_df.groupBy('film_id').mean('rating')

# Join the tables using the film_id column
film_df_with_ratings = film_df.join(
    ratings_per_film_df,
    film_df.film_id == ratings_per_film_df.film_id
)

# Show the 5 first results
print(film_df_with_ratings.show(5))
