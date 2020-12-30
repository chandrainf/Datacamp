'''
TDD: Implement the function


convert_to_int() returns None for the following:

    1. Arguments with missing thousands comma e.g. "178100,301". If you split the string at the comma using "178100,301".split(","), then the resulting list ["178100", "301"] will have at least one entry with length greater than 3 e.g. "178100".

    2. Arguments with incorrectly placed comma e.g. "12,72,891". If you split this at the comma, then the resulting list is ["12", "72", "891"]. Note that the first entry is allowed to have any length between 1 and 3. But if any other entry has a length other than 3, like "72", then there's an incorrectly placed comma.

    3. Float valued strings e.g. "23,816.92". If you remove the commas and call int() on this string i.e. int("23816.92"), you will get a ValueError.

Instructions 1/4
25 XP

-Complete the if statement that checks if the i-th element of comma_separated_parts has length greater than 3.

'''


def convert_to_int(integer_string_with_commas):
    comma_separated_parts = integer_string_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        # Write an if statement for checking missing commas
        if len(comma_separated_parts[i]) > 3:
            return None


'''
Instructions 2/4
25 XP

-Complete the if statement that checks if any entry other than the 0-th entry of comma_separated_parts has a length not equal to 3.

'''


def convert_to_int(integer_string_with_commas):
    comma_separated_parts = integer_string_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        # Write an if statement for checking missing commas
        if len(comma_separated_parts[i]) > 3:
            return None
        # Write the if statement for incorrectly placed commas
        if i != 0 and len(comma_separated_parts[i]) != 3:
            return None


'''
Instructions 3/4
25 XP

Fill in the except clause with a ValueError, which is raised when trying to convert float valued strings e.g. 23816.92 to an integer.

'''


def convert_to_int(integer_string_with_commas):
    comma_separated_parts = integer_string_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        # Write an if statement for checking missing commas
        if len(comma_separated_parts[i]) > 3:
            return None
        # Write the if statement for incorrectly placed commas
        if i != 0 and len(comma_separated_parts[i]) != 3:
            return None
    integer_string_without_commas = "".join(comma_separated_parts)
    try:
        return int(integer_string_without_commas)
    # Fill in with the correct exception for float valued argument strings
    except ValueError:
        return None


'''
Instructions 4/4
25 XP

Question :

Now that you have implemented the convert_to_int() function, let's run the tests in the test module test_convert_to_int.py again. Run it the IPython console and read the test result report. Did you implement the function correctly, or are there any bugs?

Possible Answers :

    - All tests are passing and the implementation does not have a bug.

    - The test test_on_string_with_incorrectly_placed_comma() is failing because the convert_to_int("12,72,891") is returning 1272891 instead of None.

    - All tests are failing with a NameError since convert_to_int() has not been implemented yet.

Answer : All tests are passing and the implementation does not have a bug.

'''
