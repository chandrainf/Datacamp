'''
Square and rectangle

The classic example of a problem that violates the Liskov Substitution Principle is the Circle-Ellipse problem, sometimes called the Square-Rectangle problem.

By all means, it seems like you should be able to define a class Rectangle, with attributes h and w (for height and width), and then define a class Square that inherits from the Rectangle. After all, a square "is-a" rectangle!

Unfortunately, this intuition doesn't apply to object-oriented design.

Instructions 1/4
25 XP

- Create a class Rectangle with a constructor that accepts two parameters, h and w, and sets its h and w attributes to the values of h and w.
- Create a class Square inherited from Rectangle with a constructor that accepts one parameter w, and sets both the h and w attributes to the value of w.

'''
# Define a Rectangle class


class Rectangle:

    def __init__(self, h, w):
        self.h = h
        self.w = w

# Define a Square class


class Square(Rectangle):

    def __init__(self, w):

        Rectangle.__init__(self, w, w)


'''
Instructions 2/4
25 XP

Question :

The classes are defined for you. Experiment with them in the console.

For example, in the console or the script pane, create a Square object with side length 4. Then try assigning 7 to the h attribute.

What went wrong with these classes?

Possible Answers

    - This wasn't a correct use of inheritance: we did not call the parent constructor in the child constructor.

    - We cannot set the h attribute to 7 in the Square object because it will cause an error.

    - The 4x4 Square object would no longer be a square if we assign 7 to h.

    - Because a Square only has one side length, it should not have the h attribute. We should not have included the h attribute in the constructor.

    - All of the above.

Answer : The 4x4 Square object would no longer be a square if we assign 7 to h.

'''

'''
Instructions 3/4
25 XP

A Square inherited from a Rectangle will always have both the h and w attributes, but we can't allow them to change independently of each other.

- Define methods set_h() and set_w() in Rectangle, each accepting one parameter and setting h and w.
- Define methods set_h() and set_w() in Square, each accepting one parameter, and setting both h and w to that parameter in both methods.

'''


class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h

# Define set_h to set h
    def set_h(self, h):
        self.h = h

# Define set_w to set w
    def set_w(self, w):
        self.w = w


class Square(Rectangle):
    def __init__(self, w):
        self.w, self.h = w, w

# Define set_h to set w and h
    def set_h(self, h):
        self.h = h
        self.w = h

# Define set_w to set w and h
    def set_w(self, w):
        self.w = w
        self.h = w


'''
Instructions 4/4
25 XP

Question :

Later in this chapter you'll learn how to make these setter methods run automatically when attributes are assigned new values, don't worry about that for now, just assume that when we assign a value to h of a square, now the w attribute will be changed accordingly.

How does using these setter methods violate Liskov Substitution principle?

Possible Answers :

    - There are syntactic inconsistencies.

    - Each of the setter methods of Square change both h and w attributes, while setter methods of Rectangle change only one attribute at a time, so the Square objects cannot be substituted for Rectangle into programs that rely on one attribute staying constant.

    - The setter methods of Square accept only limited range of parameters, unlike the setter methods of Rectangle, so the Square objects cannot be substituted for Rectangle into programs that use parameter values outside that range.

    - All of the above.

Answer : Each of the setter methods of Square change both h and w attributes, while setter methods of Rectangle change only one attribute at a time, so the Square objects cannot be substituted for Rectangle into programs that rely on one attribute staying constant.

'''
