'''
Nesting TRY...CATCH constructs


You want to register a new buyer in your buyers table. This new buyer is Peter Thomson. His e-mail is peterthomson@mail.com and his phone number is 555000100.

In your database, there is also a table called errors, in which each error is stored.

You prepare a script that controls possible errors in the insertion of this person's data. It also inserts those errors into the errors table.

How do you prepare the script?

Instructions
100 XP

- Surround the INSERT INTO buyers statement with a TRY block.
- Surround the error handling with a CATCH block.
- Surround the INSERT INTO errors statement with another TRY block.
- Surround the nested error handling with another CATCH block.

'''
-- Set up the first TRY block
BEGIN TRY
	INSERT INTO buyers(first_name, last_name, email, phone)
		VALUES('Peter', 'Thompson', 'peterthomson@mail.com', '555000100');
END TRY
-- Set up the first CATCH block
BEGIN CATCH
	SELECT 'An error occurred inserting the buyer! You are in the first CATCH block';
    -- Set up the nested TRY block
    BEGIN TRY
    	INSERT INTO errors 
        	VALUES ('Error inserting a buyer');
        SELECT 'Error inserted correctly!';
	END TRY
    -- Set up the nested CATCH block
    BEGIN CATCH
    	SELECT 'An error occurred inserting the error! You are in the nested CATCH block';
    END CATCH 
END CATCH
