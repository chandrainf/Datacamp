'''
Run the tests for the plotting function

Shortly after the baseline image was generated, one of your colleagues modified the plotting function. You have to run the tests in order to check whether the function still works as expected.

Remember the following:

    -The tests were housed in a test class TestGetPlotForBestFitLine in the test module visualization/test_plots.py. You can specify this test class in the pytest command by either using its node ID or the -k command line flag.
    -To ensure plots are compared to the baseline during testing, the pytest command must include a special command line flag that comes from the pytest-mpl package.

Instructions
100XP

Run the tests in this test class in the console. Because it's a shell console and not an IPython one, you don't need to use the ! at the beginning of your command. You should see two failures.

'''

# run the following command in the shell:
pytest - k "TestGetPlotForBestFitLine" - -mpl
