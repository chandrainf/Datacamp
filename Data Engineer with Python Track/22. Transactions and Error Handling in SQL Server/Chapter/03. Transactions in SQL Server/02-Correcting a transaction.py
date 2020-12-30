'''
Correcting a transaction


Today you have been given a script which is not correct. It was written by a colleague of yours who didn't know how to finish it. Your colleague tried to transfer $100 from account 1 to account 5, and register those movements into the transactions table.

You immediately realize there are several errors. SQL Server doesn't recognize the transaction statements it uses.

Can you correct the script?

Instructions
100 XP

- Run the code to verify there are errors.
- Correct every error.

'''

BEGIN TRY
   BEGIN TRAN
       UPDATE accounts SET current_balance = current_balance - 100 WHERE account_id = 1
        INSERT INTO transactions VALUES(1, -100, GETDATE())

        UPDATE accounts SET current_balance = current_balance + 100 WHERE account_id = 5
        INSERT INTO transactions VALUES(5, 100, GETDATE())
    ROLLBACK TRAN
END TRY
BEGIN CATCH
   ROLLBACK TRAN
END CATCH
