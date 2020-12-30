'''
Built-in practice: range()


In this exercise, you will practice using Python's built-in function range(). Remember that you can use range() in a few different ways:

1) Create a sequence of numbers from 0 to a stop value (which is exclusive). This is useful when you want to create a simple sequence of numbers starting at zero:

    range(stop)

    # Example
    list(range(11))

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

2) Create a sequence of numbers from a start value to a stop value (which is exclusive) with a step size. This is useful when you want to create a sequence of numbers that increments by some value other than one. For example, a list of even numbers:

    range(start, stop, step)

    # Example
    list(range(2,11,2))

    [2, 4, 6, 8, 10]

Instructions
100 XP

- Create a range object that starts at zero and ends at five. Only use a stop argument.
- Convert the nums variable into a list called nums_list.
- Create a new list called nums_list2 that starts at one, ends at eleven, and increments by two by unpacking a range object using the star character (*).

'''
# Create a range object that goes from 0 to 5
nums = range(0, 6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1, 13, 2)]
print(nums_list2)
