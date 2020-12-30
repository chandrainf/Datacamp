'''
Triggers vs. stored procedures
One important task when you take ownership of an existing database is to familiarize yourself with the objects that comprise the database.

This task includes getting to know existing procedures, functions, and triggers.

You find the following objects in the Fresh Fruit Delivery database:

The company uses a regular stored procedure, MonthlyOrders, for reporting purposes. The stored procedure sums up order amounts for each product every month.

The trigger CustomerDiscountHistory is used to keep a history of the changes that occur in the Discounts table. The trigger is fired when updates are made to the Discounts table, and it stores the old and new values from the Discount column into the table DiscountsHistory.

Instructions 1/2
50 XP

- Run an update on the Discounts table (this will fire the CustomerDiscountHistory trigger).
- Get all the rows from DiscountsHistory to verify the outcome.

'''
-- Run an update for some of the discounts
UPDATE Discounts
SET Discount = Discount + 1
WHERE Discount <= 5

-- Verify the trigger ran successfully
SELECT * FROM DiscountsHistory

'''
Instructions 2/2
50 XP

Question

Execute the MonthlyOrders regular stored procedure, using EXECUTE MonthlyOrders.

Then, try to execute the CustomerDiscountHistory trigger using

UPDATE Discounts SET Discount = Discount + 1 WHERE Discount <= 5

What conclusions can be drawn from the execution results and the step performed earlier?

Possible Answers

    - Both triggers and regular stored procedures can be executed explicitly when needed.

    - Triggers can only be fired by the corresponding event, while regular stored procedures can be executed explicitly when needed.

    - Triggers can be executed explicitly when needed, while regular stored procedures can only be fired by a corresponding event.

    - Triggers can be fired by the corresponding event, but can also be executed explicitly when needed.

Answer : Triggers can only be fired by the corresponding event, while regular stored procedures can be executed explicitly when needed.

'''
