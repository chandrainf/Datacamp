'''
Testing on circular data

Another special case where it is easy to guess the value of  is when the model does not fit the testing dataset at all. In this case,  takes its lowest possible value 0.0.

The plot shows such a testing dataset and model. The testing dataset consists of data arranged in a circle of radius 1.0. The x and y co-ordinates of the data is shown on the plot. The model corresponds to a straight line y=0.

As one can easily see, the straight line does not fit the data at all. In this particular case, the value of  is known to be 0.0.

Your job is to write a test test_on_circular_data() for the function model_test() that performs this sanity check. pytest, numpy as np, model_test, sin, cos and pi have been imported for you.

Instructions 1/4
25 XP

-Assign test_argument to a  NumPy array holding the circular testing data shown in the plot, starting with (1.0, 0.0) and moving anticlockwise.

'''


def test_on_circular_data(self):
    theta = pi/4.0
    # Complete the NumPy array holding the circular testing data

    test_argument = np.array([[1.0, 0.0], [cos(theta), sin(theta)],
                              [0.0, 1.0],
                              [cos(3 * theta), sin(3 * theta)],
                              [-1.0, 0.0],
                              [cos(5 * theta), sin(5 * theta)],
                              [0.0, -1.0],
                              [cos(7 * theta), sin(7 * theta)]]
                             )


'''
Instructions 2/4
25 XP

-Fill in with the slope and intercept of the straight line shown in the plot.

'''


def test_on_circular_data(self):
    theta = pi/4.0
    # Assign to a NumPy array holding the circular testing data
    test_argument = np.array([[1.0, 0.0], [cos(theta), sin(theta)],
                              [0.0, 1.0],
                              [cos(3 * theta), sin(3 * theta)],
                              [-1.0, 0.0],
                              [cos(5 * theta), sin(5 * theta)],
                              [0.0, -1.0],
                              [cos(7 * theta), sin(7 * theta)]]
                             )
    # Fill in with the slope and intercept of the straight line
    actual = model_test(test_argument, slope=0.0, intercept=0.0)


'''
Instructions 3/4
25 XP

-Remembering that model_test() returns a float, complete the assert statement to check if model_test() returns the expected value of  in this special case.
'''


def test_on_circular_data(self):
    theta = pi/4.0
    # Assign to a NumPy array holding the circular testing data
    test_argument = np.array([[1.0, 0.0], [cos(theta), sin(theta)],
                              [0.0, 1.0],
                              [cos(3 * theta), sin(3 * theta)],
                              [-1.0, 0.0],
                              [cos(5 * theta), sin(5 * theta)],
                              [0.0, -1.0],
                              [cos(7 * theta), sin(7 * theta)]]
                             )
    # Fill in with the slope and intercept of the straight line
    actual = model_test(test_argument, slope=0.0, intercept=0.0)
    # Complete the assert statement
    assert actual == pytest.approx(0.0)


'''
Instructions 4/4
25 XP
Question

The tests test_on_perfect_fit() and test_on_circular_data() that you wrote in the last two exercises has been written to the test class TestModelTest in the test module models/test_train.py. Run the test class in the IPython console. What is the outcome?

Possible Answers :

    - The sanity checks are all passing.

    - The test test_on_circular_data() is failing because model_test() returns 0.52 instead of 0.0 for circular testing data.

    - The test test_on_perfect_fit() is failing because model_test() returns 0.0 instead of 1.0 for linear data.

Answer : The sanity checks are all passing.

'''
