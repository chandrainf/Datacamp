'''
How can I list everything below a directory?


In order to see everything underneath a directory, no matter how deeply nested it is, you can give ls the flag -R (which means "recursive"). If you use ls -R in your home directory, you will see something like this:

    backup          course.txt      people          seasonal

    ./backup:

    ./people:
    agarwal.txt

    ./seasonal:
    autumn.csv      spring.csv      summer.csv      winter.csv

This shows every file and directory in the current level, then everything in each sub-directory, and so on.

Instructions
100 XP

To help you know what is what, ls has another flag -F that prints a / after the name of every directory and a * after the name of every runnable program. Run ls with the two flags, -R and -F, and the absolute path to your home directory to see everything it contains. (The order of the flags doesn't matter, but the directory name must come last.)

Solution : 

# Run the following command
ls -R -F /home/repl

'''
