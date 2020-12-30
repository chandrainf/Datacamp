'''
Built-in practice: enumerate()


In this exercise, you'll practice using Python's built-in function enumerate(). This function is useful for obtaining an indexed list. For example, suppose you had a list of people that arrived at a party you are hosting. The list is ordered by arrival (Jerry was the first to arrive, followed by Kramer, etc.):

    names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

If you wanted to attach an index representing a person's arrival order, you could use the following for loop:

    indexed_names = []
    for i in range(len(names)):
        index_name = (i, names[i])
        indexed_names.append(index_name)

    [(0,'Jerry'),(1,'Kramer'),(2,'Elaine'),(3,'George'),(4,'Newman')]

But, that's not the most efficient solution. Let's explore how to use enumerate() to make this more efficient.

Instructions
100 XP

- Instead of using for i in range(len(names)), update the for loop to use i as the index variable and name as the iterator variable and use enumerate().
- Rewrite the previous for loop using enumerate() and list comprehension to create a new list, indexed_names_comp.
- Create another list (indexed_names_unpack) by using the star character (*) to unpack the enumerate object created from using enumerate() on names. This time, start the index for enumerate() at one instead of zero.

'''
# Rewrite the for loop to use enumerate
indexed_names = []
for i, name in enumerate(names):
    index_name = (i, name)
    indexed_names.append(index_name)
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i, name) for i, name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)
