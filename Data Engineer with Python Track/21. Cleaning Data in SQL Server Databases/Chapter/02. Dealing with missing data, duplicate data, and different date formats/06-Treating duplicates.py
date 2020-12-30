'''
Treating duplicates


In the previous exercise, you reviewed the concept of ROW_NUMBER(). In this exercise, you will use it in your code.

You want to select all the rows from the flight_statistics table that are duplicated. After that, you want to get all the rows without duplicates. You consider that the repeating group for this table is formed by the columns airport_code, carrier_code, and registration_date.

Instructions 1/3
35 XP

- First of all, apply the ROW_NUMBER() function to the flight_statistics table.
- Consider that partitions will be formed by the columns airport_code, carrier_code, and registration_date.

'''
SELECT *,
	   -- Apply ROW_NUMBER()
       ROW_NUMBER() OVER (
         	-- Write the partition
            PARTITION BY 
                airport_code, 
                carrier_code, 
                registration_date
			ORDER BY 
                airport_code, 
                carrier_code, 
                registration_date
        ) row_num
FROM flight_statistics

'''
Instructions 2/3
35 XP

- Wrap the previous query with the WITH clause to select the duplicate rows.
- Get just the duplicate rows comparing row_num with a number.

'''
-- Use the WITH clause
WITH cte AS (
    SELECT *, 
        ROW_NUMBER() OVER (
            PARTITION BY 
                airport_code, 
                carrier_code, 
                registration_date
			ORDER BY 
                airport_code, 
                carrier_code, 
                registration_date
        ) row_num
    FROM flight_statistics
)
SELECT * FROM cte
-- Get only duplicates
WHERE row_num > 1;


'''
Instructions 3/3
30 XP

- Modify the previous query to exclude the duplicate rows by comparing row_num with a number.

'''
WITH cte AS (
    SELECT *, 
        ROW_NUMBER() OVER (
            PARTITION BY 
                airport_code, 
                carrier_code, 
                registration_date
			ORDER BY 
                airport_code, 
                carrier_code, 
                registration_date
        ) row_num
    FROM flight_statistics
)
SELECT * FROM cte
-- Exclude duplicates
WHERE row_num = 1;
