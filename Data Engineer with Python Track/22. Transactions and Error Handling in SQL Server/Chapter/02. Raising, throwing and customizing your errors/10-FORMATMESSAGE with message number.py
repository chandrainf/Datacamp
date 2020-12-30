'''
FORMATMESSAGE with message number


Like in the previous exercise, you need to check if there is enough stock when you sell a product.

This time you want to add your custom error message to the sys.messages catalog, by executing the sp_addmessage stored procedure.

Instructions
100 XP

- Pass to the sp_addmessage stored procedure 50002 as the message id, 16 as the severity, and 'There are not enough %s bikes. You only have %d in stock.' as the message text.
- Use FORMATMESSAGE, setting the first parameter (message number) to be 50002. Complete the second and the third parameters to replace the parameter placeholders of the message (%s and %d) with the appropriate variables.
- Pass to the THROW statement the custom message.

'''
-- Pass the variables to the stored procedure
EXEC sp_addmessage @msgnum = 50002, @severity = 16,


@msgtext = 'There are not enough %s bikes. You only have %d in stock.',
@lang = N'us_english'
DECLARE @product_name AS NVARCHAR(50) = 'Trek CrossRip+ - 2018'
DECLARE @number_of_sold_bikes AS INT = 10
DECLARE @current_stock INT
SELECT @current_stock = stock FROM products WHERE product_name = @product_name
DECLARE @my_message NVARCHAR(500) =
-- Prepare the error message
FORMATMESSAGE(50002, @product_name, @current_stock)

IF(@current_stock - @number_of_sold_bikes < 0)
-- Throw the error
THROW 50000, @my_message, 1
