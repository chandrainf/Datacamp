'''
Using decorator syntax


You have written a decorator called print_args that prints out all of the arguments and their values any time a function that it is decorating gets called.

Instructions 1/2
50 XP

Decorate my_function() with the print_args() decorator by redefining my_function().

'''


def my_function(a, b, c):
    print(a + b + c)


# Decorate my_function() with the print_args() decorator
my_function = print_args(my_function)

my_function(1, 2, 3)


'''
Instructions 2/2
50 XP

Decorate my_function() with the print_args() decorator using decorator syntax.

'''
# Decorate my_function() with the print_args() decorator
@print_args
def my_function(a, b, c):
    print(a + b + c)


my_function(1, 2, 3)
