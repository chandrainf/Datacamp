'''
Use a fixture for a clean data file

In the video, you saw how the preprocess() function creates a clean data file.

The get_data_as_numpy_array() function takes the path to this clean data file as the first argument and the number of columns of data as the second argument. It returns a NumPy array holding the data.

In a previous exercise, you wrote the test test_on_clean_file() without using a fixture. That's bad practice! This time, you'll use the fixture clean_data_file(), which

    - creates a clean data file in the setup,
    - yields the path to the clean data file,
    - removes the clean data file in the teardown.

The contents of the clean data file that you will use for testing is printed in the IPython console.

pytest, os, numpy as np and get_data_as_numpy_array() have been imported for you.

Instructions
100 XP

- Add the correct decorator that would turn clean_data_file() into a fixture.
- Pass an argument to the test test_on_clean_file() so that it uses the fixture.
- Pass the clean data file path yielded by the fixture as the first argument to the function get_data_as_numpy_array().

'''

# Add a decorator to make this function a fixture
@pytest.fixture
def clean_data_file():
    file_path = "clean_data_file.txt"
    with open(file_path, "w") as f:
        f.write("201\t305671\n7892\t298140\n501\t738293\n")
    yield file_path
    os.remove(file_path)

# Pass the correct argument so that the test can use the fixture


def test_on_clean_file(clean_data_file):
    expected = np.array(
        [[201.0, 305671.0], [7892.0, 298140.0], [501.0, 738293.0]])
    # Pass the clean data file path yielded by the fixture as the first argument
    actual = get_data_as_numpy_array(clean_data_file, 2)
    assert actual == pytest.approx(
        expected), "Expected: {0}, Actual: {1}".format(expected, actual)
