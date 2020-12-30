'''
Tracking retired products


As shown in the example from the video, Fresh Fruit Delivery needs to keep track of any retired products in a dedicated history table (RetiredProducts).

You are asked to create a new trigger that fires when rows are removed from the Products table.

The information about the removed rows will be saved into the RetiredProducts table.

Instructions
100 XP

- Create the TrackRetiredProducts trigger on the Products table.
-Set the trigger to fire after rows are deleted from the table.

'''
-- Create the trigger
CREATE TRIGGER TrackRetiredProducts
ON Products
AFTER DELETE
AS
INSERT INTO RetiredProducts(Product, Measure)
SELECT Product, Measure
FROM deleted
