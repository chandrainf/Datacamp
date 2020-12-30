'''
How can I move a file?


While cp copies a file, mv moves it from one directory to another, just as if you had dragged it in a graphical file browser. It handles its parameters the same way as cp, so the command:

    mv autumn.csv winter.csv ..
    
moves the files autumn.csv and winter.csv from the current working directory up one level to its parent directory (because .. always refers to the directory above your current location).

Instructions
100 XP

You are in /home/repl, which has sub-directories seasonal and backup. Using a single command, move spring.csv and summer.csv from seasonal to backup.

Solution:

# Run the following command
mv seasonal/spring.csv seasonal/summer.csv backup

'''
