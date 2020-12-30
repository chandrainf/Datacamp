'''
Diagnosing duplicates


In this lesson, you learned how to use the ROW_NUMBER() function. ROW_NUMBER() returns a number which begins at 1 for the first row in every partition, and provides a sequential number for each row within the same partition.

Considering that the partition for the statistics_flight table is formed by the columns airport_code, carrier_code, and registration_date, can you guess what value will give the ROW_NUMBER() function in the row_num column for the last row?

    |registration_code|airport_code|carrier_code|registration_date|canceled|on_time| statistician_name|statistician_surname|row_num|
    |-----------------|------------|------------|-----------------|--------|-------|------------------|--------------------|-------|
    |000000137        |MSP         |EV          |2014-01-01       |117     |369    | Michael          |Andersen            |1      |
    |000000138        |MSP         |F9          |2014-01-01       |0       |60     | Anne             |Johnson             |1      |
    |000000139        |MSP         |FL          |2014-01-01       |8       |83     | Anne             |Johnson             |1      |
    |000000140        |MSP         |MQ          |2014-01-01       |20      |67     | Anne             |Johnson             |1      |
    |000000141        |MSP         |OO          |2014-01-01       |76      |1031   | Anne             |Johnson             |1      |
    |000000142        |MSP         |OO          |2014-01-01       |76      |1031   | Anne             |Johnson             |2      |
    |000000143        |MSP         |OO          |2014-01-01       |76      |1031   | Anne             |Johnson             |???????|

Answer the question
50XP

Possible Answers

    - 1

    - 2

    - 3

Answer : 3

'''
