'''
Prevent dirty reads


You have to analyze how many accounts have more than $50,000.

As the number of accounts is an important result, you don't want to read data modified by other transactions that haven't committed or rolled back yet. In doing this, you prevent dirty reads. However, you don't need to consider having non-repeatable or phantom reads.

Prepare the script.

Instructions
100 XP

- Set the appropriate isolation level to prevent dirty reads.
- Select the count of accounts that match the criteria.

'''
-- Set the appropriate isolation level
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

-- Count the accounts
SELECT COUNT(*) AS number_of_accounts
FROM accounts
WHERE current_balance >= 50000
