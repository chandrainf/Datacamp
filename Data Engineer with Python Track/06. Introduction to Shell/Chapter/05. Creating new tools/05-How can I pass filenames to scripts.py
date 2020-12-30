'''
How can I pass filenames to scripts?


A script that processes specific files is useful as a record of what you did, but one that allows you to process any files you want is more useful. To support this, you can use the special expression $@ (dollar sign immediately followed by at-sign) to mean "all of the command-line parameters given to the script".

For example, if unique-lines.sh contains sort $@ | uniq, when you run:

    bash unique-lines.sh seasonal/summer.csv

the shell replaces $@ with seasonal/summer.csv and processes one file. If you run this:

    bash unique-lines.sh seasonal/summer.csv seasonal/autumn.csv

it processes two data files, and so on.

As a reminder, to save what you have written in Nano, type Ctrl + O to write the file out, then Enter to confirm the filename, then Ctrl + X to exit the editor.

Instructions 1/2
50 XP

1. Edit the script count-records.sh with Nano and fill in the two ____ placeholders with $@ and -l (the letter) respectively so that it counts the number of lines in one or more files, excluding the first line of each.

Solution : 

# This solution uses `cp` instead of `nano`
# because our automated tests can't edit files interactively.
# Run the following command
cp /solutions/count-records.sh ~
'''


'''
Instructions 2/2
50 XP

2. Run count-records.sh on seasonal/*.csv and redirect the output to num-records.out using >

# Run the following command
bash count-records.sh seasonal/*.csv > num-records.out

'''
