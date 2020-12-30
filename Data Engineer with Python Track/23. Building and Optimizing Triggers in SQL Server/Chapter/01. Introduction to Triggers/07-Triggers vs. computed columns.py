'''
Triggers vs. computed columns


While continuing your analysis of the database, you find two other interesting objects:

    - The table SalesWithPrice has a column that calculates the TotalAmount as Quantity * Price. This is done using a computed column which uses columns from the same table for the calculation.

    - The trigger SalesCalculateTotalAmount was created on the SalesWithoutPrice table. The Price column is not part of the SalesWithoutPrice table, so a computed column cannot be used for the TotalAmount. The trigger overcomes this limitation by using the Price column from the Products table.

Instructions 1/3
35 XP

Insert new data into SalesWithPrice and then run a SELECT from the same table to verify the outcome.

'''
-- Add the following rows to the table
INSERT INTO SalesWithPrice(Customer, Product, Price, Currency, Quantity)
VALUES('Fruit Mag', 'Pomelo', 1.12, 'USD', 200),
('VitaFruit', 'Avocado', 2.67, 'USD', 400),
('Tasty Fruits', 'Blackcurrant', 2.32, 'USD', 1100),
('Health Mag', 'Kiwi', 1.42, 'USD', 100),
('eShop', 'Plum', 1.1, 'USD', 500)

-- Verify the results after adding the new rows
SELECT * FROM SalesWithPrice

'''
Instructions 2/3
35 XP

Insert new data into SalesWithoutPrice and then run a SELECT from the same table to verify the outcome.

'''
-- Add the following rows to the table
INSERT INTO SalesWithoutPrice(Customer, Product, Currency, Quantity)
VALUES('Fruit Mag', 'Pomelo', 'USD', 200),
('VitaFruit', 'Avocado', 'USD', 400),
('Tasty Fruits', 'Blackcurrant', 'USD', 1100),
('Health Mag', 'Kiwi', 'USD', 100),
('eShop', 'Plum', 'USD', 500)

-- Verify the results after the INSERT
SELECT * FROM SalesWithoutPrice

'''
Instructions 3/3
30 XP

Question

The previous step used both a computed column and a trigger to calculate the TotalAmount value automatically. From a user perspective, there was no difference, but from a technical perspective, there is one.

What is the major limitation of computed columns that can be easily overcome with the use of triggers?

Possible Answers

    - A computed column cannot use columns from other tables for the calculation.

    - A computed column cannot use columns from the same table for the calculation.

    - A computed column cannot use other columns for the calculation.

    - A computed column cannot use more than one column for the calculation.

Answer : A computed column cannot use columns from other tables for the calculation.

'''
