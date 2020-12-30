'''
Modifying a trigger's definition


A member of the Sales team has noticed that one of the triggers attached to the Discounts table is showing a message with the word "allowed" missing.

Instructions
100 XP

- Modify the trigger definition and fix the typo without dropping and recreating the trigger.
- Add the missing word to the PRINT statement.

'''
-- Fix the typo in the trigger message
ALTER TRIGGER PreventDiscountsDelete
ON Discounts
INSTEAD OF DELETE
AS
PRINT 'You are not allowed to remove data from the Discounts table.'
