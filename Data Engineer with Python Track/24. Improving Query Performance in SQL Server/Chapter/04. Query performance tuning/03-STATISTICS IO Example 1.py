'''
STATISTICS IO: Example 1


Your sales company has just taken on a new regional manager for Western Europe. He has asked you to provide him daily updates on orders shipped to some key Western Europe capital cities. As this data is time sensitive, you want a robust query that is tuned to return the results as quickly as possible.

You initially decide on a query that uses two sub-queries: one in the SELECT statement to get the count of orders and one using a filter condition with an IN operator.

You will turn on the STATISTICS IO command to review the page read statistics.

Instructions 1/3
35 XP

- Turn on STATISTICS IO.

'''

SET STATISTICS IO ON-- Turn the IO command on


'''
Instructions 2/3
100 XP

- Add the table used to count the number of orders.
- Add the filter operator for the second sub-query.

'''
-- Example 1
SELECT CustomerID,
CompanyName,
(SELECT COUNT(*)
 FROM Orders AS o - - Add table
 WHERE c.CustomerID=o.CustomerID) CountOrders
FROM Customers AS c
WHERE CustomerID IN - - Add filter operator
(SELECT CustomerID
 FROM Orders
 WHERE ShipCity IN
 ('Berlin', 'Bern', 'Bruxelles', 'Helsinki',
  'Lisboa', 'Madrid', 'Paris', 'London'))


'''
Instructions 3/3
30 XP

Question

From the STATISTICS IO output below, how many data pages from the Orders table were read from memory to complete the query?

  Table 'Customers'. Scan count 1, logical reads 2, physical reads 0,...
  Table 'Orders'. Scan count 2, logical reads 32, physical reads 0,...

Possible Answers

    - Two

    - Zero

    - Thirty-two

    - One

Answer : Thirty-two

'''
