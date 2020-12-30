'''
Using broadcasting on Spark joins


Remember that table joins in Spark are split between the cluster workers. If the data is not local, various shuffle operations are required and can have a negative impact on performance. Instead, we're going to use Spark's broadcast operations to give each node a copy of the specified data.

A couple tips:

Broadcast the smaller DataFrame. The larger the DataFrame, the more time required to transfer to the worker nodes.
On small DataFrames, it may be better skip broadcasting and let Spark figure out any optimization on its own.
If you look at the query execution plan, a broadcastHashJoin indicates you've successfully configured broadcasting.
The DataFrames flights_df and airports_df are available to you.

Instructions
100 XP

- Import the broadcast() method from pyspark.sql.functions.
- Create a new DataFrame broadcast_df by joining flights_df with airports_df, using the broadcasting.
- Show the query plan and consider differences from the original.

'''
# Import the broadcast method from pyspark.sql.functions
from pyspark.sql.functions import broadcast

# Join the flights_df and airports_df DataFrames using broadcasting
broadcast_df = flights_df.join(broadcast(airports_df),
                               flights_df["Destination Airport"] == airports_df["IATA"])

# Show the query plan and compare against the original
broadcast_df.explain()
