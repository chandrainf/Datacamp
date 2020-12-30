'''
Using %timeit: formal name or literal syntax


Python allows you to create data structures using either a formal name or a literal syntax. In this exercise, you'll explore how using a literal syntax for creating a data structure can speed up runtimes.

    data structure	    formal name	    literal syntax
    list	            list()	        []
    dictionary	        dict()	        {}
    tuple	            tuple()	        ()

Instructions 1/3
35 XP

- Create an empty list called formal_list using the formal name (list()).
- Create an empty list called literal_list using the literal syntax ([]).

'''
# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)


'''
Instructions 2/3
35 XP

-Print out the type of formal_list and literal_list to show that both naming conventions create a list.

'''
# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))


'''
Instructions 3/3
30 XP

Question

Use %timeit in your IPython console to compare runtimes between creating a list using the formal name (list()) and the literal syntax ([]). Don't include the print() statements when timing.

Which naming convention is faster?

Possible Answers

    - Using the formal name (list()) to create a list is faster.

    - Using the literal syntax ([]) to create a list is faster.

    - Both naming conventions have the same runtime.

Answer : Using the literal syntax ([]) to create a list is faster.

'''
