'''
Method inheritance

Inheritance is powerful because it allows us to reuse and customize code without rewriting existing code. By calling methods of the parent class within the child class, we reuse all the code in those methods, making our code concise and manageable.

In this exercise, you'll continue working with the Manager class that is inherited from the Employee class. You'll add new data to the class, and customize the give_raise() method from Chapter 1 to increase the manager's raise amount by a bonus percentage whenever they are given a raise.

A simplified version of the Employee class, as well as the beginning of the Manager class from the previous lesson is provided for you in the script pane.

Instructions 1/2
50 XP

Add a constructor to Manager that:

- accepts name, salary (default 50000), and project (default None)
- calls the constructor of the Employee class with the name and salary parameters,
- creates a project attribute and sets it to the project parameter.

'''


class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):
  # Add a constructor
    def __init__(self, name, salary=50000, project=None):

        # Call the parent's constructor
        Employee.__init__(self, name, salary)

        # Assign project attribute
        self.project = project

    def display(self):
        print("Manager ", self.name)


'''
Instructions 2/2
50 XP

Add a give_raise() method to Manager that:

-accepts the same parameters as Employee.give_raise(), plus a bonus parameter with the default value of 1.05 (bonus of 5%),
-multiplies amount by bonus,
-uses the Employee's method to raise salary by that product.

'''


class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self, amount, bonus=1.05):

        Employee.give_raise(self, amount * bonus)


mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)
