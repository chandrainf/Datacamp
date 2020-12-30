'''
Anatomy review


When you execute the following script:

    INSERT INTO products (product_name, stock, price)
        VALUES ('Trek Powerfly 5 - 2018', 10, 3499.99);
        
The console of your SQL Server shows this:

    Msg 2627, Level 14, State 1, Line 1
    Violation of UNIQUE KEY constraint 'unique_name'. 
    Cannot insert duplicate key in object 'dbo.products'. 
    The duplicate key value is (Trek Powerfly 5 - 2018).

What are the different parts of the error you get, from left to right?

Answer the question
50XP

Possible Answers

    - Message level, severity level, state, line, and message text.

    - Error number, line, state, severity level, and message text.

    - Error number, severity level, state, line, and message text.

Answer : Error number, severity level, state, line, and message text.

'''
