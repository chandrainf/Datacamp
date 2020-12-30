'''
Shell pipelines to Bash scripts


In this exercise, you are working as a sports analyst for a Bulgarian soccer league. 
You have received some data on the results of the grand final from 1932 in a csv file. 
The file is comma-delimited in the format Year,Winner,Winner Goals which lists the year of the match, the team that won and how many goals the winning team scored, such as 1932,Arda,4.

Your job is to create a Bash script from a shell piped command which will aggregate to see how many times each team has won.

Don't worry about the tail -n +2 part, this just ensures we don't aggregate the CSV headers!

Instructions
100XP

- Create a single-line pipe to cat the file, cut out the relevant field and aggregate (sort & uniq -c will help!) based on winning team.
- Save your script and run from the console.

'''
#!/bin/bash

# Create a single-line pipe
cat soccer_scores.csv | cut - d "," - f 2 | tail - n + 2 | sort | uniq - c

# Now save and run!
