'''
Creating a trigger to keep track of data changes


The Fresh Fruit Delivery company needs to keep track of any new items added to the Products table. You can do this by using a trigger.

The new trigger will store the name, price, and first introduced date for new items into a ProductsHistory table.

Instructions
100 XP

- Create the ProductsNewItems trigger on the Products table.
- Set the trigger to fire when data is inserted into the table.

'''
-- Create a new trigger
CREATE TRIGGER ProductsNewItems
ON Products
AFTER INSERT
AS
-- Add details to the history table
INSERT INTO ProductsHistory(Product, Price, Currency, FirstAdded)
SELECT Product, Price, Currency, GETDATE()
FROM inserted
