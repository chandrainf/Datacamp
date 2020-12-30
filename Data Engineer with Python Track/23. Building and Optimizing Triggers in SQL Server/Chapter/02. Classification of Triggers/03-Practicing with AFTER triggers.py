'''
Practicing with AFTER triggers


Fresh Fruit Delivery company is happy with your services, and they've decided to keep working with you.

You have been given the task to create new triggers on some tables, with the following requirements:

    - Keep track of canceled orders (rows deleted from the Orders table). Their details will be kept in the table CanceledOrders upon removal.

    - Keep track of discount changes in the table Discounts. Both the old and the new values will be copied to the DiscountsHistory table.

    - Send an email to the Sales team via the SendEmailtoSales stored procedure when a new order is placed.

Instructions 1/3
35 XP

- Create a new trigger on the Orders table to keep track of any canceled orders.

'''

-- Create a new trigger for canceled orders
CREATE TRIGGER KeepCanceledOrders
ON Orders
AFTER UPDATE
AS
INSERT INTO CanceledOrders
SELECT * FROM deleted


'''
Instructions 2/3
35 XP

Create a new trigger on the Discounts table to keep track of discount value changes.
'''


-- Create a new trigger to keep track of discounts
CREATE TRIGGER CustomerDiscountHistory
ON Discounts
AFTER UPDATE
AS
-- Store old and new values into the `DiscountsHistory` table
INSERT INTO DiscountsHistory(Customer, OldDiscount, NewDiscount, ChangeDate)
SELECT i.Customer, d.Discount, i.Discount, GETDATE()
FROM inserted AS i
INNER JOIN deleted AS d ON i.Customer = d.Customer


'''
Instructions 2/3
30 XP

Create the trigger NewOrderAlert to notify the Sales team when new orders are placed.
'''


-- Notify the Sales team of new orders
CREATE TRIGGER NewOrderAlert
ON Orders
AFTER UPDATE
AS
EXECUTE SendEmailtoSales
