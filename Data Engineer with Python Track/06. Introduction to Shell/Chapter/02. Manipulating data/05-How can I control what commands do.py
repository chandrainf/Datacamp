'''
How can I control what commands do?


You won't always want to look at the first 10 lines of a file, so the shell lets you change head's behavior by giving it a command-line flag (or just "flag" for short). If you run the command:

head -n 3 seasonal/summer.csv
head will only display the first three lines of the file. If you run head -n 100, it will display the first 100 (assuming there are that many), and so on.

A flag's name usually indicates its purpose (for example, -n is meant to signal "number of lines"). Command flags don't have to be a - followed by a single letter, but it's a widely-used convention.

Note: it's considered good style to put all flags before any filenames, so in this course, we only accept answers that do that.

Instructions
100 XP

Display the first 5 lines of winter.csv in the seasonal directory.

Solution :

# Run the following command
head -n 5 seasonal/winter.csv
'''
