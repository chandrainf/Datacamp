'''
Testing with multiple assert statements


You're now going to test the function split_into_training_and_testing_sets() from the models module.

It takes a n x 2 NumPy array containing housing area and prices as argument. To see an example argument, print the variable example_argument in the IPython console.

The function returns a 2-tuple of NumPy arrays (training_set, testing_set). The training set contains int(0.75 * n) (approx. 75%) randomly selected rows of the argument array. The testing set contains the remaining rows.

Print the variable expected_return_value in the IPython console. example_argument had 6 rows. Therefore the training array has int(0.75 * 6) = 4 of its rows and the testing array has the remaining 2 rows.

numpy as np, pytest and split_into_training_and_testing_sets have been imported for you.

Instructions 1/4
25 XP

- Calculate the expected number of rows of the training array using the formula int(0.75*n), where n is the number of rows in example_argument, and assign the variable expected_training_array_num_rows to this number.

'''


def test_on_six_rows():
    example_argument = np.array([[2081.0, 314942.0], [1059.0, 186606.0],
                                 [1148.0, 206186.0], [1506.0, 248419.0],
                                 [1210.0, 214114.0], [1697.0, 277794.0]]
                                )
    # Fill in with training array's expected number of rows
    expected_training_array_num_rows = 4


'''
Instructions 2/4
25 XP
Calculate the expected number of rows of the testing array using the formula n - int(0.75*n), where n is the number of rows in example_argument, and assign the variable expected_testing_array_num_rows to this number.

'''


def test_on_six_rows():
    example_argument = np.array([[2081.0, 314942.0], [1059.0, 186606.0],
                                 [1148.0, 206186.0], [1506.0, 248419.0],
                                 [1210.0, 214114.0], [1697.0, 277794.0]]
                                )
    # Fill in with training array's expected number of rows
    expected_training_array_num_rows = 4
    # Fill in with testing array's expected number of rows
    expected_testing_array_num_rows = example_argument.shape[0] - \
        int(.75 * example_argument.shape[0])


'''
Instructions 3/4
25 XP

Write an assert statement that checks if training array has expected_training_array_num_rows rows.

'''


def test_on_six_rows():
    example_argument = np.array([[2081.0, 314942.0], [1059.0, 186606.0],
                                 [1148.0, 206186.0], [1506.0, 248419.0],
                                 [1210.0, 214114.0], [1697.0, 277794.0]]
                                )
    # Fill in with training array's expected number of rows
    expected_training_array_num_rows = 4
    # Fill in with testing array's expected number of rows
    expected_testing_array_num_rows = 2
    actual = split_into_training_and_testing_sets(example_argument)
    # Write the assert statement checking training array's number of rows
    assert actual[0].shape[0] == expected_training_array_num_rows, "The actual number of rows in the training array is not {}".format(
        expected_training_array_num_rows)


'''
Instructions 4/4
25 XP

Write an assert statement that checks if testing array has expected_testing_array_num_rows rows.

'''


def test_on_six_rows():
    example_argument = np.array([[2081.0, 314942.0], [1059.0, 186606.0],
                                 [1148.0, 206186.0], [1506.0, 248419.0],
                                 [1210.0, 214114.0], [1697.0, 277794.0]]
                                )
    # Fill in with training array's expected number of rows
    expected_training_array_num_rows = 4
    # Fill in with testing array's expected number of rows
    expected_testing_array_num_rows = 2
    actual = split_into_training_and_testing_sets(example_argument)
    # Write the assert statement checking training array's number of rows
    assert actual[0].shape[0] == expected_training_array_num_rows, "The actual number of rows in the training array is not {}".format(
        expected_training_array_num_rows)
    # Write the assert statement checking testing array's number of rows
    assert actual[1].shape[0] == expected_testing_array_num_rows,  "The actual number of rows in the testing array is not {}".format(
        expected_testing_array_num_rows)
