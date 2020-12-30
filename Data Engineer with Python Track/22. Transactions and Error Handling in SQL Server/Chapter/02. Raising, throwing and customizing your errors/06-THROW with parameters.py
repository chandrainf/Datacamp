'''
THROW with parameters


You need to prepare a script to select all the information of a member from the staff table using a given staff_id.

If the select statement doesn't find any member, you want to throw an error using the THROW statement. You need to warn there is no staff member with such id.

Instructions
100 XP

- Set @staff_id to 4.
- Use the THROW statement, with 50001 as the error number, 'No staff member with such id' as the message text, and 1 as the state.

'''
-- Set @staff_id to 4
DECLARE @staff_id INT = 4

IF NOT EXISTS(SELECT * FROM staff WHERE staff_id=@staff_id)
-- Invoke the THROW statement with parameters
THROW 50001, 'No staff member with such id', 1
ELSE
SELECT * FROM staff WHERE staff_id = @staff_id
