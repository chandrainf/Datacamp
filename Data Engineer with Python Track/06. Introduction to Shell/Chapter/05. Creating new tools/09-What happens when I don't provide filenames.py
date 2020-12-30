'''
What happens when I don't provide filenames?


A common mistake in shell scripts (and interactive commands) is to put filenames in the wrong place. If you type:

    tail -n 3

then since tail hasn't been given any filenames, it waits to read input from your keyboard. This means that if you type:

    head -n 5 | tail -n 3 somefile.txt
    
then tail goes ahead and prints the last three lines of somefile.txt, but head waits forever for keyboard input, since it wasn't given a filename and there isn't anything ahead of it in the pipeline.

Suppose you do accidentally type:

    head -n 5 | tail -n 3 somefile.txt

What should you do next?

Instructions
50 XP

Possible Answers

    - Wait 10 seconds for head to time out.

    - Type somefile.txt and press Enter to give head some input.

    - Use Ctrl + C to stop the running head program.

Answer : Use Ctrl + C to stop the running head program.

'''
