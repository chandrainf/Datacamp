'''
Fix the plotting function

In the last exercise, pytest saved the baseline images, actual images, and images containing the pixelwise difference in a temporary folder. The difference image for one of the tests test_on_almost_linear_data() is shown below.



The black areas are where the actual image and the baseline matches. The white areas are where they don't match.

This clearly tells us that something is wrong with the axis labels. Take a look at the plots section to see the baseline (plot 1/2) and the actual plot (plot 2/2). Based on that, it's your job to fix the plotting function.

Instructions 1/2
50 XP

- Fill in the axis labels xlabel and ylabel so that they match the baseline plot (plot 1/2).

'''
import matplotlib.pyplot as plt
import numpy as np


def get_plot_for_best_fit_line(slope, intercept, x_array, y_array, title):
    fig, ax = plt.subplots()
    ax.plot(x_array, y_array, ".")
    ax.plot([0, np.max(x_array)], [intercept,
                                   slope * np.max(x_array) + intercept], "-")
    # Fill in with axis labels so that they match the baseline
    ax.set(xlabel='area (square feet)', ylabel="price (dollars)", title=title)
    return fig


'''
Instructions 2/2
50 XP
Question

Now that you have fixed the function, run all the tests in the tests directory, remembering that the current working directory in the IPython console is tests. What is the outcome?

Possible Answers

    - All 25 tests pass.

    - 22 tests are passing and 3 are failing.

    - 24 tests are passing and 1 is failing.

Answer : All 25 tests pass.

'''
