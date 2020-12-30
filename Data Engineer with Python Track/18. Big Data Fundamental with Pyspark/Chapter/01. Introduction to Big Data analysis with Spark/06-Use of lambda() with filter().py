'''
Use of lambda() with filter()


Another function that is used extensively in Python is the filter() function. The filter() function in Python takes in a function and a list as arguments. The general syntax of the filter() function is filter(function, list_of_input). Similar to the map(), filter() can be used with lambda() function. The general syntax of the filter() function with lambda() is filter(lambda <argument>:<expression>, list). Refer to slide 6 of video 1.7 for general help of the filter() function with lambda().

In this exercise, you'll be using lambda() function inside the filter() built-in function to find all the numbers divisible by 10 in the list.

Instructions
100 XP

- Print my_list2 which is available in your environment.
- Filter the numbers divisible by 10 from my_list2 using filter() and lambda().
- Print the numbers divisible by 10 from my_list2.

'''
# Print my_list2 in the console
print("Input list is:", my_list2)

# Filter numbers divisible by 10
filtered_list = list(filter(lambda x: (x % 10 == 0), my_list2))

# Print the numbers divisible by 10
print("Numbers divisible by 10 are:", filtered_list)
