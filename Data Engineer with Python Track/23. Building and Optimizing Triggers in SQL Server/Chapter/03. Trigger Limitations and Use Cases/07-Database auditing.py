'''
Database auditing


Your next task is to develop a new trigger to audit database object changes.

You need to create the trigger at the database level. You can use the DDL_TABLE_VIEW_EVENTS group event to fire the trigger. This group event includes any database operation involving tables, views, indexes, or statistics. By using the group event, you do not need to specify all the events individually.

The trigger will insert details about the firing statement (event, user, query, etc.) into the DatabaseAudit table.

Instructions
100 XP

- Create a DatabaseAudit trigger on the database that fires for DDL_TABLE_VIEW_EVENTS.

'''
-- Create a new trigger
CREATE TRIGGER DatabaseAudit
-- Attach the trigger at the database level
ON DATABASE
-- Fire the trigger for all tables / views events
FOR DDL_TABLE_VIEW_EVENTS
AS
INSERT INTO DatabaseAudit(EventType, DatabaseName, SchemaName, Object, ObjectType, UserAccount, Query, EventTime)
SELECT EVENTDATA().value('(/EVENT_INSTANCE/EventType)[1]', 'NVARCHAR(50)') AS EventType
, EVENTDATA().value('(/EVENT_INSTANCE/DatabaseName)[1]', 'NVARCHAR(50)') AS DatabaseName
, EVENTDATA().value('(/EVENT_INSTANCE/SchemaName)[1]', 'NVARCHAR(50)') AS SchemaName
, EVENTDATA().value('(/EVENT_INSTANCE/ObjectName)[1]', 'NVARCHAR(100)') AS Object
, EVENTDATA().value('(/EVENT_INSTANCE/ObjectType)[1]', 'NVARCHAR(50)') AS ObjectType
, EVENTDATA().value('(/EVENT_INSTANCE/LoginName)[1]', 'NVARCHAR(100)') AS UserAccount
, EVENTDATA().value('(/EVENT_INSTANCE/TSQLCommand/CommandText)[1]', 'NVARCHAR(MAX)') AS Query
, EVENTDATA().value('(/EVENT_INSTANCE/PostTime)[1]', 'DATETIME') AS EventTime
