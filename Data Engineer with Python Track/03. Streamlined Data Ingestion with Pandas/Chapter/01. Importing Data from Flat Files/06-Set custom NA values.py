'''
Set custom NA values


Part of data exploration and cleaning consists of checking for missing or NA values and deciding how to account for them. This is easier when missing values are treated as their own data type. and there are pandas functions that specifically target such NA values. pandas automatically treats some values as missing, but we can pass additional NA indicators with the na_values argument. Here, you'll do this to ensure that invalid ZIP codes in the Vermont tax data are coded as NA.

pandas has been imported as pd.

Instructions
100 XP

- Create a dictionary, null_values, specifying that 0s in the zipcode column should be considered NA values.
- Load vt_tax_data_2016.csv, using the na_values argument and the dictionary to make sure invalid ZIP codes are treated as missing.

'''
# Create dict specifying that 0s in zipcode are NA values
null_values = {"zipcode": 0}

# Load csv using na_values keyword argument
data = pd.read_csv("vt_tax_data_2016.csv",
                   na_values=null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])
