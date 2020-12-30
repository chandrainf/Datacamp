'''
Using error functions


For every month, you want to know the total amount of money you earned in your bike store. Instead of reviewing every order line, you thought it would be better to prepare a script that computes it and displays the results.

While writing the script, you made a mistake. As you can see, the operation 'Total: ' + SUM(price * quantity) AS total is missing a cast conversion, causing an error.

How can we catch this error? Show the error number, severity, state, line, and message.

Instructions
100 XP

- Surround the operation with a TRY block.
- Surround the functions with a CATCH block.
- Select the error information

'''
-- Set up the TRY block
BEGIN TRY
SELECT 'Total: ' + SUM(price * quantity) AS total
FROM orders
END TRY
-- Set up the CATCH block
BEGIN CATCH
-- Show error information.
SELECT  ERROR_NUMBER() AS number,
ERROR_SEVERITY() AS severity_level,
ERROR_STATE() AS state,
ERROR_LINE() AS line,
ERROR_MESSAGE() AS message
END CATCH
