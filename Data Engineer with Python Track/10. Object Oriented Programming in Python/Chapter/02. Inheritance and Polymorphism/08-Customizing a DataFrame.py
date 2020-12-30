'''
Customizing a DataFrame

In your company, any data has to come with a timestamp recording when the dataset was created, to make sure that outdated information is not being used. You would like to use pandas DataFrames for processing data, but you would need to customize the class to allow for the use of timestamps.

In this exercise, you will implement a small LoggedDF class that inherits from a regular pandas DataFrame but has a created_at attribute storing the timestamp. You will then augment the standard to_csv() method to always include a column storing the creation date.

Tip: all DataFrame methods have many parameters, and it is not sustainable to copy all of them for each method you're customizing. The trick is to use variable-length arguments *args and **kwargsto catch all of them.

Instructions 1/2
50 XP

- Import pandas as pd.
- Define LoggedDF class inherited from pd.DataFrame.
- Define a constructor with arguments *args and **kwargs that:
    -calls the pd.DataFrame constructor with the same arguments,
    -assigns datetime.today() to self.created_at.    

'''
# Import pandas as pd
import pandas as pd

# Define LoggedDF inherited from pd.DataFrame and add the constructor


class LoggedDF(pd.DataFrame):

    def __init__(self, *args, **kwargs):

        pd.DataFrame.__init__(self, *args, **kwargs)
        self.created_at = datetime.today()


ldf = LoggedDF({"col1": [1, 2], "col2": [3, 4]})
print(ldf.values)
print(ldf.created_at)

'''
Instructions 2/2
50 XP

- Add a to_csv() method to LoggedDF that:
- copies self to a temporary DataFrame using .copy(),
- creates a new column created_at in the temporary DataFrame and fills it with self.created_at
- calls pd.DataFrame.to_csv() on the temporary variable.

'''
# Import pandas as pd

# Define LoggedDF inherited from pd.DataFrame and add the constructor


class LoggedDF(pd.DataFrame):

    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self.created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        # Copy self to a temporary DataFrame
        temp = self.copy()

        # Create a new column filled with self.created at
        temp["created_at"] = self.created_at

        # Call pd.DataFrame.to_csv on temp with *args and **kwargs
        pd.DataFrame.to_csv(temp, *args, **kwargs)
