'''
Place test modules at the correct location


A data science project without visualization is like pizza without cheese, right? But this has been fixed by creating a package called visualization under the top level application directory src.

src/                                    # All application code lives here
|-- visualization/                      # Package for visualization
    |-- __init__.py
    |-- plots.py                        # Module for plotting

In the package, there is a Python module plots.py, which contain functions related to plotting. These functions should be tested in a test module test_plots.py.

According to pytest guidelines, where should you place this test module within the project structure?

Answer the question
50XP

Possible Answers :

    - src/visualization/test_plots.py.

    - src/visualization/tests/test_plots.py.

    - tests/test_plots.py.

    - tests/visualization/test_plots.py.

Answer : tests/visualization/test_plots.py.

'''
