'''
The TrackRetiredProducts trigger in action


Once you've created a trigger, it's always a good idea to see if it performs as expected.

The company's request for the trigger created earlier was based on a real need: they want to retire several products from their offering. This means you can check the trigger in action.

Instructions
100 XP

Remove retired items from the Products table and check the output from the RetiredProducts table.

'''
-- Remove the products that will be retired
DELETE FROM Products
WHERE Product IN('Cloudberry', 'Guava', 'Nance', 'Yuzu')

-- Verify the output of the history table
SELECT * FROM RetiredProducts
