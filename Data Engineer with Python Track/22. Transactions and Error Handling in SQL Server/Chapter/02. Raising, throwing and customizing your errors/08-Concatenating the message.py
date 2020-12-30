'''
Concatenating the message


You need to prepare a script to select all the information about the members from the staff table using a given first_name.

If the select statement doesn't find any member, you want to throw an error using the THROW statement. You need to warn there is no staff member with such a name.

Instructions
100 XP

- Set the @first_name variable to 'Pedro'.
- Assign to the @my_message variable the concatenation of the text 'There is no staff member with ', with the value of the @first_name variable and with the text ' as the first name.'.
- Use the THROW statement with 50000 as the error number, @my_message variable as the message parameter, and 1 as the state.

'''
-- Set @first_name to 'Pedro'
DECLARE @first_name NVARCHAR(20) = 'Pedro'

-- Concat the message
DECLARE @my_message NVARCHAR(500) =
CONCAT('There is no staff member with ', @first_name, ' as the first name.')

IF NOT EXISTS(SELECT * FROM staff WHERE first_name=@first_name)
-- Throw the error
THROW 50000, @my_message, 1
