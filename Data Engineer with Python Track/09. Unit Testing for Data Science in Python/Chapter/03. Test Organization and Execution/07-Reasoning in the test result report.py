'''
Reasoning in the test result report


In the last exercises, you marked the test class TestModelTest in the test module models/test_train.py as expected to fail. You also marked the test test_on_clean_file() in the test class TestGetDataAsNumpyArray belonging to the test module features/test_as_numpy.py as skipped if the Python version is greater than 2.7.

In both cases, you provided a reason argument which detailed why they are expected to fail or skipped. In this exercise, your job is to make this reason show up in the test result report when you run all tests in the IPython console.

Feel free to run the !pytest command with different options and flags in the IPython console while doing the exercise.

Instructions 1/3
35 XP
Question

What is the command that would only show the reason for expected failures in the test result report?

Possible Answers : 

    - !pytest -r

    - !pytest -rx

    - !pytest -x

    - !pytest -rs

Answer : !pytest -rx


Instructions 2/3
35 XP
Question

What is the command that would only show the reason for skipped tests in the test result report?

Possible Answers :

    - !pytest -r.

    - !pytest -rx.

    - !pytest -s.

    - !pytest -rs.

Answer : !pytest -rs.

Instructions 3/3
30 XP
Question

What is the command that would show the reason for both skipped tests and tests that are expected to fail in the test result report?

Possible Answers :

    - !pytest -rsx.

    - !pytest -sx.

    - !pytest -s -x

Answer : !pytest -rsx.

'''
