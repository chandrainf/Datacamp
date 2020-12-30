'''
Identifying problematic triggers


You've identified an issue when placing new orders in the company's sales system.

The issue is related to a trigger run, but you don't have many details on the triggers themselves. Unfortunately, the database objects (including triggers) are not documented.

You need to identify the trigger that's causing the problem to proceed with the investigation. To be sure, you need to gather some important details about the triggers.

The only information you have when starting the investigation is that the table related to the issues is Orders.

Instructions 1/4
25 XP

- Find the ID of the Orders table by using the sys.objects system view.

'''
-- Get the table ID
SELECT object_id AS TableID
FROM sys.objects
WHERE name = 'Orders'

'''


Instructions 2/4
25 XP

- Find all the triggers attached to the Orders table by joining the first query with sys.triggers.
- Select the trigger name column.

'''
-- Get the trigger name
SELECT t.object_id AS TriggerName
FROM sys.objects AS o
-- Join with the triggers table
INNER JOIN sys.triggers AS t ON t.parent_id = o.object_id
WHERE o.name = 'Orders'

'''



Instructions 3/4
25 XP

- Filter the triggers fired for UPDATE statements, joining the previous query with sys.trigger_events.
- Select the triggers and their firing statements by matching the object_id columns from sys.triggers and sys.trigger_events.

'''
SELECT t.name AS TriggerName
FROM sys.objects AS o
INNER JOIN sys.triggers AS t ON t.parent_id = o.object_id
-- Get the trigger events
INNER JOIN sys.trigger_events AS te ON te.object_id = t.object_id
WHERE o.name = 'Orders'
-- Filter for triggers reacting to new rows
AND te.type_desc = 'INSERT'


'''
Instructions 4/4
25 XP

- Include the trigger definitions in your selection with the use of a standard SQL Server function.

'''

SELECT t.name AS TriggerName,
OBJECT_DEFINITION(t.parent_class_desc) AS TriggerDefinition
FROM sys.objects AS o
INNER JOIN sys.triggers AS t ON t.parent_id = o.object_id
INNER JOIN sys.trigger_events AS te ON te.object_id = t.object_id
WHERE o.name = 'Orders'
AND te.type_desc = 'INSERT'
