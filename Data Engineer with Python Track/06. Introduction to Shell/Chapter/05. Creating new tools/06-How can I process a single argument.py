'''
How can I process a single argument?


As well as $@, the shell lets you use $1, $2, and so on to refer to specific command-line parameters. You can use this to write commands that feel simpler or more natural than the shell's. For example, you can create a script called column.sh that selects a single column from a CSV file when the user provides the filename as the first parameter and the column as the second:

    cut -d , -f $2 $1

and then run it using:

    bash column.sh seasonal/autumn.csv 1

Notice how the script uses the two parameters in reverse order.

The script get-field.sh is supposed to take a filename, the number of the row to select, the number of the column to select, and print just that field from a CSV file. For example:

    bash get-field.sh seasonal/summer.csv 4 2

should select the second field from line 4 of seasonal/summer.csv. Which of the following commands should be put in get-field.sh to do that?

Answer the question
50XP

Possible Answers

    - head -n $1 $2 | tail -n 1 | cut -d , -f $3

    - head -n $2 $1 | tail -n 1 | cut -d , -f $3

    - head -n $3 $1 | tail -n 1 | cut -d , -f $2

    - head -n $2 $3 | tail -n 1 | cut -d , -f $1

Answer : head -n $2 $1 | tail -n 1 | cut -d , -f $3

'''
