'''
Using CONVERT()


The CONVERT() function can help you to convert dates into the desired format.

You need to get a report of the airports, carriers, canceled flights, and registration dates, registered in the first semester of the year 2014. You realize that the format of the registration_date column is yyyy-mm-dd, and you want to show the results in the format of mm/dd/yyyy, which is hardcoded as 101, using the CONVERT() function.

Notice that the type of the registration_date column is VARCHAR(10) and not a date.

Instructions
100 XP

- Convert the type of the registration_date column to DATE and print it in mm/dd/yyyy format.
- Convert the registration_date column to mm/dd/yyyy format to filter the results.
- Filter the results for the first semester of 2014 in mm/dd/yyyy format.

'''
SELECT
airport_code,
carrier_code,
canceled,
airport_code,
-- Convert the registration_date to a DATE and print it in mm/dd/yyyy format
CONVERT(VARCHAR(10), CAST(registration_date AS DATE), 101) AS registration_date
FROM flight_statistics
-- Convert the registration_date to mm/dd/yyyy format
WHERE CONVERT(VARCHAR(10), CAST(registration_date AS DATE), 101)
-- Filter the first semester of 2014 in mm/dd/yyyy format
BETWEEN '01/01/2014' AND '06/30/2014'
