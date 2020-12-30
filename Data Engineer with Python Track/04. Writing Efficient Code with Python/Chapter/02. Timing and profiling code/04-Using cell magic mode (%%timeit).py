'''
Using cell magic mode (%%timeit)


From here on out, you'll be working with a superheroes dataset. For this exercise, a list of each hero's weight in kilograms (called wts) is loaded into your session. You'd like to convert these weights into pounds.

You could accomplish this using the below for loop:

    hero_wts_lbs = []
    for wt in wts:
        hero_wts_lbs.append(wt * 2.20462)

Or you could use a numpy array to accomplish this task:

    wts_np = np.array(wts)
    hero_wts_lbs_np = wts_np * 2.20462

Use %%timeit in your IPython console to compare runtimes between these two approaches. Make sure to press SHIFT+ENTER after the magic command to add a new line before writing the code you wish to time. After you've finished coding, answer the following question:

Which of the above techniques is faster?

Instructions
50 XP

Possible Answers

    - The for loop technique was faster.

    - The numpy technique was faster.

    - Both techniques had similar runtimes.

Answer : The numpy technique was faster.

'''
