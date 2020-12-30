'''
STATISTICS IO comparison


Using the STATISTICS IO outputs from the example queries in the previous two exercises, what might you conclude?

Example 1

    Table 'Customers'. Scan count 1, logical reads 2, physical reads 0,....
    Table 'Orders'. Scan count 2, logical reads 32, physical reads 0,...

Example 2

    Table 'Customers'. Scan count 1, logical reads 2, physical reads 0,....
    Table 'Orders'. Scan count 2, logical reads 16, physical reads 0,...

Answer the question
50XP

Possible Answers

    - Nothing. We should use STATISTICS TIME to compare queries and not STATISTICS IO.

    - The Example 1 query will run faster than the Example 2 query.

    - The time to return the results from both queries will be the same.

    - The Example 2 query will run faster than the Example 1 query.

Answer : The Example 2 query will run faster than the Example 1 query.

'''
