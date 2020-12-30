'''
TDD: Tests for normal arguments


In this and the following exercises, you will implement the function convert_to_int() using Test Driven Development (TDD). In TDD, you write the tests first and implement the function later.

Normal arguments for convert_to_int() are integer strings with comma as thousand separators. Since the best practice is to test a function for two to three normal arguments, here are three examples with no comma, one comma and two commas respectively.

    Argument value          Expected return value
    ---------------------------------------------
    "756"	                756
    ---------------------------------------------
    "2,081"	                2081
    ---------------------------------------------
    "1,034,891"	            1034891
    ---------------------------------------------

Since the convert_to_int() function does not exist yet, you won't be able to import it. But you will use it in the tests anyway. That's how TDD works.

pytest has already been imported for you.

Instructions
100 XP

- Complete the assert statement for test_with_no_comma() by inserting the correct boolean expression.
- Complete the assert statement for test_with_one_comma() by inserting the correct boolean expression.
- Complete the assert statement for test_with_two_commas() by inserting the correct boolean expression.

'''


def test_with_no_comma():
    actual = convert_to_int("756")
    # Complete the assert statement
    assert actual == 756, "Expected: 756, Actual: {0}".format(actual)


def test_with_one_comma():
    actual = convert_to_int("2,081")
    # Complete the assert statement
    assert actual == 2081, "Expected: 2081, Actual: {0}".format(actual)


def test_with_two_commas():
    actual = convert_to_int("1,034,891")
    # Complete the assert statement
    assert actual == 1034891, "Expected: 1034891, Actual: {0}".format(actual)
