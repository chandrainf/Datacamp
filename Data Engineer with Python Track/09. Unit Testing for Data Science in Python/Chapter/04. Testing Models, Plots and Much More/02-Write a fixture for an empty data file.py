'''
Write a fixture for an empty data file

When a function takes a data file as an argument, you need to write a fixture that takes care of creating and deleting that data file. This exercise will test your ability to write such a fixture.

get_data_as_numpy_array() should return an empty numpy array if it gets an empty data file as an argument. To test this behavior, you need to write a fixture empty_file() that does the following.

    - Creates an empty data file empty.txt relative to the current working directory in setup.
    - Yields the path to the empty data file.
    - Deletes the empty data file in teardown.

The fixture will be used by the test test_on_empty_file(), which is available for you to see in the script.

os, pytest, numpy as np and get_data_as_numpy_array have been imported for you.

Instructions 1/2
50 XP

- In the setup, assign the variable file_path to the correct string.
- After the setup, yield the variable file_path so that the test can use it.
- In the teardown, remove the file.

'''
@pytest.fixture
def empty_file():
    # Assign the file path "empty.txt" to the variable
    file_path = "empty.txt"
    open(file_path, "w").close()
    # Yield the variable file_path
    yield file_path
    # Remove the file in the teardown
    os.remove(file_path)


def test_on_empty_file(self, empty_file):
    expected = np.empty((0, 2))
    actual = get_data_as_numpy_array(empty_file, 2)
    assert actual == pytest.approx(
        expected), "Expected: {0}, Actual: {1}".format(expected, actual)


'''
Instructions 2/2
50 XP
Question

The test test_on_empty_file() was added to the test class TestGetDataAsNumpyArray, which lives in the test module tests/features/test_as_numpy.py. The fixture empty_file() was also written to this test module.

Remembering that the current working directory in the IPython console is tests, run the test test_on_empty_file(). What is the outcome?

Possible Answers :

    -The test passes.

    -The test fails because get_data_as_numpy_array() does not return an empty NumPy array, and instead returns None.

    -The test fails with a NameError as Python 3 does not recognize the xrange() function.

Answer : The test passes.

'''
