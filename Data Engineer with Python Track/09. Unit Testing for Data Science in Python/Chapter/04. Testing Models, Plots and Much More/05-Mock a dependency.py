'''
Mock a dependency


Mocking helps us replace a dependency with a MagicMock() object. Usually, the MagicMock() is programmed to be a bug-free version of the dependency. To verify whether the function under test works properly with the dependency, you simply check whether the MagicMock() is called with the correct arguments and in the right order.

In the last exercise, you programmed a bug-free version of the dependency data.preprocessing_helpers.convert_to_int in the context of the test test_on_raw_data(), which applies preprocess() on a raw data file. The data file is printed out in the IPython console.

pytest, unittest.mock.call, preprocess raw_and_clean_data_file and convert_to_int_bug_free has been imported for you.

Instructions 1/4
25 XP

- In the test test_on_raw_data(), add the correct argument that enables the use of the mocking fixture.

'''
# Add the correct argument to use the mocking fixture in this test


def test_on_raw_data(self, raw_and_clean_data_file, mocker):
    raw_path, clean_path = raw_and_clean_data_file


'''
Instructions 2/4
25 XP

- Replace the dependency "data.preprocessing_helpers.convert_to_int" with the bug-free version convert_to_int_bug_free() by using the correct method and side effect.
'''
# Add the correct argument to use the mocking fixture in this test


def test_on_raw_data(self, raw_and_clean_data_file, mocker):
    raw_path, clean_path = raw_and_clean_data_file
    # Replace the dependency with the bug-free mock
    convert_to_int_mock = mocker.patch("data.preprocessing_helpers.convert_to_int",
                                       side_effect=convert_to_int_bug_free)


'''
Instructions 3/4
25 XP

- Use the correct attribute which returns the list of calls to the mock, and check if the mock was called with this sequence of arguments: "1,801", "201,411", "2,002", "333,209", "1990", "782,911", "1,285", "389129".

'''


def test_on_raw_data(self, raw_and_clean_data_file, mocker):
    raw_path, clean_path = raw_and_clean_data_file
    # Replace the dependency with the bug-free mock
    convert_to_int_mock = mocker.patch("data.preprocessing_helpers.convert_to_int",
                                       side_effect=convert_to_int_bug_free)
    preprocess(raw_path, clean_path)
    # Check if preprocess() called the dependency correctly
    assert convert_to_int_mock.call_args_list == [call("1,801"), call("201,411"), call(
        "2,002"), call("333,209"), call("1990"), call("782,911"), call("1,285"), call("389129")]
    with open(clean_path, "r") as f:
        lines = f.readlines()
    first_line = lines[0]
    assert first_line == "1801\\t201411\\n"
    second_line = lines[1]
    assert second_line == "2002\\t333209\\n"


'''
Instructions 4/4
25 XP
Question

The test that you wrote was written to the test class TestPreprocess in the test module data/test_preprocessing_helpers.py. The same test module also contains the test class TestConvertToInt.

Run the tests in TestPreprocess and TestConvertToInt. Based on the test result report, which of the following is correct?

Possible Answers :

    - The tests for both convert_to_int() and preprocess() passes.

    - The tests for convert_to_int() passes but the test for preprocess() fails.

    - Some tests for convert_to_int() fail but the test for preprocess() passes.

Answer : Some tests for convert_to_int() fail but the test for preprocess() passes.

'''
