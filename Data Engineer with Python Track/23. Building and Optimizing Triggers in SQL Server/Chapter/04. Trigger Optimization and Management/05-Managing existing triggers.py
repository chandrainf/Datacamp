'''
Managing existing triggers


Fresh Fruit Delivery has asked you to act as the main administrator of their database.

A best practice when taking over an existing database is to get familiar with all the existing objects.

You'd like to start by looking at the existing triggers.

Instructions 1/3
35 XP

- Get the name, object_id, and parent_class_desc for all the disabled triggers.

'''
-- Get the disabled triggers
SELECT name,
object_id,
parent_class_desc
FROM sys.triggers
WHERE is_disabled = 1


'''
Instructions 2/3
35 XP

- Get the unmodified server-level triggers.
- An unmodified trigger's create date is the same as the modify date.

'''
-- Check for unchanged server triggers
SELECT *
FROM sys.server_triggers
WHERE create_date = modify_date


'''
Instructions 2/3
30 XP

- Use sys.triggers to extract information only about database-level triggers.

'''
-- Get the table triggers
SELECT *
FROM sys.triggers
WHERE parent_class_desc = 'DATABASE'
