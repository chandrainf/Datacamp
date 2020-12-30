'''
Select multiple sheets


So far, you've read Excel files one sheet at a time, which lets you customize import arguments for each sheet. But if an Excel file has some sheets that you want loaded with the same parameters, you can get them in one go by passing a list of their names or indices to read_excel()'s sheet_name keyword. To get them all, pass None. You'll practice both methods to get data from fcc_survey.xlsx, which has multiple sheets of similarly-formatted data.

pandas has been loaded as pd.

Instructions 1/3
35 XP

Load both the 2016 and 2017 sheets by name with a list and one call to read_excel().

'''
# Load both the 2016 and 2017 sheets by name
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=['2016', '2017'])

# View the data type of all_survey_data
print(type(all_survey_data))


'''
Instructions 2/3
35 XP

Load the 2016 sheet by its position (0) and 2017 by name. Note the sheet names in the result.

'''
# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=[0, '2017'])

# View the sheet names in all_survey_data
print(all_survey_data.keys())


'''
Instructions 3/3
30 XP

Load all sheets in the Excel file without listing them all.

'''

# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=None)

# View the sheet names in all_survey_data
print(all_survey_data.keys())
