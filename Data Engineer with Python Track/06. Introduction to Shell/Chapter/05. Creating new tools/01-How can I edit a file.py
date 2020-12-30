'''
How can I edit a file?


Unix has a bewildering variety of text editors. For this course, we will use a simple one called Nano. If you type nano filename, it will open filename for editing (or create it if it doesn't already exist). You can move around with the arrow keys, delete characters using backspace, and do other operations with control-key combinations:

    -Ctrl + K: delete a line.
    -Ctrl + U: un-delete a line.
    -Ctrl + O: save the file ('O' stands for 'output'). You will also need to press Enter to confirm the filename!
    -Ctrl + X: exit the editor.

Instructions
100 XP

Run nano names.txt to edit a new file in your home directory and enter the following four lines:

    Lovelace
    Hopper
    Johnson
    Wilson

To save what you have written, type Ctrl + O to write the file out, then Enter to confirm the filename, then Ctrl + X to exit the editor.

Solution :

# Run the following command
# This solution uses `cp` instead of `nano`
# because our automated tests can't edit files interactively.

cp /solutions/names.txt /home/repl

'''
