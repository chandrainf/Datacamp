'''
Using internal attibutes


In this exercise, you'll return to the BetterDate class of Chapter 2. Your date class is better because it will use the sensible convention of having exactly 30 days in each month.

You decide to add a method that checks the validity of the date, but you don't want to make it a part of BetterDate public interface.

The class BetterDate is available in the script pane.

Instructions
100 XP

- Add a class attribute _MAX_DAYS storing the maximal number of days in a month - 30.
- Add another class attribute storing the maximal number of months in a year - 12. Use the appropriate naming convention to indicate that this is an internal attribute.
- Add an _is_valid() method that returns True if the day and month attributes are less than or equal to the corresponding maximum values, and False otherwise. Make sure to refer to the class attributes by their names!

'''


class BetterDate:

    _MAX_DAYS = 30
    _MAX_MONTHS = 12

    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    # Add _is_valid() checking day and month values
    def _is_valid(self):

        return self.month <= BetterDate._MAX_MONTHS and self.day <= BetterDate._MAX_DAYS


bd1 = BetterDate(2020, 4, 30)
print(bd1._is_valid())

bd2 = BetterDate(2020, 6, 45)
print(bd2._is_valid())
