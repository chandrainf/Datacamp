'''
Generate the baseline image


In this exercise, you will get one step closer to the real thing. During this whole course, you've built a library of tests using a Python script and an IPython console. In real life, you're more likely to use an IDE (Integrated Development Environment), that lets you write scripts in the language you want, organize them into your directories, and execute shell commands. Basically, an IDE increases your productivity by gathering the most common activities of software development into a single application: writing source code, executing, and debugging.

Here, you can see the directory you've built on the left pane. The upper right pane is where you will write your Python scripts, and the bottom right pane is a shell console, which replaces the IPython console you've used so far.

Parts of an integrated development environment

In this exercise, you will test the function introduced in the video get_plot_for_best_fit_line() on another set of test arguments. Here is the test data.

    1.0    3.0
    2.0    8.0
    3.0    11.0

The best fit line that the test will draw follows the equation y=5x-2. Two points, (1.0, 3.0) and (2.0, 8.0) will fall on the line. The point (3.0, 11.0) won't. The title of the plot will be "Test plot for almost linear data".

The test is called test_plot_for_almost_linear_data() and it's your job to complete the test and generate the baseline image. pytest, numpy as np and get_plot_for_best_fit_line has been imported for you.

Instructions
100XP

- Add the correct pytest marker that helps in generating baselines and comparing images.
- Return the matplotlib figure returned by the function under test.
- The test that you wrote was written to a test class TestGetPlotForBestFitLine in the test module visualization/test_plots.py. In the shell console, execute the command required to create the baseline image for this test only. The baseline folder should be in project/tests/visualization. Because it's a shell console and not an IPython one, you don't need to use the ! at the beginning of your command. Once you've ran your command and created your baseline, click Submit Answer.

'''

import pytest
import numpy as np

from visualization.plots import get_plot_for_best_fit_line


class TestGetPlotForBestFitLine(object):
    # Add the pytest marker which generates baselines and compares images
    @pytest.mark.mpl_image_compare
    def test_plot_for_almost_linear_data(self):
        slope = 5.0
        intercept = -2.0
        x_array = np.array([1.0, 2.0, 3.0])
        y_array = np.array([3.0, 8.0, 11.0])
        title = "Test plot for almost linear data"
        # Return the matplotlib figure returned by the function under test
        return get_plot_for_best_fit_line(slope, intercept, x_array, y_array, title)


'''
note : # After completing the test_plots.py script, run the following command in the shell:

pytest --mpl-generate-path /home/repl/workspace/project/tests/visualization/baseline -k "test_plot_for_almost_linear_data"
'''
