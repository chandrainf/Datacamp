'''
Using FORMAT()


Unlike the CONVERT() function, the FORMAT() function takes in the format as a string as such 'dd/MM/yyyy'.

You need to get a report of all the pilots. You realize that the format of the entry_date column is 'yyyy-MM-dd', and you want to show the results in the format of 'dd/MM/yyyy'. As this table contains few data, you think about using the FORMAT() function.

Notice that the type of the entry_date column is VARCHAR(10) and not a date.

Instructions
100 XP

- Convert the type of the entry_date column to DATE and print it in 'dd/MM/yyyy' format.

'''
SELECT
	pilot_code,
	pilot_name,
	pilot_surname,
	carrier_code,
    -- Convert the entry_date to a DATE and print it in dd/MM/yyyy format
	FORMAT(CAST(entry_date AS DATE), 'dd/MM/yyyy') AS entry_date
from pilots
