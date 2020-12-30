'''
Practicing creating triggers


The Fresh Fruit Delivery company needs help creating a new trigger called OrdersUpdatedRows on the Orders table.

This trigger will be responsible for filling in a historical table (OrdersUpdate) where information about the updated rows is kept.

A historical table is often used in practice to store information that has been altered in the original table. In this example, changes to orders will be saved into OrdersUpdate to be used by the company for auditing purposes.

Instructions
100 XP

- Create the new trigger for the Orders table.
- Set the trigger to be fired only after UPDATE statements.

'''
-- Set up a new trigger
CREATE TRIGGER OrdersUpdatedRows
ON Orders
-- The trigger should fire after UPDATE statements
AFTER UPDATE
-- Add the AS keyword before the trigger body
AS
-- Insert details about the changes to a dedicated table
INSERT INTO OrdersUpdate(OrderID, OrderDate, ModifyDate)
SELECT OrderID, OrderDate, GETDATE()
FROM inserted
