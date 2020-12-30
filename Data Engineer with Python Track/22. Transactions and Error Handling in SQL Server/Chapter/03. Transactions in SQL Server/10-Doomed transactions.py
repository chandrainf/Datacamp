'''
Doomed transactions


You want to insert the data of two new customers into the customer table. You prepare a script controlling that if an error occurs, the transaction rollbacks and you get the message of the error. You want to control it using XACT_ABORT in combination with XACT_STATE.

Instructions
100 XP

- Use the appropriate setting of XACT_ABORT.
- Check if there is an open transaction.
- Rollback the transaction.
- Select the error message.

'''
-- Use the appropriate setting
SET XACT_ABORT OFF;
BEGIN TRY
	BEGIN TRAN;
		INSERT INTO customers VALUES('Mark', 'Davis', 'markdavis@mail.com', '555909090');
		INSERT INTO customers VALUES('Dylan', 'Smith', 'dylansmith@mail.com', '555888999');
	COMMIT TRAN;
END TRY
BEGIN CATCH
	-- Check if there is an open transaction
	IF XACT_STATE() <> 0
    	-- Rollback the transaction
		ROLLBACK TRAN;
    -- Select the message of the error
    SELECT ERROR_MESSAGE() AS Error_message;
END CATCH
