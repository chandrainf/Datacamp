'''
Load into Postgres


In this exercise, you'll write out some data to a PostgreSQL data warehouse. That could be useful when you have a result of some transformations, and you want to use it in an application.

For example, the result of a transformation could have added a column with film recommendations, and you want to use them in your online store.

There's a pandas DataFrame called film_pdf in your workspace.

As a reminder, here's the structure of a connection URI for sqlalchemy:

    postgresql://[user[:password]@][host][:port][/database]

Instructions
100 XP

- Complete the connection URI for to create the database engine. The user and password are repl and password respectively. The host is localhost, and the port is 5432. This time, the database is dwh.
- Finish the call so we use the "store" schema in the database. If the table exists, replace it completely.

'''
# Finish the connection URI
connection_uri = "postgresql://repl:password@localhost:5432/dwh"
db_engine_dwh = sqlalchemy.create_engine(connection_uri)

# Transformation step, join with recommendations data
film_pdf_joined = film_pdf.join(recommendations)

# Finish the .to_sql() call to write to store.film
film_pdf_joined.to_sql("film", db_engine_dwh,
                       schema="store", if_exists="replace")

# Run the query to fetch the data
pd.read_sql("SELECT film_id, recommended_film_ids FROM store.film", db_engine_dwh)
