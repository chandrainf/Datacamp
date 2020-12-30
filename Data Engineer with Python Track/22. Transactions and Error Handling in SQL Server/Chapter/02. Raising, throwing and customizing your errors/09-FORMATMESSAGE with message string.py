'''
FORMATMESSAGE with message string


Every time you sell a bike in your store, you need to check if there is enough stock. You prepare a script to check it and throw an error if there is not enough stock.

Today, you sold 10 'Trek CrossRip+ - 2018' bikes, so you need to check if you can sell them.

Instructions
100 XP

- Save into the @current_stock variable the value of the stock of the product.
- Use the FORMATMESSAGE function with parameter placeholders (%s, %d, … ) to customize the error message. The message has to be 'There are not enough (the given product name) bikes. You only have (the stock of the product) in stock.'
- Pass to the THROW statement the variable of the custom message.

'''
DECLARE @product_name AS NVARCHAR(50) = 'Trek CrossRip+ - 2018'
DECLARE @number_of_sold_bikes AS INT = 10
DECLARE @current_stock INT
-- Select the current stock
SELECT @current_stock = stock FROM products WHERE product_name = @product_name
DECLARE @my_message NVARCHAR(500) =
-- Customize the message
CONCAT('There are not enough %s bikes. You only have %d in stock.', @product_name, @current_stock)

IF(@current_stock - @number_of_sold_bikes < 0)
-- Throw the error
THROW 50000, @my_message, 1
