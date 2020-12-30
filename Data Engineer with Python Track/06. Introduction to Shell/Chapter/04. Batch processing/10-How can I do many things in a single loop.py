'''
How can I do many things in a single loop?


The loops you have seen so far all have a single command or pipeline in their body, but a loop can contain any number of commands. To tell the shell where one ends and the next begins, you must separate them with semi-colons:

    for f in seasonal/*.csv; do echo $f; head -n 2 $f | tail -n 1; done

    seasonal/autumn.csv
    2017-01-05,canine
    seasonal/spring.csv
    2017-01-25,wisdom
    seasonal/summer.csv
    2017-01-11,canine
    seasonal/winter.csv
    2017-01-03,bicuspid

Suppose you forget the semi-colon between the echo and head commands in the previous loop, so that you ask the shell to run:

    for f in seasonal/*.csv; do echo $f head -n 2 $f | tail -n 1; done

What will the shell do?

Instructions
50 XP

Possible Answers

    -Print an error message.

    -Print one line for each of the four files.

    -Print one line for autumn.csv (the first file).

    -Print the last line of each file.

Answer : Print one line for each of the four files.

'''
