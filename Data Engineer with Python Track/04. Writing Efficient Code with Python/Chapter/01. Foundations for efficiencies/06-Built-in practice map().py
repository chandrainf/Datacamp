'''
Built-in practice: map()


In this exercise, you'll practice using Python's built-in map() function to apply a function to every element of an object. Let's look at a list of party guests:

  names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

Suppose you wanted to create a new list (called names_uppercase) that converted all the letters in each name to uppercase. you could accomplish this with the below for loop:

  names_uppercase = []

  for name in names:
    names_uppercase.append(name.upper())

  ['JERRY', 'KRAMER', 'ELAINE', 'GEORGE', 'NEWMAN']

Let's explore using the map() function to do this more efficiently in one line of code.

Instructions
100 XP

- Use map() and the method str.upper() to convert each name in the list names to uppercase. Save this to the variable names_map.
- Print the data type of names_map.
- Unpack the contents of names_map into a list called names_uppercase using the star character (*).
- Print names_uppercase and observe its contents.

'''

# Use map to apply str.upper to each element in names
names_map = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)
