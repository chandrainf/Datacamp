'''
Get data from a spreadsheet


In this exercise, you'll create a data frame from a "base case" Excel file: one with a single sheet of tabular data. The fcc_survey.xlsx file here has a sample of responses from FreeCodeCamp's annual New Developer Survey. This survey asks participants about their demographics, education, work and home life, plus questions about how they're learning to code. Let's load all of it.

pandas has not been pre-loaded in this exercise, so you'll need to import it yourself before using read_excel() to load the spreadsheet.

Instructions
100 XP

- Load the pandas library as pd.
- Read in fcc_survey.xlsx and assign it to the variable survey_responses.
- Print the first few records of survey_responses.

'''

# Load pandas as pd
import pandas as pd

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel('fcc_survey.xlsx')

# View the head of the data frame
print(survey_responses.head())
