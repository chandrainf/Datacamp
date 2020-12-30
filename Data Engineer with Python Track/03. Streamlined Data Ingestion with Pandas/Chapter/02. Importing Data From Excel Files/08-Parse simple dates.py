'''
Parse simple dates

pandas does not infer that columns contain datetime data; it interprets them as object or string data unless told otherwise. Correctly modeling datetimes is easy when they are in a standard format -- we can use the parse_dates argument to tell read_excel() to read columns as datetime data.

The New Developer Survey responses contain some columns with easy-to-parse timestamps. In this exercise, you'll make sure they're the right data type.

pandas has been loaded as pd.

Instructions
100 XP

- Load fcc_survey.xlsx, making sure that the Part1StartTime column is parsed as datetime data.
- View the first few values of the survey_data.Part1StartTime to make sure it contains datetimes.

'''
# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("fcc_survey.xlsx",
                            parse_dates=["Part1StartTime"])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())
