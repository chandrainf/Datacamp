'''
STATISTICS IO: Example 2


In the previous exercise, you were asked you to provide a new regional manager daily updates on orders shipped to Western Europe capital cities. You initially created a query that contained two sub-queries. You decide to do a rewrite and use an INNER JOIN.

The STATISTICS IO command is turned on. You will need to turn it off after completing the query.

Instructions 1/3
50 XP

- Add the join operator.
- Add the shipping destination city column in the filter condition.

'''

-- Example 2
SELECT c.CustomerID,
c.CompanyName,
COUNT(o.CustomerID)
FROM Customers AS c
INNER JOIN Orders AS o - - Join operator
ON c.CustomerID = o.CustomerID
WHERE o.ShipCity IN - - Shipping destination column
('Berlin', 'Bern', 'Bruxelles', 'Helsinki',
 'Lisboa', 'Madrid', 'Paris', 'London')
GROUP BY c.CustomerID,
c.CompanyName


'''
Instructions 2/3
35 XP

- Turn off STATISTICS IO.

'''

SET STATISTICS IO OFF - - Turn the IO command off


'''
Instructions 3/3
50 XP

Question

From the STATISTICS IO output below, how many data pages from the Orders table were read from memory to complete the query?

    Table 'Customers'. Scan count 1, logical reads 2, physical reads 0,...
    Table 'Orders'. Scan count 2, logical reads 16, physical reads 0,...

Possible Answers

    - Zero

    - Sixteen

    - One

    - Two

Answer : Sixteen

'''
