'''
Testing on linear data


The model_test() function, which measures how well the model fits unseen data, returns a quantity called  which is very difficult to compute in the general case. Therefore, you need to find special testing sets where computing  is easy.

One important special case is when the model fits the testing set perfectly. This happens when the testing set is perfectly linear. One such testing set is printed out in the IPython console for you.

In this special case, model_test() should return 1.0 if the model's slope and intercept match the testing set, because 1.0 is usually the highest possible value that r2 can take.

Remember that for data points , the slope is (Xn,Yn), the slope is y2-y1/x2-x1 and the intercept is y1-slope X x1.

Instructions
100 XP

- Assign the variable test_argument to a NumPy array holding the perfectly linear testing data printed out in the IPython console.
- Assign the variable expected to the expected value of  in the special case of a perfect fit.
- Fill in with the model's slope and intercept that matches the testing set.
- Remembering that actual is a float, complete the assert statement to check if actual returned by model_test() is equal to the expected return value expected.

'''
import numpy as np
import pytest
from models.train import model_test


def test_on_perfect_fit():
    # Assign to a NumPy array containing a linear testing set
    test_argument = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
    # Fill in with the expected value of r^2 in the case of perfect fit
    expected = 1.0
    # Fill in with the slope and intercept of the model
    actual = model_test(test_argument, slope=2.0, intercept=1.0)
    # Complete the assert statement
    assert actual == pytest.approx(
        expected), "Expected: {0}, Actual: {1}".format(expected, actual)
