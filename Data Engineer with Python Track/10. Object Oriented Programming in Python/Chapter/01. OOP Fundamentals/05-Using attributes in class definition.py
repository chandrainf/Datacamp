'''
Using attributes in class definition

In the previous exercise, you defined an Employee class with two attributes and two methods setting those attributes. This kind of method, aptly called a setter method, is far from the only possible kind. Methods are functions, so anything you can do with a function, you can also do with a method. For example, you can use methods to print, return values, make plots, and raise exceptions, as long as it makes sense as the behavior of the objects described by the class (an Employee probably wouldn't have a pivot_table() method).

In this exercise, you'll go beyond the setter methods and learn how to use existing class attributes to define new methods. The Employee class and the emp object from the previous exercise are in your script pane.

Instructions 1/3
35 XP

- Print the salary attribute of emp.
- Attributes aren't read-only: use assignment (equality sign) to increase the salary attribute of emp by 1500, and print it again.

'''


class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary


emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Print the salary attribute of emp
print(emp.salary)

# Increase salary of emp by 1500
emp.salary = emp.salary + 1500

# Print the salary attribute of emp again
print(emp.salary)

'''
Instructions 2/3
35 XP

Raising a salary for an employee is a common pattern of behavior, so it should be part of the class definition instead.

Add a method give_raise() to Employee that increases the salary by the amount passed to give_raise() as a parameter.

'''


class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary

    # Add a give_raise() method with raise amount as a parameter
    def give_raise(self, given_rais_sal):
        self.salary += given_rais_sal


emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

print(emp.salary)
emp.give_raise(1500)
print(emp.salary)

'''

Instructions 3/3
30 XP

Methods don't have to just modify the attributes - they can return values as well!

- Add a method monthly_salary() that returns the value of the .salary attribute divided by 12.
- Call .monthly_salary() on emp, assign it to mon_sal, and print.

'''


class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary

    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary/12.0


emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary()

# Print mon_sal
print(mon_sal)
