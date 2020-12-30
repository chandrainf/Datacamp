'''
Iterating with .iterrows()


In the video, we discussed that .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs. But, what does this mean? Let's explore with a few coding exercises.

A pandas DataFrame has been loaded into your session called pit_df. This DataFrame contains the stats for the Major League Baseball team named the Pittsburgh Pirates (abbreviated as 'PIT') from the year 2008 to the year 2012. It has been printed into your console for convenience.

Instructions 1/4
25 XP

Use .iterrows() to loop over pit_df and print each row. Save the first item from .iterrows() as i and the second as row.

'''
# Iterate over pit_df and print each row
for i, row in pit_df.iterrows():
    print(row)


'''
Instructions 2/4
25 XP

Add two lines to the loop: one before print(row) to print each index variable and one after to print each row's type.

'''
# Iterate over pit_df and print each index variable and then each row
for i, row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row))


'''
Instructions 3/4
25 XP

Instead of using i and row in the for statement to store the output of .iterrows(), use one variable named row_tuple.

'''
# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)


'''
Instructions 4/4
25 XP

Add a line in the for loop to print the type of each row_tuple.
'''
# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))
