'''
Class-level attributes

Class attributes store data that is shared among all the class instances. They are assigned values in the class body, and are referred to using the ClassName. syntax rather than self. syntax when used in methods.

In this exercise, you will be a game developer working on a game that will have several players moving on a grid and interacting with each other. As the first step, you want to define a Player class that will just move along a straight line. Player will have a position attribute and a move() method. The grid is limited, so the position of Player will have a maximal value.

Instructions 1/2
50 XP

- Define a class Player that has:
- A class attribute MAX_POSITION with value 10.
- The __init__() method that sets the position instance attribute to 0.
- Print Player.MAX_POSITION.
-Create a Player object p and print its MAX_POSITION.

'''

# Create a Player class


class Player:

    # Class Attributes
    MAX_POSITION = 10

    def __init__(self):
        self.position = 0


# Print Player.MAX_POSITION
print(Player.MAX_POSITION)

# Create a player p and print its MAX_POSITITON

p = Player()

print(p.MAX_POSITION)

'''
Instructions 2/2
50 XP

Add a move() method with a steps parameter such that:

-if position plus steps is less than MAX_POSITION, then add steps to position and assign the result back to position;
-otherwise, set position to MAX_POSITION.
Take a look at the console for a visualization!

'''


class Player:
    MAX_POSITION = 10

    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    def move(self, steps):

        if(self.position + steps < Player.MAX_POSITION):
            self.position += steps
        else:
            self.position = Player.MAX_POSITION

    # This method provides a rudimentary visualization in the console

    def draw(self):
        drawing = "-" * self.position + "|" + "-" * \
            (Player.MAX_POSITION - self.position)
        print(drawing)


p = Player()
p.draw()
p.move(4)
p.draw()
p.move(5)
p.draw()
p.move(3)
p.draw()
