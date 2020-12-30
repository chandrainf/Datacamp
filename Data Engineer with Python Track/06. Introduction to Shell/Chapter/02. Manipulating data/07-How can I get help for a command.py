'''
How can I get help for a command?


To find out what commands do, people used to use the man command (short for "manual"). For example, the command man head brings up this information:

     HEAD(1)               BSD General Commands Manual              HEAD(1)

     NAME
          head -- display first lines of a file

     SYNOPSIS
          head [-n count | -c bytes] [file ...]

     DESCRIPTION
          This filter displays the first count lines or bytes of each of
          the specified files, or of the standard input if no files are
          specified.  If count is omitted it defaults to 10.

          If more than a single file is specified, each file is preceded by
          a header consisting of the string ``==> XXX <=='' where ``XXX''
          is the name of the file.

     SEE ALSO
          tail(1)

man automatically invokes less, so you may need to press spacebar to page through the information and :q to quit.

The one-line description under NAME tells you briefly what the command does, and the summary under SYNOPSIS lists all the flags it understands. Anything that is optional is shown in square brackets [...], either/or alternatives are separated by |, and things that can be repeated are shown by ..., so head's manual page is telling you that you can either give a line count with -n or a byte count with -c, and that you can give it any number of filenames.

The problem with the Unix manual is that you have to know what you're looking for. If you don't, you can search Stack Overflow, ask a question on DataCamp's Slack channels, or look at the SEE ALSO sections of the commands you already know.

Instructions 1/2
50 XP

1. Read the manual page for the tail command to find out what putting a + sign in front of the number used with the -n flag does. (Remember to press spacebar to page down and/or type q to quit.)

Solution :

# Run the following command
| cat': man tail | cat

'''


'''
Instructions 2/2
50 XP

2. Use tail with the flag -n +7 to display all but the first six lines of seasonal/spring.csv.

Solution :

# Run the following command
tail -n +7 seasonal/spring.csv

'''
