'''
Executing a stored procedure that throws an error


You need to insert a new product using the stored procedure you created in the previous exercise:

    CREATE PROCEDURE insert_product
    @product_name VARCHAR(50),
    @stock INT,
    @price DECIMAL

    AS

    BEGIN TRY
        INSERT INTO products (product_name, stock, price)
            VALUES (@product_name, @stock, @price);
    END TRY
    BEGIN CATCH    
        INSERT INTO errors VALUES ('Error inserting a product');  
        THROW;  
    END CATCH

You want to register that you received 3 Super bike bikes with a price of $499.99. You need to catch the possible errors generated in the execution of the stored procedure, showing the original error message.

How do you prepare the script?

Instructions
100 XP

- Execute the stored procedure called insert_product.
- Set the appropriate values for the parameters of the stored procedure.
- Surround the error handling with a CATCH block.
- Select the error message.

'''
BEGIN TRY
	-- Execute the stored procedure
	EXEC insert_product
    	-- Set the values for the parameters
    	@product_name = 'Super bike',
        @stock = 3,
        @price = 499.99;
END TRY
-- Set up the CATCH block
BEGIN CATCH
	-- Select the error message
	SELECT ERROR_MESSAGE();
END CATCH