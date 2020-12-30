'''
How can I write loops in a shell script?


Shell scripts can also contain loops. You can write them using semi-colons, or split them across lines without semi-colons to make them more readable:

    # Print the first and last data records of each file.
    for filename in $@
    do
        head -n 2 $filename | tail -n 1
        tail -n 1 $filename
    done

(You don't have to indent the commands inside the loop, but doing so makes things clearer.)

The first line of this script is a comment to tell readers what the script does. Comments start with the # character and run to the end of the line. Your future self will thank you for adding brief explanations like the one shown here to every script you write.

As a reminder, to save what you have written in Nano, type Ctrl + O to write the file out, then Enter to confirm the filename, then Ctrl + X to exit the editor.

Instructions 1/3
35 XP

1.Fill in the placeholders in the script date-range.sh with $filename (twice), head, and tail so that it prints the first and last date from one or more files.


Solution:

# This solution uses `cp` instead of `nano`
# because our automated tests can't edit files interactively.
# Run the following command
cp /solutions/date-range.sh date-range.sh

'''


'''
Instructions 2/3
35 XP

2. Run date-range.sh on all four of the seasonal data files using seasonal/*.csv to match their names.

Solution:

# Run the following command
bash date-range.sh seasonal/*.csv

'''


'''
Instructions 3/3
30 XP

3. Run date-range.sh on all four of the seasonal data files using seasonal/*.csv to match their names, and pipe its output to sort to see that your scripts can be used just like Unix's built-in commands.

Solution:

# Run the following command
bash date-range.sh seasonal/*.csv | sort

'''
