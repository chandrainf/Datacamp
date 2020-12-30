'''
Keeping a history of row changes


The Fresh Fruit Delivery company needs to track changes made to the Customers table.

You are asked to create a new trigger that covers any statements modifying rows in the table.

Instructions
100 XP

- Create a new trigger called CopyCustomersToHistory.
- Attach the trigger to the Customers table.
- Fire the trigger when rows are added or modified.
- Extract the information from the inserted special table.

'''
-- Create a trigger to keep row history
CREATE TRIGGER CopyCustomersToHistory
ON Customers
-- Fire the trigger for new and updated rows
AFTER INSERT, UPDATE
AS
	INSERT INTO CustomersHistory(CustomerID, Customer, ContractID, ContractDate, Address, PhoneNo, Email, ChangeDate)
	SELECT CustomerID, Customer, ContractID, ContractDate, Address, PhoneNo, Email, GETDATE()
    -- Get info from the special table that keeps new rows
    FROM inserted
