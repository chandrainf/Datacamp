'''
How can I select columns from a file?


head and tail let you select rows from a text file. If you want to select columns, you can use the command cut. It has several options (use man cut to explore them), but the most common is something like:

    cut -f 2-5,8 -d , values.csv
    
which means "select columns 2 through 5 and columns 8, using comma as the separator". cut uses -f (meaning "fields") to specify columns and -d (meaning "delimiter") to specify the separator. You need to specify the latter because some files may use spaces, tabs, or colons to separate columns.

What command will select the first column (containing dates) from the file spring.csv?

Instructions
50 XP

Possible Answers

    - cut -d , -f 1 seasonal/spring.csv

    - cut -d, -f1 seasonal/spring.csv

    - Either of the above.

    - Neither of the above, because -f must come before -d.

Answer : Either of the above.

'''
