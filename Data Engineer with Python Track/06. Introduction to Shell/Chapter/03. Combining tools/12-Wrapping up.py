'''
Wrapping up


To wrap up, you will build a pipeline to find out how many records are in the shortest of the seasonal data files.

Instructions 1/3
35 XP

1. Use wc with appropriate parameters to list the number of lines in all of the seasonal data files. (Use a wildcard for the filenames instead of typing them all in by hand.)

Solution :

# Run the following command
wc -l seasonal/*.csv

'''


'''
Instructions 2/3
35 XP

2. Add another command to the previous one using a pipe to remove the line containing the word "total".

Solution :

# Run the following command
wc -l seasonal/*.csv | grep -v total

'''


'''
Instructions 3/3
30 XP

3. Add two more stages to the pipeline that use sort -n and head -n 1 to find the file containing the fewest lines.

Solution :

# Run the following command
wc -l seasonal/*.csv | grep -v total | sort -n | head -n 1
'''
