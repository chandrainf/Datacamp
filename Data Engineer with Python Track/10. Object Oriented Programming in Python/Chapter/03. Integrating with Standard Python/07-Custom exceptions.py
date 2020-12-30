'''
Custom exceptions


You don't have to rely solely on built-in exceptions like IndexError: you can define your own exceptions more specific to your application. You can also define exception hierarchies. All you need to define an exception is a class inherited from the built-in Exception class or one of its subclasses.

In Chapter 1, you defined an Employee class and used print statements and default values to handle errors like creating an employee with a salary below the minimum or giving a raise that is too big. A better way to handle this situation is to use exceptions. Because these errors are specific to our application (unlike, for example, a division by zero error which is universal), it makes sense to use custom exception classes.

Instructions 1/3
35 XP

- Define an empty class SalaryError inherited from the built-in ValueError class.
- Define an empty class BonusError inherited from the SalaryError class.

'''

# Define SalaryError inherited from ValueError


class SalaryError(ValueError):
    pass

# Define BonusError inherited from SalaryError


class BonusError(SalaryError):
    pass


'''
Instructions 2/3
35 XP

- Complete the definition of __init__() to raise a SalaryError with the message "Salary is too low!" if the salary parameter is less than MIN_SALARY class attribute.

There's no need for else because raise terminates the program anyway.

'''


class SalaryError(ValueError):
    pass


class BonusError(SalaryError):
    pass


class Employee:
    MIN_SALARY = 30000
    MAX_RAISE = 5000

    def __init__(self, name, salary=30000):
        self.name = name

        # If salary is too low
        if self.salary < Employee.MIN_SALARY:
            # Raise a SalaryError exception
            raise SalaryError("Salary is too low!")

        self.salary = salary


'''
Instructions 3/3
30 XP

Examine the give_bonus() method, and the rewrite it using exceptions instead of print statements:

- raise a BonusError if the bonus amount is too high;
- raise a SalaryError if the result of adding the bonus would be too low.

'''


class SalaryError(ValueError):
    pass


class BonusError(SalaryError):
    pass


class Employee:
    MIN_SALARY = 30000
    MAX_BONUS = 5000

    def __init__(self, name, salary=30000):
        self.name = name
        if salary < Employee.MIN_SALARY:
            raise SalaryError("Salary is too low!")
        self.salary = salary

    # Rewrite using exceptions
    def give_bonus(self, amount):
        if amount > Employee.MAX_BONUS:
            raise BonusError("The bonus amount is too high!")

        elif self.salary + amount < Employee.MIN_SALARY:
            raise SalaryError("The salary after bonus is too low!")

        else:
            self.salary += amount
