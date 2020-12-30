'''
Skip bad data


In this exercise you'll use read_csv() parameters to handle files with bad data, like records with more values than columns. By default, trying to import such files triggers a specific error, pandas.io.common.CParserError.

Some lines in the Vermont tax data here are corrupted. In order to load the good lines, we need to tell pandas to skip errors. We also want pandas to warn us when it skips a line so we know the scope of data issues.

pandas has been imported as pd. The exercise code will try to read the file. If there is a pandas.io.common.CParserError, the code in the except block will run.

Instructions 1/3
35 XP

Try to import the file vt_tax_data_2016_corrupt.csv without any keyword arguments.

'''
try:
    # Import the CSV without any keyword arguments
    data = pd.read_csv("vt_tax_data_2016_corrupt.csv")

    # View first 5 records
    print(data.head())

except pd.io.common.CParserError:
    print("Your data contained rows that could not be parsed.")


'''
Instructions 2/3
35 XP

Import vt_tax_data_2016_corrupt.csv with the error_bad_lines parameter set to skip bad records.

'''
try:
    # Import CSV with error_bad_lines set to skip bad records
    data = pd.read_csv("vt_tax_data_2016_corrupt.csv",
                       error_bad_lines=False)

    # View first 5 records
    print(data.head())

except pd.io.common.CParserError:
    print("Your data contained rows that could not be parsed.")


'''
Instructions 3/3
30 XP

Update the import with the warn_bad_lines parameter set to issue a warning whenever a bad record is skipped.

'''
try:
    # Set warn_bad_lines to issue warnings about bad records
    data = pd.read_csv("vt_tax_data_2016_corrupt.csv",
                       error_bad_lines=False,
                       warn_bad_lines=True)

    # View first 5 records
    print(data.head())

except pd.io.common.CParserError:
    print("Your data contained rows that could not be parsed.")
