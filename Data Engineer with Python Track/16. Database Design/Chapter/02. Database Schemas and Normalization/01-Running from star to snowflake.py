'''
Running from star to snowflake


Remember your running database from last chapter? 

After learning about the snowflake schema, you convert the current star schema into a snowflake schema. To do this, you normalize route_dim and week_dim. Which option best describes the resulting new tables after doing this?

The tables runs_fact, route_dim, and week_dim have been loaded.

Instructions
50 XP

Possible Answers

    - week_dim is extended two dimensions with new tables for month and year. route_dim is extended one dimension with a new table for city.

    - week_dim is extended two dimensions with new tables for month and year. route_dim is extended two dimensions with new tables for city and park.

    - week_dim is extended three dimensions with new tables for week, month and year. route_dim is extended one dimension with new tables for city and park.

Answer : week_dim is extended two dimensions with new tables for month and year. route_dim is extended two dimensions with new tables for city and park.

'''
