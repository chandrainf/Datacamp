'''
How can I look at the start of a file?


The first thing most data scientists do when given a new dataset to analyze is figure out what fields it contains and what values those fields have. If the dataset has been exported from a database or spreadsheet, it will often be stored as comma-separated values (CSV). A quick way to figure out what it contains is to look at the first few rows.

We can do this in the shell using a command called head. As its name suggests, it prints the first few lines of a file (where "a few" means 10), so the command:

    head seasonal/summer.csv

displays:

    Date,Tooth
    2017-01-11,canine
    2017-01-18,wisdom
    2017-01-21,bicuspid
    2017-02-02,molar
    2017-02-27,wisdom
    2017-02-27,wisdom
    2017-03-07,bicuspid
    2017-03-15,wisdom
    2017-03-20,canine

What does head do if there aren't 10 lines in the file? (To find out, use it to look at the top of people/agarwal.txt.)

Instructions
50 XP

Possible Answers

    - Print an error message because the file is too short.

    - Display as many lines as there are.

    - Display enough blank lines to bring the total to 10.

Answer : Display as many lines as there are.

'''
