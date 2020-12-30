'''
Splitting the rental rate


In the video exercise, you saw how to use pandas to split the email address column of the film table in order to extract the users' domain names. Suppose you would want to have a better understanding of the rates users pay for movies, so you decided to divide the rental_rate column into dollars and cents.

In this exercise, you will use the same techniques used in the video exercises to do just that! The film table has been loaded into the pandas DataFrame film_df. Remember, the goal is to split up the rental_rate column into dollars and cents.

Instructions
100 XP

- Use the .astype() method to convert the rental_rate column into a column of string objects, and assign the results to rental_rate_str.
- Split rental_rate_str on '.' and expand the results into columns. Assign the results to rental_rate_expanded.
- Assign the newly created columns into films_df using the column names rental_rate_dollar and rental_rate_cents respectively.


'''
# Get the rental rate column as a string
rental_rate_str = film_df.rental_rate.astype(str)

# Split up and expand the column
rental_rate_expanded = rental_rate_str.str.split('.', expand=True)

# Assign the columns to film_df
film_df = film_df.assign(
    rental_rate_dollar=rental_rate_expanded[0],
    rental_rate_cents=rental_rate_expanded[1],
)
