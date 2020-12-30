'''
How can I print a variable's value?


A simpler way to find a variable's value is to use a command called echo, which prints its arguments. Typing

    echo hello DataCamp!

prints

    hello DataCamp!

If you try to use it to print a variable's value like this:

    echo USER

it will print the variable's name, USER.

To get the variable's value, you must put a dollar sign $ in front of it. Typing

    echo $USER

prints

    repl

This is true everywhere: to get the value of a variable called X, you must write $X. (This is so that the shell can tell whether you mean "a file named X" or "the value of a variable named X".)

Instructions
100 XP

The variable OSTYPE holds the name of the kind of operating system you are using. Display its value using echo.

Solution :

# Run the following command
echo $OSTYPE

'''
