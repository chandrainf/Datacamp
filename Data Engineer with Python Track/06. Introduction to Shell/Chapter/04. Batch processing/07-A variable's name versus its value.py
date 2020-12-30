'''
A variable's name versus its value


A common mistake is to forget to use $ before the name of a variable. When you do this, the shell uses the name you have typed rather than the value of that variable.

A more common mistake for experienced users is to mis-type the variable's name. For example, if you define datasets like this:

    datasets=seasonal/*.csv

and then type:

    echo $datsets

the shell doesn't print anything, because datsets (without the second "a") isn't defined.


If you were to run these two commands in your home directory, what output would be printed?

    files=seasonal/*.csv
    for f in files; do echo $f; done

(Read the first part of the loop carefully before answering.)

Answer the question
50XP

Possible Answers

    - One line: the word "files".

    - Four lines: the names of all four seasonal data files.

    - Four blank lines: the variable f isn't assigned a value.

Answer : One line: the word "files".

'''
