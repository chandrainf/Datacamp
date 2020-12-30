'''
Changing class attributes

You learned how to define class attributes and how to access them from class instances. So what will happen if you try to assign another value to a class attribute when accessing it from an instance? The answer is not as simple as you might think!

The Player class from the previous exercise is pre-defined. Recall that it has a position instance attribute, and MAX_SPEED and MAX_POSITION class attributes. The initial value of MAX_SPEED is 3.

Instructions 1/2
50 XP

- Create two Player objects p1 and p2.
- Print p1.MAX_SPEED and p2.MAX_SPEED.
- Assign 7 to p1.MAX_SPEED.
- Print p1.MAX_SPEED and p2.MAX_SPEED again.
- Print Player.MAX_SPEED.
- Examine the output carefully.

'''
# Create Players p1 and p2
p1 = Player()
p2 = Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# Assign 7 to p1.MAX_SPEED
p1.MAX_SPEED = 7


print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)

'''
Instructions 2/2
50 XP

Even though MAX_SPEED is shared across instances, assigning 7 to p1.MAX_SPEED didn't change the value of MAX_SPEED in p2, or in the Player class.

So what happened? In fact, Python created a new instance attribute in p1, also called it MAX_SPEED, and assigned 7 to it, without touching the class attribute.

Now let's change the class attribute value for real.

-Modify the assignment to assign 7 to Player.MAX_SPEED instead.

'''
# Create Players p1 and p2
p1, p2 = Player(), Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# ---MODIFY THIS LINE---
Player.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)
