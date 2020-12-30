'''
Using the READ UNCOMMITTED isolation level


A new client visits your bank to open an account. You insert her data into your system, causing a script like this one to start running:

  BEGIN TRAN

    INSERT INTO customers (first_name, last_name, email, phone)
    VALUES ('Ann', 'Ros', 'aros@mail.com', '555555555')

    DECLARE @cust_id INT = scope_identity()

    INSERT INTO accounts (account_number, customer_id, current_balance)
    VALUES ('55555555555010121212', @cust_id, 150)

  COMMIT TRAN
  
At that moment, your marketing colleague starts to send e-mails to every customer. There is going to be a raffle for a car! The script he executes gets every customer's data, including the last customer you inserted. This script starts running after the first insert occurs but before the COMMIT TRAN.

How can that be?

Instructions
100 XP

- Set the READ UNCOMMITTED isolation level.
- Select first_name, last_name, email and phone from customers table.

'''
-- Set the appropriate isolation level
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED

	-- Select first_name, last_name, email and phone
	SELECT
    	first_name, 
        last_name, 
        email,
        phone
    FROM customers;