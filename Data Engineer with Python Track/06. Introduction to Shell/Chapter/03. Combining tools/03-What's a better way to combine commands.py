'''
What's a better way to combine commands?


Using redirection to combine commands has two drawbacks:

    1. It leaves a lot of intermediate files lying around (like top.csv).
    2. The commands to produce your final result are scattered across several lines of history.

The shell provides another tool that solves both of these problems at once called a pipe. Once again, start by running head:

    head -n 5 seasonal/summer.csv

Instead of sending head's output to a file, add a vertical bar and the tail command without a filename:

    head -n 5 seasonal/summer.csv | tail -n 3

The pipe symbol tells the shell to use the output of the command on the left as the input to the command on the right.

Instructions
100 XP

Use cut to select all of the tooth names from column 2 of the comma delimited file seasonal/summer.csv, then pipe the result to grep, with an inverted match, to exclude the header line containing the word "Tooth". cut and grep were covered in detail in Chapter 2, exercises 8 and 11 respectively.

Solution :

# Run the following command
cut -d , -f 2 seasonal/summer.csv | grep -v Tooth

'''
