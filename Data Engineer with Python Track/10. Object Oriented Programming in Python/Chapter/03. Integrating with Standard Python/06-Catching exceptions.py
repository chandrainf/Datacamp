'''
Catching exceptions


Before you start writing your own custom exceptions, let's make sure you have the basics of handling exceptions down.

In this exercise, you are given a function invert_at_index(x, ind) that takes two arguments, a list x and an index ind, and inverts the element of the list at that index. For example invert_at_index([5,6,7], 1) returns 1/6, or 0.166666 .

Try running the code as-is and examine the output in the console. There are two unsafe operations in this function: first, if the element that we're trying to invert has the value 0, then the code will cause a ZeroDivisionError exception. Second, if the index passed to the function is out of range for the list, the code will cause a IndexError. In both cases, the script will be interrupted, which might not be desirable.

Instructions
100 XP

Use a try - except - except pattern (with two except blocks) inside the function to catch and handle two exceptions as follows:

- try executing the code as-is,
- if ZeroDivisionError occurs, print "Cannot divide by zero!",
- if IndexError occurs, print "Index out of range!"

You know you got it right if the code runs without errors, and the output in the console is:

    0.16666666666666666
    Cannot divide by zero!
    None
    Index out of range!
    None

'''


def invert_at_index(x, ind):

    try:
        return 1/x[ind]

    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("Index out of range!")


a = [5, 6, 0, 7]

# Works okay
print(invert_at_index(a, 1))

# Potential ZeroDivisionError
print(invert_at_index(a, 2))

# Potential IndexError
print(invert_at_index(a, 5))
