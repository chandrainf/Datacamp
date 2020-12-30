'''
Mark a test class as expected to fail


A new function model_test() is being developed and it returns the accuracy of a given linear regression model on a testing dataset. Test Driven Development (TDD) is being used to implement it. The procedure is: write tests first and then implement the function.

A test class TestModelTest has been created within the test module models/test_train.py. In the test class, there are two unit tests called test_on_linear_data() and test_on_one_dimensional_array(). But the function model_test() has not been implemented yet.

Throughout this exercise, pytest and numpy as np will be imported for you.

Instructions 1/3
35 XP

Question :

Run the tests in the test class TestModelTest in the IPython console. What is the outcome?

Possible Answers : 

    - The tests fail with IndexError because some arguments to format the variable message are missing.

    - The tests pass.

    - The tests fail with NameError since the function model_test() has not yet been defined.

    - The tests fail with AssertionError.

Answer : The tests fail with NameError since the function model_test() has not yet been defined.

'''


'''
Instructions 2/3
35 XP

-Mark the whole test class TestModelTest as "expected to fail".

'''
# Mark the whole test class as "expected to fail"
@pytest.mark.xfail(reason="Using TDD, model_test() has not yet been implemented")
class TestModelTest(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)
        message = "model_test({0}) should return {1}, but it actually returned {2}".format(
            test_input, expected, actual)
        assert actual == pytest.approx(expected), message

    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)


'''
Instructions 3/3
30 XP

-Add the following reason for the expected failure: "Using TDD, model_test() has not yet been implemented".

'''
# Add a reason for the expected failure


@pytest.mark.xfail(reason="Using TDD, model_test() has not yet been implemented")
class TestModelTest(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)
        message = "model_test({0}) should return {1}, but it actually returned {2}".format(
            test_input, expected, actual)
        assert actual == pytest.approx(expected), message

    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)
