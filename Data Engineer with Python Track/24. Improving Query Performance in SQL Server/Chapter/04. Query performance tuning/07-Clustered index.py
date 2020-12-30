'''
Clustered index


Clustered indexes can be added to tables to speed up search operations in queries. You have two copies of the Cities table from the Earthquakes database: one copy has a clustered index on the CountryCode column. The other is not indexed.

You have a query on each table with a different filter condition:

Query 1

    - Returns all rows where the country is either Russia or China.

Query 2

    - Returns all rows where the country is either Jamaica or New Zealand.

Instructions 1/3
35 XP

- Add the two country codes to the filter condition for Query 1.

'''

-- Query 1
SELECT *
FROM Cities
WHERE CountryCode = 'RU' - - Country code
OR CountryCode = 'CN' - - Country code


'''
Instructions 2/3
35 XP

- Add the two country codes to the filter condition for Query 2.

'''

-- Query 2
SELECT *
FROM Cities
WHERE CountryCode IN('JM', 'NZ') - - Country codes


'''
Instructions 3/3
30 XP

Question

For these two queries, what conclusion could you make using the following output from the STATISTICS IO command?

Query 1

    4694 results returned
    Table 'Cities'. ..., logical reads 274, ... ,

Query 2

    212 results returned
    Table 'Cities'. ..., logical reads 10, ... ,

Possible Answers

    - Query 1 accesses a clustered index because proportionally there were fewer logical reads for results returned.

    - The filter conditions are different; therefore it is not possible to tell which query is accessing a clustered index. The number of rows returned needs to be the same to make the comparison.

    - Query 2 accesses a clustered index because logical reads indicates fewer data pages were accessed compared to Query 1

    - Results returned versus logical reads are proportionally similar, so there is no way to tell which query is accessing a clustered index.

Answer : Query 2 accesses a clustered index because logical reads indicates fewer data pages were accessed compared to Query 1

'''
