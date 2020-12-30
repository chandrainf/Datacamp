'''
Replacing .iloc with underlying arrays


Now that you have a better grasp on a DataFrame's internals let's update one of your previous analyses to leverage a DataFrame's underlying arrays. You'll revisit the win percentage calculations you performed row by row with the .iloc method:

    def calc_win_perc(wins, games_played):
        win_perc = wins / games_played
        return np.round(win_perc,2)

    win_percs_list = []

    for i in range(len(baseball_df)):
        row = baseball_df.iloc[i]

        wins = row['W']
        games_played = row['G']

        win_perc = calc_win_perc(wins, games_played)

        win_percs_list.append(win_perc)

    baseball_df['WP'] = win_percs_list

Let's update this analysis to use arrays instead of the .iloc method. A DataFrame (baseball_df) has been loaded into your session.

Instructions 1/3
35 XP

Use the right method to collect the underlying 'W' and 'G' arrays of baseball_df and pass them directly into the calc_win_perc() function. Store the result as a variable called win_percs_np.

'''
# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)


'''
Instructions 2/3
35 XP

Create a new column in baseball_df called 'WP' that contains the win percentages you just calculated.

'''
# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np
print(baseball_df.head())


'''
Instructions 3/3
50 XP

Question

Use timeit in cell magic mode within your IPython console to compare the runtimes between the old code block using .iloc and the new code you developed using NumPy arrays.

Don't include the code that defines the calc_win_perc() function or the print() statements or when timing.

You should include eight lines of code when timing the old code block and two lines of code when timing the new code you developed. You may need to press SHIFT+ENTER when using timeit in cell magic mode to get to a new line within your IPython console.

Which approach was the faster?

Possible Answers

    - The original code with .iloc is much faster than using NumPy arrays

    - The old code block with .iloc and the new code with NumPy arrays have similar runtimes.

    - The NumPy array approach is faster than the .iloc approach.

Answer : The NumPy array approach is faster than the .iloc approach.

'''
