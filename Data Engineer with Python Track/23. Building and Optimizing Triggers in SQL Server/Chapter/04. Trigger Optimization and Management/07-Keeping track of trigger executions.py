'''
Keeping track of trigger executions


One important factor when monitoring triggers is to have a history of their execution. This allows you to associate the timings between trigger runs and any issues that occur in the database.

If the times match, it's possible that the problems were caused by the trigger.

SQL Server provides information about the execution of any triggers that are currently stored in memory in the sys.dm_exec_trigger_stats view. But once a trigger is removed from the memory, any information about it is removed from the view as well, so you lose the trigger execution history.

To overcome this limitation, you decide to make use of the TriggerAudit table to store information about any attempts to modify rows in the Orders table, because people have reported the table is often unresponsive.

Instructions
100 XP

- Modify the PreventOrdersUpdate trigger.
- Set the trigger to fire when rows are updated in the Orders table.
- Add additional details about the trigger execution into the TriggerAudit table.

'''
-- Modify the trigger to add new functionality
ALTER TRIGGER PreventOrdersUpdate
ON Orders
-- Prevent any row changes
INSTEAD OF UPDATE
AS
 -- Keep history of trigger executions
  INSERT INTO TriggerAudit(TriggerName, ExecutionDate)
   SELECT 'PreventOrdersUpdate',
      GETDATE()

    RAISERROR('Updates on "Orders" table are not permitted.
              Place a new order to add new products.', 16, 1)
