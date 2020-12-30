'''
Joining on relations

You've used the following diagram in the previous exercise:

Database Schema for Customer and Order

You've learned that you can use the read_sql() function from pandas to query the database. The real power of SQL is the ability to join information from multiple tables quickly. You do this by using the JOIN statement.

When joining two or more tables, pandas puts all the columns of the query result into a DataFrame.

Instructions
100 XP

- Complete the SELECT statement, so it joins the "Customer" with the "Order" table.
Print the id column of data. What do you see?


'''

# Complete the SELECT statement
data = pd.read_sql("""
SELECT * FROM "Customer"
INNER JOIN "Order"
ON "Order"."customer_id"="Customer"."id"
""", db_engine)

# Show the id column of data
print(data.id)
