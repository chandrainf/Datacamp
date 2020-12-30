'''
Creating in-memory DataFrames


Creating small datasets for unit tests is an important skill. It improves readability and understanding, because any developer looking at your code, can immediately see the inputs to some function and how they relate to the output. Additionally, you can illustrate how the function behaves with normal data and with exceptional data, like missing or incorrect fields.

We have already instantiated a record object using the row() function, which in essential is just a row in our dataframe. You will use this row structure to add some records to our dataframe, which we can use to perform tests.

Instructions
100 XP

- Use the Record class, which has the 5 instance attributes given in the Row class constructor, to create a tuple of Row-like records, that will be assigned to the data variable.
- Use the createDataFrame() function to create a Spark DataFrame.

'''
from datetime import date
from pyspark.sql import Row

record = Row("country", "utm_campaign",
             "airtime_in_minutes", "start_date", "end_date")

# Create a tuple of records
data = (
    record("USA", "DiapersFirst", 28, date(2017, 1, 20), date(2017, 1, 27)),
    record("Germany", "WindelKind", 31, date(2017, 1, 25), None),
    record("India", "CloseToCloth", 32, date(2017, 1, 25), date(2017, 2, 2))
)

# Create a DataFrame from these records
frame = spark.createDataFrame(data)
frame.show()
