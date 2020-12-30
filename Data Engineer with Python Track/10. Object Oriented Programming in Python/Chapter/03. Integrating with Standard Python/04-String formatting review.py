'''
String formatting review


Before you start defining custom string representations for objects, make sure you are comfortable working with strings and formatting them. If you need a refresher, take a minute to look through the official Python tutorial on string formatting.

In this exercise, consider the following code

    my_num = 5
    my_str = "Hello"

    f = ...
    print(f)

where the definition for f is missing.

Here are a few possible variants for the definition of f:

1.
    f = "my_num is {0}, and my_str is {1}.".format(my_num, my_str)
2.
    f = "my_num is {}, and my_str is \"{}\".".format(my_num, my_str)
3.
    f = "my_num is {n}, and my_str is '{s}'.".format(n=my_num, s=my_str)
4.
    f = "my_num is {my_num}, and my_str is '{my_str}'.".format()

Instructions 1/1
100 XP

Question :

Pick the definition of f that will make the code above print exactly the following:

    my_num is 5, and my_str is "Hello".

There is only one correct answer! Feel free to use the script pane or console to experiment.

Possible Answers

    - 1

    - 2

    - 3

    - 4

Answer : 2

'''
