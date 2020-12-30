'''
Load a portion of a spreadsheet


Spreadsheets meant to be read by people often have multiple tables, e.g., a small business might keep an inventory workbook with tables for different product types on a single sheet. Even tabular data may have header rows of metadata, like the New Developer Survey data here. While the metadata is useful, we don't want it in a data frame. You'll use read_excel()'s skiprows keyword to get just the data. You'll also create a string to pass to usecols to get only columns AD and AW through BA, about future job goals.

pandas has been imported as pd.

Instructions
100 XP

- Create a single string, col_string, specifying that pandas should load column AD and the range AW through BA.
- Load fcc_survey_headers.xlsx', setting skiprows and usecols to skip the first two rows of metadata and get only the columns in col_string.
- View the selected column names in the resulting data frame.

'''

# Create string of lettered columns to load
col_string = "AD, AW:BA"

# Load data with skiprows and usecols set
survey_responses = pd.read_excel("fcc_survey_headers.xlsx",
                                 skiprows=2,
                                 usecols=col_string)

# View the names of the columns selected
print(survey_responses.columns)
