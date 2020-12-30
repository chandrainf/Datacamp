'''
Unifying flight formats II

In the previous exercise, you used CONCAT(), REPLICATE(), and LEN(). You got every register with more than 100 delays from the flight_statistics table. In a unique column, you concatenated the carrier_code, registration_code, and airport_code, having a similar format to this one: "AA - 0000119, JFK".

In this exercise, you will solve the same problem again, this time using the FORMAT() and CONCAT() functions together.

Instructions
100 XP

- Concatenate the carrier_code, formatted registration_code, and airport_code together using the appropriate function.
- Format the registration_code column while casting it as an integer.
- Filter registers with more than 100 delays.

'''
SELECT
-- Concat the strings
CONCAT(
    carrier_code,
    ' - ',
    -- Format the code
    FORMAT(CAST(registration_code AS INT), '0000000'),
    ', ',
    airport_code
) AS registration_code
FROM flight_statistics
-- Filter registers with more than 100 delays
WHERE delayed > 100
