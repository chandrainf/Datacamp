'''
Work with multiple spreadsheets


Workbooks meant primarily for human readers, not machines, may store data about a single subject across multiple sheets. For example, a file may have a different sheet of transactions for each region or year in which a business operated.

The FreeCodeCamp New Developer Survey file is set up similarly, with samples of responses from different years in different sheets. Your task here is to compile them in one data frame for analysis.

pandas has been imported as pd. All sheets have been read into the ordered dictionary responses, where sheet names are keys and data frames are values, so you can get data frames with the values() method.

Instructions
100 XP

- Create an empty data frame, all_responses.
- Set up a for loop to iterate through the values in the responses dictionary.
- Append each data frame to all_responses and reassign the result to the same variable name.

'''

# Create an empty data frame
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in responses.values():
    # Print the number of rows being added
    print("Adding {} rows".format(df.shape[0]))
    # Append df to all_responses, assign result
    all_responses = all_responses.append(df)

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()
