'''
How can I record the names of a set of files?


People often set a variable using a wildcard expression to record a list of filenames. For example, if you define datasets like this:

    datasets=seasonal/*.csv

you can display the files' names later using:

    for filename in $datasets; do echo $filename; done

This saves typing and makes errors less likely.

If you run these two commands in your home directory, how many lines of output will they print?

    files=seasonal/*.csv
    for f in $files; do echo $f; done

Instructions
50 XP

Possible Answers

    - None: since files is defined on a separate line, it has no value in the second line.

    - One: the word "files".

    - Four: the names of all four seasonal data files.

Answer : Four: the names of all four seasonal data files.

'''
