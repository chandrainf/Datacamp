'''
A taste of things to come


In this exercise, you'll explore both the Non-Pythonic and Pythonic ways of looping over a list.

    names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

Suppose you wanted to collect the names in the above list that have six letters or more. In other programming languages, the typical approach is to create an index variable (i), use i to iterate over the list, and use an if statement to collect the names with six letters or more:

    i = 0
    new_list= []
    while i < len(names):
        if len(names[i]) >= 6:
            new_list.append(names[i])
        i += 1

Let's explore some more Pythonic ways of doing this.

Instructions 1/3
35 XP

Print the list, new_list, that was created using a Non-Pythonic approach.

'''
# Print the list created using the Non-Pythonic approach
i = 0
new_list = []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)


'''
Instructions 2/3
35 XP

A more Pythonic approach would loop over the contents of names, rather than using an index variable. Print better_list.

'''
# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)


'''
Instructions 3/3
30 XP

The best Pythonic way of doing this is by using list comprehension. Print best_list.

'''

# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)
