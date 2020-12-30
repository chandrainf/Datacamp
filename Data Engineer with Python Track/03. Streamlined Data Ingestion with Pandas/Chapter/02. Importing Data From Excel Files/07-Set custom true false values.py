'''
Set custom true/false values


In Boolean columns, pandas automatically recognizes certain values, like "TRUE" and 1, as True, and others, like "FALSE" and 0, as False. Some datasets, like survey data, can use unrecognized values, such as "Yes" and "No".

For practice purposes, some Boolean columns in the New Developer Survey have been coded this way. You'll make sure they're properly interpreted with the help of the true_values and false_values arguments.

pandas is loaded as pd. You can assume the columns you are working with have no missing values.

Instructions
100 XP

- Load the Excel file, specifying "Yes" as a true value and "No" as a false value.

'''

# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel("fcc_survey_yn_data.xlsx",
                              dtype={"HasDebt": bool,
                                     "AttendedBootCampYesNo": bool},
                              true_values=["Yes"],
                              false_values=["No"])

# View the data
print(survey_subset.head())
