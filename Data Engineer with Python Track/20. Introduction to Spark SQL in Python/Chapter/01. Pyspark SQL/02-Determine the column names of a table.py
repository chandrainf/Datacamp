'''
Determine the column names of a table


The video lesson showed how to run an SQL query. It also showed how to inspect the column names of a Spark table using SQL. This is important to know because in practice relational tables are typically provided without additional documentation giving the table schema.

Don't hesitate to refer to the slides available at the right of the console if you forget how something was done in the video.

Instructions
100 XP

- Use a DESCRIBE query to determine the names and types of the columns in the table schedule.

'''
# Inspect the columns in the table df
spark.sql("DESCRIBE schedule").show()
