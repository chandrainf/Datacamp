'''
Spotting and fixing bugs


To find bugs in functions, you need to follow a four step procedure.

    1. Write unit tests.
    2. Run them.
    3. Read the test result report and spot the bugs.
    4. Fix the bugs.

In a previous exercise, you wrote a unit test for the function convert_to_int(), which is supposed to convert a comma separated integer string like "2,081" to the integer 2081. You also ran the unit test and discovered that it is failing.

In this exercise, you will read the test result report from that exercise in detail, and then spot and fix the bug. This would equip you with all basic skills to start using unit tests for your projects.

The convert_to_int() function is defined in the file preprocessing_helpers.py. The unit test is available in the test module test_convert_to_int.py.

Instructions 1/2
50 XP

Question

Run the unit test in the test module test_convert_to_int.py in the IPython console. Read the test result report and spot the bug.

Which of the following describes the bug in the function convert_to_int(), if any?

Possible Answers :

    - convert_to_int("2,081") is expected to return the string "2081", but it is actually returning the integer 2081.

    - convert_to_int("2,081") is expected to return the integer 2081, but it is actually returning the string "2081".

    - convert_to_int("2,081") is expected to return the integer 2081, but it is actually returning the string "2,081".

    - The function convert_to_int() does not have a bug.

Answer : convert_to_int("2,081") is expected to return the integer 2081, but it is actually returning the string "2081".



'''


'''
Instructions 2/2
50 XP

- Fix the convert_to_int() function so that it returns the integer 2081 instead of the string "2081" for the argument "2,081".

'''


def convert_to_int(string_with_comma):
    return int(string_with_comma.replace(",", ""))
