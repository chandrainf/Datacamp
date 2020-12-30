'''
A simple Bash script


Welcome to your first IDE exercise! On the left, you have a directory of folders and several files. 
You can open the files and see the code in the right pane. 
This will auto-save every few seconds, though you can still use cmd + s (on mac, or ctrl + s on windows) to save.

You can run scripts using the run this file button or via the terminal window below (using the command bash script.sh). 
Running in terminal is good practice for real use cases and will be necessary later when we cover arguments.

IDE interface annotated screenshot

Let's start with a very basic example to practice turning command-line (shell) arguments into a Bash script. 
In the provided editor, the first line has already been written for you. 
Remember how that was called the 'hash-bang' or 'shebang'? 
For this environment bash is not located at /usr/bash but at /bin/bash. 
You can confirm this with the command which bash.

There is a file in your working directory called server_log_with_todays_date.txt. 
Your task is to write a simple Bash script that concatenates this out to the terminal so you can see what is inside.

Instructions
100XP

- Create a single-line script that concatenates the mentioned file.
- Save your script and run from the console.

'''
#!/bin/bash

# Concatenate the file
cat server_log_with_todays_date.txt

# Now save and run!
