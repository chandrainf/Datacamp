'''
Rolling back a transaction if there is an error


On your first day of work, you were given the task of setting up transactions that record when money is transferred in your bank.

You want to prepare a simple script where $100 transfers from account_id = 1 and goes to account_id = 5. After that, it registers those movements into the transactions table. You think you have written everything correctly, but as a cautious worker, you prefer to check everything!

As a matter of fact, you did make a mistake. Instead of inserting a new transaction for account 5, you did it for account 500, which doesn't exist.

To prevent future errors, the script you create should rollback every change if an error occurs. If everything goes correctly, the transaction should be committed.

Instructions
100 XP

- Begin the transaction.
- Correct the mistake in the operation.
- Commit the transaction if there are no errors.
- Inside the CATCH block, roll back the transaction.

'''
BEGIN TRY
	-- Begin the transaction
	BEGIN TRAN;
		UPDATE accounts SET current_balance = current_balance - 100 WHERE account_id = 1;
		INSERT INTO transactions VALUES(1, -100, GETDATE());

		UPDATE accounts SET current_balance = current_balance + 100 WHERE account_id = 5;
        -- Correct it
		INSERT INTO transactions VALUES(5, 100, GETDATE());
    -- Commit the transaction
	COMMIT TRAN;    
END TRY
BEGIN CATCH  
	SELECT 'Rolling back the transaction';
    -- Rollback the transaction
	ROLLBACK TRAN;
END CATCH
