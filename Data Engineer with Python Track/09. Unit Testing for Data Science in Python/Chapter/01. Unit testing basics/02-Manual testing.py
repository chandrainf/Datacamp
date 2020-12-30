'''
Manual testing


The function row_to_list(), which you met in the video lesson, has the following expected return values for the arguments listed below.

Argument	            Expected return value	    Explanation
"2,081\t314,942\n"	    ["2,081", "314,942"]	    Correct row format
"\t293,410\n"	        None	                    Missing area
"1,463238,765\n"	    None	                    Missing tab separator

row_to_list() has been defined and imported for you. Your job is to test the function manually in the IPython console.

While testing manually, notice how many times you have to repeat the same steps! The point is to experience the inefficiency of manual testing.

Instructions 1/2
50 XP

Question

Call row_to_list() in the IPython console on the three arguments listed in the table. Do the actual return values match the expected return values listed in the table?

Possible Answers :

    - Yes, the implementation returns the expected value in each case.

    - No, the function returns None for the argument "2,081\t314,942\n" instead of the expected return value ["2,081", "314,942"].

    - No. the function returns ["", "293,410"] for the argument "\t293,410\n" instead of the expected return value None.

    - No, the function returns False for the argument "1,463238,765\n" instead of the expected return value None.

Answer : No. the function returns ["", "293,410"] for the argument "\t293,410\n" instead of the expected return value None.

'''


'''
Instructions 2/2
50 XP

Question

In the last step, you discovered a bug in our implementation of row_to_list(). Good job!

We have implemented a corresponding bug fix in a new function row_to_list_bugfix(). Call row_to_list_bugfix() in the IPython console on the three arguments listed in the table. Do the actual return values now match the expected return values listed in the table?

Possible Answers :

    - Yes, the implementation returns the expected value in each case.

    - No, the function returns None for the argument "2,081\t314,942\n" instead of the expected return value ["2,081", "314,942"].

    - No. the function returns ["", "293,410"] for the argument "\t293,410\n" instead of the expected return value None.

    - No, the function returns False for the argument "1,463238,765\n" instead of the expected return value None..

Answer : Yes, the implementation returns the expected value in each case.

'''
