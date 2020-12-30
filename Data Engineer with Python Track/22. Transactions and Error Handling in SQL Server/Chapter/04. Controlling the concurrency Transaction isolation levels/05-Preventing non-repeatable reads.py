'''
Preventing non-repeatable reads


You are in charge of analyzing data about your bank customers.

You prepare a script that first selects the data of every customer. After that, your script needs to process some mathematical operations based on the result. (We won't focus on these operations for this exercise.) After that, you want to select the same data again, ensuring nothing has changed.

As this is critical, you think it is better if nobody can change anything in the customers table until you finish your analysis. In doing this, you prevent non-repeatable reads.

Instructions
100 XP

- Set the appropriate isolation level to prevent non-repeatable reads.
- Begin a transaction.
- Commit the transaction.

'''
-- Set the appropriate isolation level
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ

-- Begin a transaction
BEGIN TRAN

SELECT * FROM customers;

-- some mathematical operations, don't care about them...

SELECT * FROM customers;

-- Commit the transaction
COMMIT TRAN