'''
Removing unwanted triggers


After some time, the Fresh Fruit Delivery company notices that some of the triggers they requested are no longer needed. Their workflow has changed and not all of the triggers are used now.

It's a good practice to have your database clean and up-to-date. Unused objects should always be removed after proper confirmation from the involved parties.

The company calls to ask you to help them remove the unused triggers.

Instructions 1/3
35 XP

Remove the PreventNewDiscounts trigger attached to the Discounts table.

'''
-- Remove the trigger
DROP TRIGGER PreventNewDiscounts


'''
Instructions 2/3
35 XP

Remove the PreventTableDeletion trigger attached to the database.

'''
-- Remove the database trigger
DROP TRIGGER PreventTableDeletion
ON DATABASE


'''
Instructions 3/3
35 XP

Remove the DisallowLinkedServers trigger attached at the server level.

'''

-- Remove the server trigger
DROP TRIGGER DisallowLinkedServers
ON ALL SERVER
