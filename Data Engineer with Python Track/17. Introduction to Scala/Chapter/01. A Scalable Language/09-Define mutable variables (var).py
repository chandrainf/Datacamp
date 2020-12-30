'''
Define mutable variables (var)


Scala has two kinds of variables: val and var. var are mutable and can be reassigned.

In Twenty-One, an ace is like a var, as it can be worth 1 or 11 points depending on the player's choice (as opposed to cards 2 through king, which have a constant point value throughout the game).

In this exercise, you will define each ace as a var of type Int set to a default value of 1 point. This time around, you'll leverage Scala's type inference (its ability to guess types based on supplied values) and omit the type annotation.

Instructions
100 XP

- Define four mutable variables, all of type Int and equal to 1: aceClubs, aceDiamonds, aceHearts, aceSpades.

'''
// Define mutable variables for all aces
var aceClubs: Int = 1
var aceDiamonds: Int = 1
var aceHearts: Int = 1
var aceSpades: Int = 1
