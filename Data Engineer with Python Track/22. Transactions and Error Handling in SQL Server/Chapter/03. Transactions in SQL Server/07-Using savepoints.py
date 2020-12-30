'''
Using savepoints


Your colleague Anita needs help. She prepared a script that uses savepoints, but it doesn't work. The script marks the first savepoint, savepoint1 and then inserts the data of a customer. Then, the script marks another savepoint, savepoint2, and inserts the data of another customer again. After that, both savepoints are rolled back. Finally, the script marks another savepoint, savepoint3, and inserts the data of another customer.

Anita tells you that her script doesn't work because it has some errors, but she doesn't know how to correct them. Can you help her?

Instructions
100 XP

- Run the code to verify there are errors.
- Correct every error.

'''
BEGIN TRAN;
	-- Mark savepoint1
	SAVE TRAN savepoint1;
	INSERT INTO customers VALUES('Mark', 'Davis', 'markdavis@mail.com', '555909090');

	-- Mark savepoint2
    SAVE TRAN savepoint2;
	INSERT INTO customers VALUES ('Zack', 'Roberts', 'zackroberts@mail.com', '555919191');

	-- Rollback savepoint2
	ROLLBACK TRAN savepoint2;
    -- Rollback savepoint1
	ROLLBACK TRAN savepoint1;

	-- Mark savepoint3
	SAVE TRAN savepoint3;
	INSERT INTO customers VALUES ('Jeremy', 'Johnsson', 'jeremyjohnsson@mail.com', '555929292');
-- Commit the transaction
COMMIT TRAN;
