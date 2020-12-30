'''
How can I use a command's output as an input?


Suppose you want to get lines from the middle of a file. More specifically, suppose you want to get lines 3-5 from one of our data files. You can start by using head to get the first 5 lines and redirect that to a file, and then use tail to select the last 3:

    head -n 5 seasonal/winter.csv > top.csv
    tail -n 3 top.csv

A quick check confirms that this is lines 3-5 of our original file, because it is the last 3 lines of the first 5.

Instructions 1/2
50 XP

1. Select the last two lines from seasonal/winter.csv and save them in a file called bottom.csv.

Solution :

# Run the following command
tail -n 2 seasonal/winter.csv > bottom.csv

'''


'''
Instructions 2/2
50 XP

2. Select the first line from bottom.csv in order to get the second-to-last line of the original file.

Solution :

# Run the following command
head -n 1 bottom.csv
'''
