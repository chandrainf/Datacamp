'''
How can one shell script do many things?


Our shells scripts so far have had a single command or pipe, but a script can contain many lines of commands. For example, you can create one that tells you how many records are in the shortest and longest of your data files, i.e., the range of your datasets' lengths.

Note that in Nano, "copy and paste" is achieved by navigating to the line you want to copy, pressing CTRL + K to cut the line, then CTRL + U twice to paste two copies of it.

As a reminder, to save what you have written in Nano, type Ctrl + O to write the file out, then Enter to confirm the filename, then Ctrl + X to exit the editor.

Instructions 1/4
25 XP

Use Nano to edit the script range.sh and replace the two ____ placeholders with $@ and -v so that it lists the names and number of lines in all of the files given on the command line without showing the total number of lines in all files. (Do not try to subtract the column header lines from the files.)

# This solution uses `cp` instead of `nano`
# because our automated tests can't edit files interactively.
# Run the following command
cp /solutions/range-1.sh range.sh

'''


'''
Instructions 2/4
25 XP

Use Nano again to add sort -n and head -n 1 in that order to the pipeline in range.sh to display the name and line count of the shortest file given to it.


Solution :

# This solution uses `cp` instead of `nano`
# because our automated tests can't edit files interactively.
# Run the following command
cp /solutions/range-2.sh range.sh

'''


'''
Instructions 3/4
25 XP

Again using Nano, add a second line to range.sh to print the name and record count of the longest file in the directory as well as the shortest. This line should be a duplicate of the one you have already written, but with sort -n -r rather than sort -n.

Solution :

# This solution uses `cp` instead of `nano`
# because our automated tests can't edit files interactively.
# Run the following command
cp /solutions/range-3.sh range.sh

'''


'''
Instructions 4/4
25 XP

Run the script on the files in the seasonal directory using seasonal/*.csv to match all of the files and redirect the output using > to a file called range.out in your home directory.

Solution :

# Run the following command
bash range.sh seasonal/*.csv > range.out

'''
