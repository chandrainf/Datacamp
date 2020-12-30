'''
Prevent phantom reads just in some rows


You need to analyze some data about your bank customers with the customer_id between 1 and 10. You only want to lock the rows of the customers table with the customer_id between 1 and 10. In doing this, you guarantee nobody will be able to change these rows, and you allow other transactions to work with the rest of the table.

You need to select the customers and execute some mathematical operations again. (We won't focus either on these operations for this exercise.) After that, you want to select the customers with the customer_id between 1 and 10 again, ensuring nothing has changed.

How can you prepare the script?

Instructions
100 XP

- Set the appropriate isolation level to prevent phantom reads.
- Begin a transaction.
- Select those customers you want to lock.
- Commit the transaction.

'''
-- Set the appropriate isolation level
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE

-- Begin a transaction
BEGIN TRAN

SELECT * 
FROM customers
-- Select customer_id between 1 and 10
WHERE customer_id BETWEEN 1 AND 10;

-- After completing some mathematical operation, select customer_id between 1 and 10
SELECT * 
FROM customers
WHERE customer_id BETWEEN 1 AND 10;

-- Commit the transaction
COMMIT TRAN