'''
Checking stock before placing orders


On multiple occasions, customers have placed orders for products when the company didn't have enough stock to fulfill the orders.

This issue can be easily fixed by adding a new trigger with conditional logic for its actions.

The trigger should fire when new rows are added to the Orders table and check if the company has sufficient stock of the specified products to fulfill those orders.

If there is sufficient stock, the trigger will then perform the same INSERT operation like the one that fired it—only this time, the values will be taken from the inserted special table.

Instructions
100 XP

- Add a new trigger that fires for INSERT statements and checks if the order quantity can be fulfilled by the current stock.
- Raise an error if there's insufficient stock. Otherwise, perform an INSERT by making use of the inserted special table.

'''
-- Create a new trigger to confirm stock before ordering
CREATE TRIGGER ConfirmStock
ON Orders
INSTEAD OF INSERT
AS
  IF EXISTS(SELECT *
              FROM Products AS p
              INNER JOIN inserted AS i ON i.Product=p.Product
              WHERE p.Quantity < i.Quantity)
   BEGIN
       RAISERROR(
           'You cannot place orders when there is no stock for the order''s product.', 16, 1)
    END
    ELSE
    BEGIN
      INSERT INTO Orders (OrderID, Customer, Product, Price, Currency, Quantity, WithDiscount, Discount, OrderDate, TotalAmount, Dispatched)
       SELECT OrderID, Customer, Product, Price, Currency, Quantity, WithDiscount, Discount, OrderDate, TotalAmount, Dispatched FROM Orders
    END
