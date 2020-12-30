'''
Import a file in chunks


When working with large files, it can be easier to load and process the data in pieces. Let's practice this workflow on the Vermont tax data.

The first 500 rows have been loaded as vt_data_first500. You'll get the next 500 rows. To do this, you'll employ several keyword arguments: nrows and skiprows to get the correct records, header to tell pandas the data does not have column names, and names to supply the missing column names. You'll also want to use the list() function to get column names from vt_data_first500 to reuse.

pandas has been imported as pd.

Instructions
100 XP

- Use nrows and skiprows to make a data frame, vt_data_next500, with the next 500 rows.
- Set the header argument so that pandas knows there is no header row.
- Name the columns in vt_data_next500 by supplying a list of vt_data_first500's columns to the names argument.

'''
# Create data frame of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv",
                              nrows=500,
                              skiprows=500,
                              header=None,
                              names=list(vt_data_first500))

# View the Vermont data frames to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())
