'''
Create your first class

Time to write your first class! In this exercise, you'll start building the Employee class you briefly explored in the previous lesson. You'll start by creating methods that set attributes, and then add a few methods that manipulate them.

As mentioned in the first video, an object-oriented approach is most useful when your code involves complex interactions of many objects. In real production code, classes can have dozens of attributes and methods with complicated logic, but the underlying structure is the same as with the most simple class.

Your classes in this course will only have a few attributes and short methods, but the organizational principles behind the them will be directly translatable to more complicated code.

Instructions 1/3
35 XP

- Create an empty class Employee.
- Create an object emp of the class Employee by calling Employee().
Try printing the .name attribute of emp object in the console. What happens?
'''

# Create an empty class Employee


class Employee:
    pass


# Create an object emp of class Employee
emp = Employee()

'''
Instructions 2/3
35 XP

-Modify the Employee class to include a .set_name() method that takes a new_name argument, and assigns new_name to the .name attribute of the class.
-Use the set_name() method on emp to set the name to 'Korel Rossi'.
-Print emp.name.

'''
# Include a set_name method


class Employee:

    def set_name(self, new_name):
        self.name = new_name


# Create an object emp of class Employee
emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Print the name of emp
print(emp.name)


'''
Instructions 3/3
30 XP

- Follow the pattern to add another method - set_salary() - that will set the salary attribute of the class to the parameter new_salary passed to method.
- Set the salary of emp to 50000.
Try printing emp.salary before and after calling set_salary().

'''


class Employee:

    def set_name(self, new_name):
        self.name = new_name

    # Add set_salary() method
    def set_salary(self, new_salary):
        self.salary = new_salary


# Create an object emp of class Employee
emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)
