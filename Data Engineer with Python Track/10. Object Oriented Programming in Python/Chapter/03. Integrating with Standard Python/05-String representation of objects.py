'''
String representation of objects


There are two special methods in Python that return a string representation of an object. __str__() is called when you use print() or str() on an object, and __repr__() is called when you use repr() on an object, print the object in the console without calling print(), or instead of __str__() if __str__() is not defined.

__str__() is supposed to provide a "user-friendly" output describing an object, and __repr__() should return the expression that, when evaluated, will return the same object, ensuring the reproducibility of your code.

In this exercise, you will continue working with the Employee class from Chapter 2.

Instructions 1/2
50 XP

Add the __str__() method to Employee that satisfies the following:

- If emp is an Employee object with name "Amar Howard" and salary of 40000, then print(emp) outputs

    Employee name: Amar Howard
    Employee salary: 40000

'''


class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    # Add the __str__() method
    def __str__(self):
        output = """
        Employee name:{name}
        Employee salary:{salary}
        """.format(name=self.name, salary=self.salary)
        return output


emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)


'''
Instructions 2/2
50 XP

Add the __repr__() method to Employee that satisfies the following:

- If emp is an Employee object with name "Amar Howard" and salary of 40000, then repr(emp) outputs

    Employee("Amar Howard", 40000)

'''


class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(
            name=self.name, salary=self.salary)
        return s

    # Add the __repr__method
    def __repr__(self):

        return "Employee(\"{name}\", {salary})".format(name=self.name, salary=self.salary)


emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))
