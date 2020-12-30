'''
Sensible data types


Let’s take a look at the following dataset of purchases, where each record contains demographic data about a person and whether or not this person has bought a certain product.

  Country	  Age	  Salary	Purchased
  Spain	    30	  53000	  No
  France	  28	  48000	  Yes
  Spain	    44	  71000	  No
  Germany	  37	  63000	  No

The schema has been defined as follows. Do you see any data type that has been defined incorrectly?

  schema = StructType([
    StructField("Country", StringType(), nullable=False),
    StructField("Age", ByteType(), nullable=False),
    StructField("Salary", ByteType(), nullable=True),
    StructField("Purchased", StringType(), nullable=True)
  ])

Answer the question
50XP

Possible Answers :

    - Age should be IntegerType().

    - Salary should be CurrencyType().

    - Salary should be IntegerType().

    - Purchased should be ByteType().

Answer : Salary should be IntegerType().

'''
