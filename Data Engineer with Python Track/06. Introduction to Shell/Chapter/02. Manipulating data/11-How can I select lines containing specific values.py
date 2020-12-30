'''
How can I select lines containing specific values?


head and tail select rows, cut selects columns, and grep selects lines according to what they contain. In its simplest form, grep takes a piece of text followed by one or more filenames and prints all of the lines in those files that contain that text. For example, grep bicuspid seasonal/winter.csv prints lines from winter.csv that contain "bicuspid".

grep can search for patterns as well; we will explore those in the next course. What's more important right now is some of grep's more common flags:

    -c: print a count of matching lines rather than the lines themselves
    -h: do not print the names of files when searching multiple files
    -i: ignore case (e.g., treat "Regression" and "regression" as matches)
    -l: print the names of files that contain matches, not the matches
    -n: print line numbers for matching lines
    -v: invert the match, i.e., only show lines that don't match

Instructions 1/3
35 XP

1. Print the contents of all of the lines containing the word molar in seasonal/autumn.csv by running a single command while in your home directory. Don't use any flags.

Solution :

# Run the following command
grep molar seasonal/autumn.csv

'''


'''
Instructions 2/3
35 XP

2. Invert the match to find all of the lines that don't contain the word molar in seasonal/spring.csv, and show their line numbers. Remember, it's considered good style to put all of the flags before other values like filenames or the search term "molar".

Solution :

# Run the following command
grep -v -n molar seasonal/spring.csv

'''


'''
Instructions 3/3
35 XP

3. Count how many lines contain the word incisor in autumn.csv and winter.csv combined. (Again, run a single command from your home directory.)

Solution :

# Run the following command
grep -c incisor seasonal/autumn.csv seasonal/winter.csv

'''
