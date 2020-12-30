'''
Unifying flight formats I


Cleaning data is important because frequently, you may acquire messy data that is not ready for analysis.

In this exercise, you need to get every register with more than 100 delays from the flight_statistics table. In a unique column, you have to concatenate the carrier_code, registration_code, and airport_code, having a similar format to this one: "AA - 000000119, JFK".

When analyzing the flight_statistics table, you realize that some registration_code values have different formats. A correct registration_code must have nine digits, and if it has fewer, you need to complete it with leading zeros.

To do this, you can use the REPLICATE() function in combination with LEN() and CONCAT().

Instructions
100 XP

- Use the appropriate function to concatenate the carrier_code, the leading zeros before a registration code, the registration_code, and airport_code columns.
- Replicate as many zeros as needed by subtracting 9 from the length of each registration_code.
- Filter the registers where the delayed column is more than 100.

'''
SELECT
-- Concat the strings
CONCAT(
    carrier_code,
    ' - ',
    -- Replicate zeros
    REPLICATE('0', 9 - LEN(registration_code)),
    registration_code,
    ', ',
    airport_code)
AS registration_code
FROM flight_statistics
-- Filter registers with more than 100 delays
WHERE delayed > 100
