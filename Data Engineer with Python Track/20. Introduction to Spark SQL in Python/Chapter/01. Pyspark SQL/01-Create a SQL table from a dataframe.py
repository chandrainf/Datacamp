'''
Create a SQL table from a dataframe


A dataframe can be used to create a temporary table. A temporary table is one that will not exist after the session ends. Spark documentation also refers to this type of table as a SQL temporary view. In the documentation this is referred to as to register the dataframe as a SQL temporary view. This command is called on the dataframe itself, and creates a table if it does not already exist, replacing it with the current data from the dataframe if it does already exist.

Instructions
100 XP

- Load csv data from the file trainsched.txt into a dataframe stored in a variable named df.
- Create a temporary table from df. Call the table "table1".

'''
# Load trainsched.txt
df = spark.read.csv("trainsched.txt", header=True)

# Create temporary table called table1
df.createOrReplaceTempView('table1')
