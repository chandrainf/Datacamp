'''
How can I copy files?


You will often want to copy files, move them into other directories to organize them, or rename them. One command to do this is cp, which is short for "copy". If original.txt is an existing file, then:

    cp original.txt duplicate.txt

creates a copy of original.txt called duplicate.txt. If there already was a file called duplicate.txt, it is overwritten. If the last parameter to cp is an existing directory, then a command like:

    cp seasonal/autumn.csv seasonal/winter.csv backup

copies all of the files into that directory.

Instructions 1/2
50 XP

1. Make a copy of seasonal/summer.csv in the backup directory (which is also in /home/repl), calling the new file summer.bck.

Solution: 

# Run the following command
cp seasonal/summer.csv backup/summer.bck

'''


'''
Instructions 2/2
50 XP

2. Copy spring.csv and summer.csv from the seasonal directory into the backup directory without changing your current working directory (/home/repl).

Solution: 

# Run the following command
cp seasonal/spring.csv seasonal/summer.csv backup

'''
