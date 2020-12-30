'''
Analyzing baseball stats with .apply()


The Tampa Bay Rays want you to analyze their data.

They'd like the following metrics:

    - The sum of each column in the data
    - The total amount of runs scored in a year ('RS' + 'RA' for each year)
    - The 'Playoffs' column in text format rather than using 1's and 0's

The below function can be used to convert the 'Playoffs' column to text:

    def text_playoffs(num_playoffs): 
        if num_playoffs == 1:
            return 'Yes'
        else:
            return 'No' 

Use .apply() to get these metrics. A DataFrame (rays_df) has been loaded and printed to the console. This DataFrame is indexed on the 'Year' column.

Instructions 1/3
35 XP

Apply sum() to each column of rays_df to collect the sum of each column. Be sure to specify the correct axis.

'''
# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)


'''
Instructions 2/3
35 XP

Apply sum() to each row of rays_df, only looking at the 'RS' and 'RA' columns, and specify the correct axis.

'''
# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)


'''
Instructions 3/3
30 XP

Use .apply() and a lambda function to apply text_playoffs() to each row's 'Playoffs' value of the rays_df DataFrame.

'''
# Convert numeric playoffs to text
textual_playoffs = rays_df.apply(
    lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)
