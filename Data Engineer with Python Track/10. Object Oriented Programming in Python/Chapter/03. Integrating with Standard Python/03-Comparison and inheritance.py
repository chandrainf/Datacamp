'''
Comparison and inheritance


What happens when an object is compared to an object of a child class? Consider the following two classes:

    class Parent:
        def __eq__(self, other):
            print("Parent's __eq__() called")
            return True

    class Child(Parent):
        def __eq__(self, other):
            print("Child's __eq__() called")
            return True

The Child class inherits from the Parent class, and both implement the __eq__() method that includes a diagnostic printout.

Instructions 1/1
100 XP

Question

Which __eq__() method will be called when the following code is run?

    p = Parent()
    c = Child()

    p == c 

Feel free to experiment in the console -- the classes have already been defined for you.

Possible Answers :

    - Parent's __eq__() method will be called.

    - Child's __eq__() method will be called.

    - The code will cause an error.

Answer : Child's __eq__() method will be called.

'''
