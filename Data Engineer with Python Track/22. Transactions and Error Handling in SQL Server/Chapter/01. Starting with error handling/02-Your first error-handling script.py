'''
Your first error-handling script


You realized your products table doesn't have any constraint to check the data stored in its stock column. It makes sense that stock is always greater than or equal to 0. For some reason, there is a mistake in the following row. The stock is -1!

    | product_id | product_name | stock | price |
    |------------|--------------|-------|-------|
    | 6          | Trek Neko+   | -1    | 2799  |

You want to prepare a script adding a constraint to the products table, so that only stocks greater than or equal to 0 are allowed.

If you add this constraint that only allows stocks greater than or equal to 0, the execution will fail because there is one row where the stock equals -1.

How can you prepare the script?

Instructions
100 XP

- Surround the constraint with a TRY block.
- Add the constraint to the products table.
- Surround the error message with a CATCH block.

'''
-- Set up the TRY block
BEGIN TRY
-- Add the constraint
ALTER TABLE products
ADD CONSTRAINT CHK_Stock CHECK(stock >= 0)
END TRY
-- Set up the CATCH block
BEGIN CATCH
SELECT 'An error occurred!'
END CATCH
