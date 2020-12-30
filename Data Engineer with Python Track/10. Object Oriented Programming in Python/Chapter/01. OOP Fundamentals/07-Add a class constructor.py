'''
Add a class constructor


In this exercise, you'll continue working on the Employee class. Instead of using the methods like set_salary() that you wrote in the previous lesson, you will introduce a constructor that assigns name and salary to the employee at the moment when the object is created.

You'll also create a new attribute -- hire_date -- which will not be initialized through parameters, but instead will contain the current date.

Initializing attributes in the constructor is a good idea, because this ensures that the object has all the necessary attributes the moment it is created.

Instructions 1/3
35 XP

Define the class Employee with a constructor __init__() that:

    - accepts two arguments, name and salary (with default value0),
    - creates two attributes, also called name and salary,
    - sets their values to the corresponding arguments.

'''
from datetime import datetime


class Employee:
    # Create __init__() method
    def __init__(self, name, salary=0):
        # Create the name and salary attributes
        self.name = name
        self.salary = salary

    # From the previous lesson
    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary/12


emp = Employee("Korel Rossi")
print(emp.name)
print(emp.salary)


'''
Instructions 2/3
35 XP

The __init__() method is a great place to do preprocessing.

- Modify __init__() to check whether the salary parameter is positive:
    -if yes, assign it to the salary attribute,
    -if not, assign 0 to the attribute and print "Invalid salary!".

'''


class Employee:

    def __init__(self, name, salary=0):
        self.name = name
        # Modify code below to check if salary is positive
        if salary >= 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")
   # ...Other methods omitted for brevity ...


emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

'''
Instructions 3/3
30 XP

- Import datetime from the datetime module. This contains the function that returns current date.
- Add an attribute hire_date and set it to datetime.today().

'''


class Employee:

    def __init__(self, name, salary=0):
        self.name = name
        if salary > 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")

        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()

   # ...Other methods omitted for brevity ...


emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)
