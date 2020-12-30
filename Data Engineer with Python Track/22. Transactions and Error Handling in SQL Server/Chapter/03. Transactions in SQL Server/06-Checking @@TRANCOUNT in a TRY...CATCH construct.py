'''
Checking @@TRANCOUNT in a TRY...CATCH construct


The owner of account 10 has won a raffle and will be awarded $200. You prepare a simple script to add those $200 to the current_balance of account 10. You think you have written everything correctly, but you prefer to check your code.

In fact, you made a silly mistake when adding the money: SET current_balance = 'current_balance' + 200. You wrote 'current_balance' as a string, which generates an error.

The script you create should rollback every change if an error occurs, checking if there is an open transaction. If everything goes correctly, the transaction should be committed, also checking if there is an open transaction.

Instructions
100 XP

- Begin the transaction.
- Correct the mistake in the operation.
- Inside the TRY block, check if there is a transaction and commit it.
- Inside the CATCH block, check if there is a transaction and roll it back.

'''
BEGIN TRY
	-- Begin the transaction
	BEGIN TRAN;
    	-- Correct the mistake
		UPDATE accounts SET current_balance = current_balance + 200
			WHERE account_id = 10;
    	-- Check if there is a transaction
		IF @@TRANCOUNT > 0     
    		-- Commit the transaction
			COMMIT TRAN;
     
	SELECT * FROM accounts
    	WHERE account_id = 10;      
END TRY
BEGIN CATCH  
    SELECT 'Rolling back the transaction'; 
    -- Check if there is a transaction
    IF @@TRANCOUNT > 0   	
    	-- Rollback the transaction
        ROLLBACK TRAN;
END CATCH