'''
How can I save the output of a pipe?


The shell lets us redirect the output of a sequence of piped commands:

    cut -d , -f 2 seasonal/*.csv | grep -v Tooth > teeth-only.txt

However, > must appear at the end of the pipeline: if we try to use it in the middle, like this:

    cut -d , -f 2 seasonal/*.csv > teeth-only.txt | grep -v Tooth

then all of the output from cut is written to teeth-only.txt, so there is nothing left for grep and it waits forever for some input.

What happens if we put redirection at the front of a pipeline as in:

    > result.txt head -n 3 seasonal/winter.csv

Instructions
50 XP

Possible Answers

    - The command's output is redirected to the file as usual.

    - The shell reports it as an error.

    - The shell waits for input forever.

Answer : The command's output is redirected to the file as usual.

'''
