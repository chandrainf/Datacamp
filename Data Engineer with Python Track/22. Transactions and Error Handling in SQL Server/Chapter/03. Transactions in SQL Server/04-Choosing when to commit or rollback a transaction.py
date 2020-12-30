'''
Choosing when to commit or rollback a transaction


The bank where you work has decided to give $100 to those accounts with less than $5,000. However, the bank director only wants to give that money if there aren't more than 200 accounts with less than $5,000.

You prepare a script to give those $100, and of the multiple ways of doing it, you decide to open a transaction and then update every account with a balance of less than $5,000. After that, you check the number of the rows affected by the update, using the @@ROWCOUNT function. If this number is bigger than 200, you rollback the transaction. Otherwise, you commit it.

How do you prepare the script?

Instructions
100 XP

- Begin the transaction.
- Check if the number of affected rows is bigger than 200.
- Rollback the transaction if the number of affected rows is more than 200.
- Commit the transaction if the number of affected rows is less than or equal to 200.

'''
-- Begin the transaction
BEGIN TRAN;
   UPDATE accounts set current_balance = current_balance + 100
        WHERE current_balance < 5000
    -- Check number of affected rows
    IF @@ROWCOUNT > 200
        BEGIN
        -- Rollback the transaction
            ROLLBACK TRAN;
            SELECT 'More accounts than expected. Rolling back';
        END
    ELSE
        BEGIN
        -- Commit the transaction
            COMMIT TRAN;
            SELECT 'Updates commited';
        END
