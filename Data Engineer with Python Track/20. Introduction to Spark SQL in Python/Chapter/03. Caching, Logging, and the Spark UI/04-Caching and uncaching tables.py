'''
Caching and uncaching tables


In the lesson we learned that tables can be cached. Whereas a dataframe is cached using a cache or persist operation, a table is cached using a cacheTable operation.

A table called table1 is available.

Instructions
100 XP

- List the tables with the listTables() method.
- Cache table1 and confirm that it is cached.
- Uncache table1 and confirm that it is uncached.

'''
print("Tables:\n", spark.catalog.listTables())

# Cache table1 and Confirm that it is cached
spark.catalog.cacheTable('table1')
print("table1 is cached: ", spark.catalog.isCached('table1'))

# Uncache table1 and confirm that it is uncached
spark.catalog.uncacheTable('table1')
print("table1 is cached: ", spark.catalog.isCached('table1'))
