'''
XACT_ABORT and THROW


The wealthiest customers of the bank where you work have decided to donate the 0.01% of their current_balance to a non-profit organization. You are in charge of preparing the script to update the customer's accounts, but you have to do it only for those accounts with a current_balance with more than $5,000,000. The director of the bank tells you that if there aren't at least 10 wealthy customers, you shouldn't do this operation, because she wants to interview more customers.

You prepare a script, and of the multiple ways of doing it, you decide to use XACT_ABORT in combination with THROW. This way, if the number of affected rows is less than or equal to 10, you can throw an error so that the transaction is rolled back.

Instructions
100 XP

- Use the appropriate setting of XACT_ABORT.
- Begin the transaction.
- If the number of affected rows is less than or equal to 10, throw the error using the THROW statement, with a number of 55000.
- Commit the transaction if the number of affected rows is more than 10.

'''
-- Use the appropriate setting
SET XACT_ABORT ON
-- Begin the transaction
BEGIN TRAN;
   UPDATE accounts set current_balance = current_balance - current_balance * 0.01 / 100
        WHERE current_balance > 5000000
    IF @@ROWCOUNT <= 10
    -- Throw the error
        THROW 55000, 'Not enough wealthy customers!', 1
    ELSE
    -- Commit the transaction
        COMMIT TRAN
