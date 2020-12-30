'''
Correcting compilation errors


Today, your colleague Bernard has to leave work early. He was preparing a script to insert a new product into the products table, but he couldn't finish it. He asks you for help and gives you the script to finish it.

He wants to insert the 'Sun Bicycles ElectroLite - 2017', with a stock of 10 units and a price of $1559.99. He also wants to insert possible errors in a table called errors. In fact, if you try to insert this bicycle, you will get an error because there is already another product with the same name.

When you execute the script, you realize there are several compilation errors.

Can you correct Bernard's script? The final output must be: An error occurred inserting the product!

Instructions
100 XP

Note: Error messages in DataCamp have different anatomy than in SQL Server, but as they show the error message, you won't have any problem.

- Run the code to verify there are compilation errors.
- Correct every compilation error.
- Run the code to get the final output: An error occurred inserting the product!

'''
BEGIN TRY
	INSERT INTO products(product_name, stock, price)
		VALUES('Sun Bicycles ElectroLite - 2017', 10, 1559.99);
END TRY
BEGIN CATCH
	SELECT 'An error occurred inserting the product!';
    BEGIN TRY
    	INSERT INTO errors
        	VALUES ('Error inserting a product');
    END TRY    
    BEGIN CATCH
    	SELECT 'An error occurred inserting the error!';
    END CATCH    
END CATCH
