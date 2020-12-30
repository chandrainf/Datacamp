'''
Write a class from scratch


You are a Python developer writing a visualization package. For any element in a visualization, you want to be able to tell the position of the element, how far it is from other elements, and easily implement horizontal or vertical flip .

The most basic element of any visualization is a single point. In this exercise, you'll write a class for a point on a plane from scratch.

Instructions
100 XP

Define the class Point that has:

- Two attributes, x and y - the coordinates of the point on the plane;
- A constructor that accepts two arguments, x and y, that initialize the corresponding attributes. These arguments should have default value of 0.0;
- A method distance_to_origin() that returns the distance from the point to the origin. The formula for that is /x2+y2 .
- A method reflect(), that reflects the point with respect to the x- or y-axis:
    - accepts one argument axis,
    - if axis="x" , it sets the y (not a typo!) attribute to the negative value of the y attribute,
    - if axis="y", it sets the x attribute to the negative value of the x attribute,
- for any other value of axis, prints an error message. Reflection of a point with respect to y and x axes

Note: You can choose to use sqrt() function from either the numpy or the math package, but whichever package you choose, don't forget to import it before starting the class definition!

To check your work, you should be able to run the following code without errors:

    pt = Point(x=3.0)
    pt.reflect("y")
    print((pt.x, pt.y))
    pt.y = 4.0
    print(pt.distance_to_origin())

and return the output

    (-3.0,0.0)
    5.0

'''
import math


class Point:

    # Constrctor to define the attributes
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def reflect(self, axis):

        if axis == "x":
            self.y = - self.y
        elif axis == "y":
            self.x = - self.x
        else:
            print("Invalid input, please input x or y")


pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())
