'''
Preventing table deletion


Fresh Fruit Delivery wants to prevent its regular employees from deleting tables from the database.

Instructions
100 XP

- Create a new trigger, PreventTableDeletion, to prevent table deletion.
- The trigger should roll back the firing statement, so the deletion does not happen.

'''
-- Add a trigger to disable the removal of tables
CREATE TRIGGER PreventTableDeletion
ON DATABASE
FOR CREATE_TABLE
AS
	RAISERROR('You are not allowed to remove tables from this database.', 16, 1);
    -- Revert the statement that removes the table
    ROLLBACK;
