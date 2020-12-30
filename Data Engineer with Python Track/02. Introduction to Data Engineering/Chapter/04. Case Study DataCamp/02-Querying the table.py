'''
Querying the table


Now that you have a grasp of what's happening in the datacamp_application database, let's go ahead and write up a query for that database.

The goal is to get a feeling for the data in this exercise. You'll get the rating data for three sample users and then use a predefined helper function, print_user_comparison(), to compare the sets of course ids these users rated.

Instructions
100 XP

- Complete the connection URI. The database is called datacamp_application. The host is localhost with port 5432. The username is repl and password is password.
- Select the ratings of users with id: 4387, 18163 and 8770.
- Fill in print_user_comparison() with the three users you selected.

'''
# Complete the connection URI
connection_uri = "postgresql://repl:password@localhost:5432/datacamp_application"
db_engine = sqlalchemy.create_engine(connection_uri)

# Get user with id 4387
user1 = pd.read_sql("SELECT * FROM rating WHERE user_id=4387", db_engine)

# Get user with id 18163
user2 = pd.read_sql("SELECT * FROM rating WHERE user_id=18163", db_engine)

# Get user with id 8770
user3 = pd.read_sql("SELECT * FROM rating WHERE user_id=8770", db_engine)

# Use the helper function to compare the 3 users
print_user_comparison(user1, user2, user3)
