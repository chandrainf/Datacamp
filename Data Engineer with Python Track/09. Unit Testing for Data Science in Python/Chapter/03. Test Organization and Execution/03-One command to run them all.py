'''
One command to run them all


One of your colleagues pushed some changes to the functions row_to_list(), convert_to_int(), get_data_as_numpy_array() and split_into_training_and_testing_sets(). That means that you have to run all the tests again to figure out if something got broken as a result.

The current working directory in the IPython console is the tests directory, which contains all the tests in the same layout as described in the video. You can, at any time, run the tests in the IPython console using the appropriate command.

Instructions 1/4
25 XP

Question :

In the IPython console, what is the correct command for running all tests contained in the tests folder?

Possible Answers

    - !pytest

    - !pytest -x

    - !pytest tests

    - pytest

Answer : !pytest

'''


'''
Instructions 2/4
25 XP

Question :

When you run all tests with the command !pytest, how many of them pass and how may fail?

Possible Answers  

    - Passing: 10, Failing: 6

    - Passing: 15, Failing: 1

    - Passing 16, Failing: 0

Answer : Passing: 15, Failing: 1

'''


'''
Instructions 3/4
25 XP

Question :

Assuming that you simply want to answer the binary question "Are all tests passing" without wasting time and resources, what is the correct command to run all tests till the first failure is encountered?

Possible Answers : 

    - !pytest -k

    - !pytest

    - !pytest -x

Answer : !pytest -x

'''


'''
Instructions 4/4
25 XP

Question :

When you ran the tests using the !pytest -x command, how many tests ran in total before test execution stopped because of the first failing test?

Possible Answers

    - 16

    - 15

    - 7

Answer : 15

'''
