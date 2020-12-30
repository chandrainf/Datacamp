'''
TDD: Requirement collection


What should convert_to_int() do if the arguments are not normal? In particular, there are three special argument types:

    1. Arguments that are missing a comma e.g. "178100,301".
    2. Arguments that have the comma in the wrong place e.g. "12,72,891".
    3. Float valued strings e.g. "23,816.92".

Also, should convert_to_int() raise an exception for specific argument values?

When your boss asked you to implement the function, she didn't say anything about these cases! But since you want to write tests for special and bad arguments as a part of TDD, you go and ask your boss.

She says that convert_to_int() should return None for every special argument and there are no bad arguments for this function.

pytest has been imported for you.

Instructions 1/2
50 XP

- Give a name to the test by using the standard name prefix that pytest expects followed by on_string_with_missing_comma.
- Assign actual to the actual return value for the argument "12,72,891".
- Complete the assert statement.

'''
# Give a name to the test for an argument with missing comma


def test_on_string_with_missing_comma():
    actual = convert_to_int("178100,301")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


def test_on_string_with_incorrectly_placed_comma():
    # Assign to the actual return value for the argument "12,72,891"
    actual = convert_to_int("12,72,891")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


def test_on_float_valued_string():
    actual = convert_to_int("23,816.92")
    # Complete the assert statement
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


'''
Instructions 2/2
50 XP

Question :

The tests for normal and special arguments have been written to a test module test_convert_to_int.py. Run it in the IPython console and read the test result report. What happens?

Possible Answers

    - All tests are passing.

    - The test test_on_string_with_two_commas() is failing because the convert_to_int("1,034,891") returns None instead of the correct integer 1034891.

    - All tests are failing with a NameError since convert_to_int() has not been implemented yet.

Answer : All tests are failing with a NameError since convert_to_int() has not been implemented yet.

'''
