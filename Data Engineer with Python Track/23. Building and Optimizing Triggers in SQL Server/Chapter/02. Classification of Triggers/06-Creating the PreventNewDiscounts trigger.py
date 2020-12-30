'''
Creating the PreventNewDiscounts trigger


The company doesn't want regular users to add discounts. Only the Sales Manager should be able to do that.

To prevent such changes, you need to create a new trigger called PreventNewDiscounts.

The trigger should be attached to the Discounts table and prevent new rows from being added to the table.

Instructions
100 XP

- Create the trigger PreventNewDiscounts on the Discounts table.
- Set the trigger to prevent any rows being added to the Discounts table.

'''
-- Create a new trigger
CREATE TRIGGER PreventNewDiscounts
ON Discounts
INSTEAD OF INSERT
AS
RAISERROR('You are not allowed to add discounts for existing customers.
          Contact the Sales Manager for more details.', 16, 1)
