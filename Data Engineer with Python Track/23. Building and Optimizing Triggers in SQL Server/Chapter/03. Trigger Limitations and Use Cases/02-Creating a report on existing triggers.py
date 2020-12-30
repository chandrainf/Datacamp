'''
Creating a report on existing triggers


Taking on the responsibility of administrating the database for the Fresh Fruit Delivery company also means keeping an eye on existing triggers.

The best approach is to have a report that can be run regularly and outputs details of the existing triggers.

This will ensure you have a good overview of the triggers and give you access to some interesting information.

Instructions 1/3
35 XP

-Start creating the triggers report by gathering information about existing database triggers from the sys.triggers table.

'''
-- Get the column that contains the trigger name
SELECT name AS TriggerName,
	   parent_class_desc AS TriggerType,
	   create_date AS CreateDate,
	   modify_date AS LastModifiedDate,
	   is_disabled AS Disabled,
       -- Get the column that tells if it's an INSTEAD OF trigger
	   is_instead_of_trigger AS InsteadOfTrigger
FROM sys.triggers;

'''
Instructions 2/3
35 XP

-Include information about existing server-level triggers from the sys.server_triggers table and order by trigger name.

'''
-- Gather information about database triggers
SELECT name AS TriggerName,
	   parent_class_desc AS TriggerType,
	   create_date AS CreateDate,
	   modify_date AS LastModifiedDate,
	   is_disabled AS Disabled,
	   is_instead_of_trigger AS InsteadOfTrigger,
       -- Get the trigger definition by using a function
	   OBJECT_DEFINITION (object_id)
FROM sys.triggers
UNION ALL
-- Gather information about server triggers
SELECT name AS TriggerName,
	   parent_class_desc AS TriggerType,
	   create_date AS CreateDate,
	   modify_date AS LastModifiedDate,
	   is_disabled AS Disabled,
	   0 AS InsteadOfTrigger,
       -- Get the trigger definition by using a function
	   OBJECT_DEFINITION (object_id)
FROM sys.server_triggers
ORDER BY TriggerName;

'''
Instructions 3/3
30 XP

-Enhance the report by including the trigger definitions. You can get a trigger's definition using the OBJECT_DEFINITION function.

'''
-- Gather information about database triggers
SELECT name AS TriggerName,
	   parent_class_desc AS TriggerType,
	   create_date AS CreateDate,
	   modify_date AS LastModifiedDate,
	   is_disabled AS Disabled,
	   is_instead_of_trigger AS InsteadOfTrigger,
       -- Get the trigger definition by using a function
	   OBJECT_DEFINITION (object_id)
FROM sys.triggers
UNION ALL
-- Gather information about server triggers
SELECT name AS TriggerName,
	   parent_class_desc AS TriggerType,
	   create_date AS CreateDate,
	   modify_date AS LastModifiedDate,
	   is_disabled AS Disabled,
	   0 AS InsteadOfTrigger,
       -- Get the trigger definition by using a function
	   OBJECT_DEFINITION (object_id)
FROM sys.server_triggers
ORDER BY TriggerName;
