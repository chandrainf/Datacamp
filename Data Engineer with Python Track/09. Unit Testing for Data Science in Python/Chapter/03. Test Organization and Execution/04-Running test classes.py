'''
Running test classes


When you ran the !pytest command in the last exercise, the test test_on_six_rows() failed. This is a test for the function split_into_training_and_testing_sets(). This means that this function is broken.

Short recap in case you forgot: this function takes a NumPy array containing housing area and prices as argument. The function randomly splits the argument array into training and testing arrays in the ratio 3:1, and returns the resulting arrays in a tuple.

A quick look revealed that during the code update, someone inadvertently changed the split from 3:1 to 9:1. This has to be changed back and the unit tests for the function, which now lives in the test class TestSplitIntoTrainingAndTestingSets, needs to be run again. Are you up to the challenge?

Instructions 1/4
25 XP

- Fill in with a float between 0 and 1 so that num_training is approximately 3/4 of the number of rows in data_array.

'''
import numpy as np


def split_into_training_and_testing_sets(data_array):
    dim = data_array.ndim
    if dim != 2:
        raise ValueError(
            "Argument data_array must be two dimensional. Got {0} dimensional array instead!".format(dim))
    num_rows = data_array.shape[0]
    if num_rows < 2:
        raise ValueError(
            "Argument data_array must have at least 2 rows, it actually has just {0}".format(num_rows))
    # Fill in with the correct float
    num_training = int(num_rows * data_array.shape[0])
    permuted_indices = np.random.permutation(data_array.shape[0])
    return data_array[permuted_indices[:num_training], :], data_array[permuted_indices[num_training:], :]


'''
Instructions 2/4
25 XP

Question :

Now let's see if that modification fixed the broken function. The current working directory in the IPython console is the tests folder that contains all tests. The test class TestSplitIntoTrainingAndTestingSets resides in the test module tests/models/test_train.py.

What is the correct command to run all the tests in this test class using node IDs?

Possible Answers : 

    - !pytest models::test_train.py::TestSplitIntoTrainingAndTestingSets

    - !pytest -k "TestSplitIntoTrainingAndTestingSets"

    - !pytest models/test_train.py/TestSplitIntoTrainingAndTestingSets

    - !pytest models/test_train.py::TestSplitIntoTrainingAndTestingSets

Answer : !pytest models/test_train.py::TestSplitIntoTrainingAndTestingSets

'''


'''
Instructions 3/4
25 XP

Question :

What is the correct command to run only the previously failing test test_on_six_rows() using node IDs?

Possible Answers

    - !pytest models/test_train.py::TestSplitIntoTrainingAndTestingSets::test_on_six_rows

    - !pytest models/test_train.py::test_on_six_rows

    - !pytest test_on_six_rows

Answer : !pytest models/test_train.py::TestSplitIntoTrainingAndTestingSets::test_on_six_rows

'''


'''
Instructions 4/4
25 XP

Question :

What is the correct command to run the tests in TestSplitIntoTrainingAndTestingSets using keyword expressions?

Possible Answers :

    - !pytest models/test_train.py::TestSplitIntoTrainingAndTestingSets

    - !pytest -x "TestSplitIntoTrainingAndTestingSets"

    - !pytest -k "SplitInto"

    - !pytest -k "Test"

Answer : !pytest -k "SplitInto"

'''
