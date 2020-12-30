'''
Preventing changes to orders


Fresh Fruit Delivery needs to prevent changes from being made to the Orders table.

Any attempt to do so should not be permitted and an error should be shown instead.

Instructions
100 XP

- Create a new trigger on the Orders table.
- Set the trigger to prevent updates and return an error message instead.

'''
-- Create the trigger
CREATE TRIGGER PreventOrdersUpdate
ON Orders
INSTEAD OF UPDATE
AS
RAISERROR('Updates on "Orders" table are not permitted.
          Place a new order to add new products.', 16, 1)
