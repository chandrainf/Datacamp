'''
Exclusive LEFT OUTER JOIN


An exclusive LEFT OUTER JOIN can be used to check for the presence of data in one table that is absent in another table. To create an exclusive LEFT OUTER JOIN the right query requires an IS NULL filter condition on the joining column.

Your sales manager is concerned that orders from French customers are declining. He wants you to compile a list of French customers that have not placed any orders so he can contact them.

Instructions 1/2
50 XP

- Add the joining operator between the Customers and Orders tables.
- Add the joining columns from the Customers and Orders tables

'''
-- First attempt
SELECT c.CustomerID,
c.CompanyName,
c.ContactName,
c.ContactTitle,
c.Phone
FROM Customers c
LEFT OUTER JOIN Orders o - - Joining operator
ON c.CustomerID = o.CustomerID - - Joining columns
WHERE c.Country = 'France'


'''
Instructions 2/2
50 XP

- Add the filter condition to turn the query into an exclusive LEFT OUTER JOIN

'''
SELECT c.CustomerID,
c.CompanyName,
c.ContactName,
c.ContactTitle,
c.Phone
FROM Customers c
LEFT OUTER JOIN Orders o
ON c.CustomerID = o.CustomerID
WHERE c.Country = 'France'
AND o.CustomerID IS NULL
-- Filter condition
