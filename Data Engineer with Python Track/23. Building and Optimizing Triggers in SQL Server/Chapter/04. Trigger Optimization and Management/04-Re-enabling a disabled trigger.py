'''
Re-enabling a disabled trigger


You helped the company update the Orders table by disabling the PreventOrdersUpdate trigger. Now they want the trigger to be active again to ensure no unwanted modifications are made to the table.

Instructions
100 XP

- Re-enable the disabled PreventOrdersUpdate trigger attached to the Orders table.

'''
-- Resume the trigger execution
ENABLE TRIGGER PreventOrdersUpdate
ON Orders
