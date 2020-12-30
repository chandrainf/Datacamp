'''
Testing well: Values triggering special logic


Look at the plot. The boundary values of row_to_list() are now marked in orange. The normal argument is marked in green and the values triggering special behavior are marked in blue.

In the last exercise, you wrote tests for boundary values. In this exercise, you are going to write tests for values triggering special behavior, in particular, (0, 1) and (2, 1). These are values triggering special logic since the function returns None instead of a list.

Instructions
100 XP

    - Assign the variable actual to the actual return value for "\n".
    - Complete the assert statement for test_on_no_tab_with_missing_value(), making sure to format the failure message appropriately.
    - Assign the variable actual to the actual return value for "123\t\t89\n".
    - Complete the assert statement for test_on_two_tabs_with_missing_value(), making sure to format the failure message appropriately.

'''
import pytest
from preprocessing_helpers import row_to_list


def test_on_no_tab_with_missing_value():    # (0, 1) case
    # Assign to the actual return value for the argument "\n"
    actual = "\n"
    # Write the assert statement with a failure message
    assert row_to_list(
        actual) is None, "Expected: None, Actual: {0}".format(actual)


def test_on_two_tabs_with_missing_value():    # (0, 1) case
    # Assign to the actual return value for the argument "123\t\t89\n"
    actual = "123\t\t89\n"
    # Write the assert statement with a failure message
    assert row_to_list(
        actual) is None, "Expected: None, Actual: {0}".format(actual)
