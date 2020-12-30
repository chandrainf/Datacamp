'''
Read-only properties


The LoggedDF class from Chapter 2 was an extension of the pandas DataFrame class that had an additional created_at attribute that stored the timestamp when the DataFrame was created, so that the user could see how out-of-date the data is.

But that class wasn't very useful: we could just assign any value to created_at after the DataFrame was created, thus defeating the whole point of the attribute! Now, using properties, we can make the attribute read-only.

The LoggedDF class from Chapter 2 is available for you in the script pane.

Instructions
100 XP

Use the "Run code" button to run the code and verify that it's possible to assign an arbitrary value to created_at.

- Modify the code to make the created_at attribute into a read-only property. Don't forget the internal attribute!

Use "Run code" again to verify that assignment now causes an error.

- Put the code assigning a value to ldf.created_at into a try-except block that catches AttributeError exception and prints "Could not set attribute!" when the exception is caught.

'''
import pandas as pd
from datetime import datetime

# MODIFY the class to turn created_at into a read-only property


class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self._created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self._created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)

    @property
    def created_at(self):
        return self._created_at


ldf = LoggedDF({"col1": [1, 2], "col2": [3, 4]})

# Put into try-except block to catch AtributeError and print a message
try:
    ldf.created_at = '2035-07-13'
except AttributeError:
    print("Could not set attribute")
