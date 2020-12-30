'''
THROW without parameters


You want to prepare a stored procedure to insert new products in the database. In that stored procedure, you want to insert the possible errors in a table called errors, and after that, re-throw the original error.

How do you prepare the stored procedure?

Instructions
100 XP

- Surround the error handling with a CATCH block.
- Insert the error in the errors table.
- End the insert statement with a semicolon (;).
- Re-throw the original error.

'''
CREATE PROCEDURE insert_product
  @product_name VARCHAR(50),
  @stock INT,
  @price DECIMAL
AS

BEGIN TRY
	INSERT INTO products(product_name, stock, price)
		VALUES(@product_name, @stock, @price);
END TRY
-- Set up the CATCH block
BEGIN CATCH
	-- Insert the error and end the statement with a semicolon
    INSERT INTO errors VALUES ('Error inserting a product');
    -- Re-throw the error
	THROW; 
END CATCH
