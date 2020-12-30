'''
STATISTICS TIME results


In the previous exercise, the STATISTICS TIME command was used on two different queries. The following table summarizes an analysis of the elapsed time statistics for each query.

Query	Details	Average elapsed time (ms)
1	    Filters the Teams table using IN and three sub-queries	20
2	    Filters the Teams table using EXISTS	3

What conclusion can you make from this summary?

Instructions
50 XP

Possible Answers

    - None. CPU time is a better measure to compare queries.

    - The second query that uses EXISTS is more efficient.

    - None. Elapsed time should be reported as a minimum, not an average.

    - The database server processors must be running in parallel.


Answer : The second query that uses EXISTS is more efficient.

'''
