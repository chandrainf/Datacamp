'''
Using error functions in a nested TRY...CATCH


You received some new electric bikes in your store, so you need to update the stock.

You want to register that you received 2 Trek Powerfly 5 - 2018 bikes with a price of $3499.99 each, and 3 New Power K- 2018 bikes at $1999.99 each.

You try to insert the products in the database because you think they are new models. However, you forgot you already have the first one in stock. Luckily, the products table has a constraint requiring every product name to be unique.

You prepare a script controlling possible errors in the insertions. You also want to insert possible errors in a table called errors, and, if something fails when inserting the error, show the error number and error message.

Instructions
100 XP

- Surround the error handling with a CATCH block.
- Insert 'Error inserting a product' in the errors table and surround this insertion with another TRY block.
- Surround the nested error handling with another CATCH block.
- Select the error line and the error message in the inner CATCH block.

'''
BEGIN TRY
    INSERT INTO products(product_name, stock, price)
    VALUES('Trek Powerfly 5 - 2018', 2, 3499.99),
    		('New Power K- 2018', 3, 1999.99)
END TRY
-- Set up the outer CATCH block
BEGIN CATCH
	SELECT 'An error occurred inserting the product!';
    -- Set up the inner TRY block
    BEGIN TRY
    	-- Insert the error
    	INSERT INTO errors 
        	VALUES ('Error inserting a product');
    END TRY    
    -- Set up the inner CATCH block
    BEGIN CATCH
    	-- Show number and message error
    	SELECT 
        	ERROR_LINE() AS line,
			ERROR_MESSAGE() AS message; 
    END CATCH    
END CATCH
