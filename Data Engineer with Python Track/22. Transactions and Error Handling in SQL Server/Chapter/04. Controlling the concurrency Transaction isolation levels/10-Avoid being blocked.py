'''
Avoid being blocked


You are trying to select every movement of account 1 from the transactions table. When selecting that information, you are blocked by another transaction, and the result doesn't output. Your database is configured under the READ COMMITTED isolation level.

Can you change your select query to get the information right now without changing the isolation level? In doing this you can read the uncommitted data from the transactions table.

Instructions
100 XP

- Change your script to avoid being blocked.

'''

SELECT *
-- Avoid being blocked
FROM transactions WITH(NOLOCK)
WHERE account_id = 1
