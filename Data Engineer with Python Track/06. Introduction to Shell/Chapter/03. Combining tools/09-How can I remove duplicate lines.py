'''
How can I remove duplicate lines?


Another command that is often used with sort is uniq, whose job is to remove duplicated lines. More specifically, it removes adjacent duplicated lines. If a file contains:

    2017-07-03
    2017-07-03
    2017-08-03
    2017-08-03

then uniq will produce:

    2017-07-03
    2017-08-03

but if it contains:

    2017-07-03
    2017-08-03
    2017-07-03
    2017-08-03

then uniq will print all four lines. The reason is that uniq is built to work with very large files. In order to remove non-adjacent lines from a file, it would have to keep the whole file in memory (or at least, all the unique lines seen so far). By only removing adjacent duplicates, it only has to keep the most recent unique line in memory.

Instructions
100 XP

Write a pipeline to:

- get the second column from seasonal/winter.csv,
- remove the word "Tooth" from the output so that only tooth names are displayed,
- sort the output so that all occurrences of a particular tooth name are adjacent; and
- display each tooth name once along with a count of how often it occurs.

The start of your pipeline is the same as the previous exercise:

    cut -d , -f 2 seasonal/winter.csv | grep -v Tooth

Extend it with a sort command, and use uniq -c to display unique lines with a count of how often each occurs rather than using uniq and wc.

Solution :

# Run the following command
cut -d , -f 2 seasonal/winter.csv | grep -v Tooth | sort | uniq -c

'''
