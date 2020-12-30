'''
Inheritance of class attributes

In the beginning of this chapter, you learned about class attributes and methods that are shared among all the instances of a class. How do they work with inheritance?

In this exercise, you'll create subclasses of the Player class from the first lesson of the chapter, and explore the inheritance of class attributes and methods.

The Player class has been defined for you. Recall that the Player class had two class-level attributes: MAX_POSITION and MAX_SPEED, with default values 10 and 3.

Instructions 1/2
50 XP

- Create a class Racer inherited from Player,
- Assign 5 to MAX_SPEED in the body of the class.
- Create a Player object p and a Racer object r (no arguments needed for the constructor).

Examine the printouts carefully. Next step is a quiz!

'''
# Create a Racer class and set MAX_SPEED to 5


class Racer(Player):

    MAX_SPEED = 5


# Create a Player and a Racer objects
p = Player()
r = Racer()

print("p.MAX_SPEED = ", p.MAX_SPEED)
print("r.MAX_SPEED = ", r.MAX_SPEED)

print("p.MAX_POSITION = ", p.MAX_POSITION)
print("r.MAX_POSITION = ", r.MAX_POSITION)

'''
Instructions 2/2
50 XP

Question :

Which of the following statements about inheritance of class attributes is correct?

Possible Answers:

    -Class attributes CANNOT be inherited, but new class attributes of the same name CAN be created in a child class.

    -Class attributes CANNOT be inherited, and new class attributes of the same name CANNOT be created in a child class.

    -Class attributes CAN be inherited, and the value of class attributes CAN be overwritten in the child class

    -Class attributes can be inherited, and the value of class attributes CANNOT be overwritten in the child class

Answer : Class attributes CAN be inherited, and the value of class attributes CAN be overwritten in the child class

'''
