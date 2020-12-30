'''
Prevent phantom reads in a table


Today you have to analyze the data of every customer of your bank. As this information is very important, you think about locking the complete customers table, so that nobody will be able to change anything in this table. In doing this, you prevent phantom reads.

You prepare a script to select that information, and with the result of this selection, you need to process some mathematical operations. (We won't focus on these operations for this exercise.) After that, you want to select the same data again, ensuring nothing has changed.

Instructions
100 XP

- Set the appropriate isolation level to prevent phantom reads.
- Begin the transaction.
- Commit the transaction.

'''

-- Set the appropriate isolation level
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE
-- Begin a transaction
BEGIN TRAN

SELECT * FROM customers;

-- After some mathematical operations, we selected information from the customers table.
SELECT * FROM customers;

-- Commit the transaction
COMMIT TRAN