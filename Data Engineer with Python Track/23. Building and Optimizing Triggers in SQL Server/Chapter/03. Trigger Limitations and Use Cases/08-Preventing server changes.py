'''
Preventing server changes


The company is also asking you to find a method to prevent databases from being mistakenly deleted by employees.

After a detailed analysis, you decide to use a trigger to fulfill the request.

The trigger will roll back any attempts to delete databases.

Instructions
100 XP

- Create a new trigger called PreventDatabaseDelete.
- Attach the trigger at the server level.

'''
-- Create a trigger to prevent database deletion
CREATE TRIGGER PreventDatabaseDelete
-- Attach the trigger at the server level
ON all server
FOR DROP_DATABASE
AS
PRINT 'You are not allowed to remove existing databases.'
ROLLBACK
