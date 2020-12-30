'''
Filling missing values using ISNULL()


In the previous exercise, you practiced how to exclude and select the rows with NULL values. However, depending on the business assumptions behind your data, you may want to select all the rows with NULL values, but replacing these NULL values with another value. You can do it using ISNULL().

Now, you want to replace all the NULL values for the airport_city and airport_state columns with the word 'Unknown', using ISNULL().

Instructions
100 XP

- Replace the missing values for airport_city column with the 'Unknown' string.
- Replace the missing values for airport_state column with the 'Unknown' string.

'''
SELECT
  airport_code,
  airport_name,
  -- Replace missing values for airport_city with 'Unknown'
  ISNULL(airport_city, 'Unknown') AS airport_city,
  -- Replace missing values for airport_state with 'Unknown'
  ISNULL(airport_state, 'Unknown') AS airport_state
FROM airports