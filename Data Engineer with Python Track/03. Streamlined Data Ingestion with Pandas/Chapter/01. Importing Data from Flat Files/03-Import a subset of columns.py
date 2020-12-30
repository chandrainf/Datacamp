'''
Import a subset of columns


The Vermont tax data contains 147 columns describing household composition, income sources, and taxes paid by ZIP code and income group. Most analyses don't need all these columns. In this exercise, you will create a data frame with fewer variables using read_csv()s usecols argument.

Let's focus on household composition to see if there are differences by geography and income level. To do this, we'll need columns on income group, ZIP code, tax return filing status (e.g., single or married), and dependents. The data uses codes for variable names, so the specific columns needed are in the instructions.

pandas has already been imported as pd.

Instructions
100 XP

- Create a list of columns to use: zipcode, agi_stub (income group), mars1 (number of single households), MARS2 (number of households filing as married), and NUMDEP (number of dependents).
- Create a data frame from vt_tax_data_2016.csv that uses only the selected columns.

'''
# Create list of columns to use
cols = ["zipcode", "agi_stub", "mars1", "MARS2", "NUMDEP"]

# Create data frame from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols=cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())
