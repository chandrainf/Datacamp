'''
The target table


In the previous exercises, you've calculated a DataFrame called recommendations. It contains pairs of user_id's' and course_id's, with a rating that represents the average rating of this course. The assumption is the highest rated course, which is eligible for a user would be best to recommend.

It's time to put this table into a database so that it can be used by several products like a recommendation engine or an emailing system.

Since it's a pandas.DataFrame object, you can use the .to_sql() method. Of course, you'll have to connect to the database using the connection URI first. The recommendations table is available in your environment.

Instructions
100 XP

- Fill in the connection URI for the Postgres database on host localhost with port 5432. You can connect with user repl and password password. The database name is dwh.
- Complete the load_to_dwh() function. It should write to the "recommendations" table and replace if the table exists.

'''

# script.py
connection_uri = "postgresql://repl:password@localhost:5432/dwh"
db_engine = sqlalchemy.create_engine(connection_uri)


def load_to_dwh(recommendations):
    recommendations.to_sql("recommendations", db_engine, if_exists="replace")
