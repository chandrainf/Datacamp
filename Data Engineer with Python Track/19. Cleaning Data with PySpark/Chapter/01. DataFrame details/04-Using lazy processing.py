'''
Using lazy processing


Lazy processing operations will usually return in about the same amount of time regardless of the actual quantity of data. Remember that this is due to Spark not performing any transformations until an action is requested.

For this exercise, we'll be defining a Data Frame (aa_dfw_df) and add a couple transformations. Note the amount of time required for the transformations to complete when defined vs when the data is actually queried. These differences may be short, but they will be noticeable. When working with a full Spark cluster with larger quantities of data the difference will be more apparent.

Instructions
100 XP

- Load the Data Frame.
- Add the transformation for F.lower() to the Destination Airport column.
- Drop the Destination Airport column from the Data Frame aa_dfw_df. Note the time for these operations to complete.
- Show the Data Frame, noting the time difference for this action to complete.

'''
# Load the CSV file
aa_dfw_df = spark.read.format('csv').options(
    Header=True).load('AA_DFW_2018.csv.gz')

# Add the airport column using the F.lower() method
aa_dfw_df = aa_dfw_df.withColumn(
    'airport', F.lower(aa_dfw_df['Destination Airport']))

# Drop the Destination Airport column
aa_dfw_df = aa_dfw_df.drop(aa_dfw_df['Destination Airport'])

# Show the DataFrame
aa_dfw_df.show()
