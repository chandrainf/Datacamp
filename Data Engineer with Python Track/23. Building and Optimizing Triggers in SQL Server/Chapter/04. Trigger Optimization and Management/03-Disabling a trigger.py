'''
Disabling a trigger


Fresh Fruit Delivery needs to make some changes to a couple of rows in the Orders table.

Earlier they asked for a trigger to prevent unwanted changes to the Orders table, but now that trigger is stopping them from making the necessary modifications.

You are asked to help them with the situation by temporarily stopping that trigger from firing.

Instructions
100 XP

- Pause the trigger execution to allow the company to make the changes.

'''
-- Pause the trigger execution
DISABLE TRIGGER PreventOrdersUpdate
ON Orders
