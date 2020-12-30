'''
Tracking table changes


You need to create a new trigger at the database level that logs modifications to the table TablesChangeLog.

The trigger should fire when tables are created, modified, or deleted.

Instructions
100 XP

Create the new trigger following the company's requirements.

'''
-- Create the trigger to log table info
CREATE TRIGGER TrackTableChanges
ON DATABASE
FOR CREATE_TABLE,
	ALTER_TABLE,
	DROP_TABLE
AS
	INSERT INTO TablesChangeLog(EventData, ChangedBy)
    VALUES (EVENTDATA(), USER);
