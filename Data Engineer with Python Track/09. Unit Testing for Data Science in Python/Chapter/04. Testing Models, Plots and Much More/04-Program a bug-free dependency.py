'''
Program a bug-free dependency


In the video, row_to_list() was mocked. But preprocess() has another dependency convert_to_int(). Generally, its best to mock all dependencies of the function under test. It's your job to mock convert_to_int() in this and the following exercises.

The raw data file used in the test is printed in the IPython console. The second row "1,767565,112\n" is dirty, so row_to_list() will filter it out. The rest will be converted to lists and convert_to_int() will process the areas and prices.

The mocked convert_to_int() should process these areas and prices correctly. Here is the dictionary holding the correct return values.

    {"1,801": 1801, "201,411": 201411, "2,002": 2002, "333,209": 333209, "1990": None, "782,911": 782911, "1,285": 1285, "389129": None}

Instructions
100 XP

- Define a function convert_to_int_bug_free() which takes one argument called comma_separated_integer_string.
- Assign return_values to the dictionary holding the correct return values in the context of the raw data file used in the test.
- Return the correct return value by looking up the dictionary return_values for the key comma_separated_integer_string.

'''

# Define a function convert_to_int_bug_free


def convert_to_int_bug_free(comma_separated_integer_string):
    # Assign to the dict holding the correct return values
    return_values = comma_separated_integer_string
    # Return the correct result using the dict return_values
    return return_values[1]
