'''
Why shouldn't I use spaces in filenames?


It's easy and sensible to give files multi-word names like July 2017.csv when you are using a graphical file explorer. However, this causes problems when you are working in the shell. For example, suppose you wanted to rename July 2017.csv to be 2017 July data.csv. You cannot type:

    mv July 2017.csv 2017 July data.csv

because it looks to the shell as though you are trying to move four files called July, 2017.csv, 2017, and July (again) into a directory called data.csv. Instead, you have to quote the files' names so that the shell treats each one as a single parameter:

    mv 'July 2017.csv' '2017 July data.csv'

If you have two files called current.csv and last year.csv (with a space in its name) and you type:

    rm current.csv last year.csv

what will happen:

Answer the question
50XP

Possible Answers

    - The shell will print an error message because last and year.csv do not exist.

    - The shell will delete current.csv.

    - Both of the above.

    - Nothing.

Answer : Both of the above.

'''
