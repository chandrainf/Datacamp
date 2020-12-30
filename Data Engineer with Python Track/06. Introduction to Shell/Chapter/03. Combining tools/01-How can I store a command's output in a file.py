'''
How can I store a command's output in a file?


All of the tools you have seen so far let you name input files. Most don't have an option for naming an output file because they don't need one. Instead, you can use redirection to save any command's output anywhere you want. If you run this command:

    head -n 5 seasonal/summer.csv

it prints the first 5 lines of the summer data on the screen. If you run this command instead:

    head -n 5 seasonal/summer.csv > top.csv

nothing appears on the screen. Instead, head's output is put in a new file called top.csv. You can take a look at that file's contents using cat:

    cat top.csv

The greater-than sign > tells the shell to redirect head's output to a file. It isn't part of the head command; instead, it works with every shell command that produces output.

Instructions
100 XP

- Combine tail with redirection to save the last 5 lines of seasonal/winter.csv in a file called last.csv.

Solution :

# Run the following command
tail -n 5 seasonal/winter.csv > last.csv

'''
