'''
Preventing changes to Products


The Fresh Fruit Delivery company doesn't want regular users to be able to change product information or the actual stock.

Instructions
100 XP

- Create a new trigger, PreventProductChanges, that prevents any updates to the Products table.

'''
-- Prevent any product changes
CREATE TRIGGER PreventProductChanges
ON Products
AFTER insert, UPDATE
AS
RAISERROR('Updates of products are not permitted. Contact the database administrator if a change is needed.', 16, 1)
