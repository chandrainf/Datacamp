'''
Create a test class


Test classes are containers inside test modules. They help separate tests for different functions within the test module, and serve as a structuring tool in the pytest framework.

Test classes are written in CamelCase e.g. TestMyFunction as opposed to tests, which are written using underscores e.g. test_something().

You met the function split_into_training_and_testing_sets() in Chapter 2, and wrote some tests for it. One of these tests was called test_on_one_row() and it checked if the function raises a ValueError when passed a NumPy array with only one row.

In this exercise you are going to create a test class for this function. This test class will hold the test test_on_one_row().

Instructions
100 XP

- Declare the test class for the function split_into_training_and_testing_sets(), making sure to give it a name that follows the standard naming convention.
- Fill in the mandatory argument in the test test_on_one_row().

'''
import pytest
import numpy as np

from models.train import split_into_training_and_testing_sets

# Declare the test class


class TestSplitIntoTrainingAndTestingSets(object):
    # Fill in with the correct mandatory argument
    def test_on_one_row(self):
        test_argument = np.array([[1382.0, 390167.0]])
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
        expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
        assert exc_info.match(expected_error_msg)
