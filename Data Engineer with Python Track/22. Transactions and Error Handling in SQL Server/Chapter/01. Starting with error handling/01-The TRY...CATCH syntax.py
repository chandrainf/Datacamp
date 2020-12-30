'''
The TRY...CATCH syntax


You want to insert a new product in your products table. You prepare this script, trying to control the execution if an error occurs. You use the TRY...CATCH construct you learned to handle the possible errors.

    BEGIN TRY
        INSERT INTO products (product_name, stock, price)
            VALUES ('Trek Powerfly 5 - 2018', 10, 3499.99);
        SELECT 'Product inserted correctly!';

        BEGIN CATCH
            SELECT 'An error occurred! You are in the CATCH block';   
        END CATCH
    END TRY

Which of the following is true about the syntax?

Answer the question
50XP

Possible Answers

    - This script is correct because the error is handled within the CATCH block, and everything must be enclosed by the TRY block.

    - This script isn't correct because the CATCH block must start after the end of the TRY block.
    
    - This script isn't correct because the error should be handled in the TRY block.

Answer : This script isn't correct because the CATCH block must start after the end of the TRY block.

'''
