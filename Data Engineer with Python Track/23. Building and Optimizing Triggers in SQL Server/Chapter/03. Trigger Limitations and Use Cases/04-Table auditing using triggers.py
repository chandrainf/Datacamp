'''
Table auditing using triggers


The company has decided to keep track of changes made to all the most important tables. One of those tables is Orders.

Any modification made to the content of Orders should be inserted into TablesAudit.

Instructions
100 XP

- Create a new AFTER trigger on the Orders table.
- Set the trigger to fire for INSERT, UPDATE, and DELETE statements.

'''
-- Add a trigger that tracks table changes
CREATE TRIGGER OrdersAudit
ON Orders
AFTER INSERT, UPDATE, DELETE
AS
	DECLARE @Insert BIT = 0;
	DECLARE @Delete BIT = 0;
	IF EXISTS(SELECT * FROM inserted) SET @Insert = 1;
	IF EXISTS(SELECT * FROM deleted) SET @Delete = 1;
	INSERT INTO TablesAudit(TableName, EventType, UserAccount, EventDate)
	SELECT 'Orders' AS TableName
	       , CASE WHEN @Insert = 1 AND @Delete = 0 THEN 'INSERT'
				 WHEN @Insert = 1 AND @Delete = 1 THEN 'UPDATE'
				 WHEN @Insert = 0 AND @Delete = 1 THEN 'DELETE'
				 END AS Event
		   ,ORIGINAL_LOGIN() AS UserAccount
		   ,GETDATE() AS EventDate;
