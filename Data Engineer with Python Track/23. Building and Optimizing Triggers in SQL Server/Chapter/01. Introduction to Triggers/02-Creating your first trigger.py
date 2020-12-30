'''
Creating your first trigger


You have been hired by the company Fresh Fruit Delivery to help secure their database and ensure data integrity. The company sells fresh fruit to other online shops, and they use several tables to keep track of stock and placed orders.

One of their tables (Discounts) specifies the discount amount that shops receive when placing large orders. A deletion of several hundred rows happened at some point in the past when one of their employees removed some orders by mistake. They need a new trigger on the Discounts table to prevent DELETE statements related to the table, and this is where you can help.

Instructions
100 XP

- Create a new trigger on the Discounts table.
- Use the trigger to prevent DELETE statements.

'''
-- Create a new trigger that fires when deleting data
CREATE TRIGGER PreventDiscountsDelete
ON Discounts
-- The trigger should fire instead of DELETE
INSTEAD OF DELETE
AS
PRINT 'You are not allowed to delete data from the Discounts table.'
