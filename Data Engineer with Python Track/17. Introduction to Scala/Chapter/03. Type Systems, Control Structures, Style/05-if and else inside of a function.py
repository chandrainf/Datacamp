'''
if and else inside of a function


Since if expressions result in values, they can be the result of functions, which also result in values.

In this exercise, you'll create the body a function for your Twenty-One program called pointsToBust, which takes the current hand's point value as an input and calculates the the number of points remaining until 21. As a player, knowing how many additional points it takes to cause your current hand to bust will help you decide whether to hit or stay. The card variables you need and the bust function are already defined for you.

Instructions
100 XP

- Write an if condition: if the hand busts, make the Int 0 the result of the function.
- Write an else condition: if the hand does not bust, subtract hand from 21 and make that difference the result of the function.
- Call pointsToBust with a hand with the cards tenSpades and fiveClubs as the argument.

'''
// Find the number of points that will cause a bust


def pointsToBust(hand: Int): Int = {
    // If the hand is a bust, 0 points remain
    if (bust(hand))
    0
    // Otherwise, calculate the difference between 21 and the current hand
    else
    21 - hand
}


// Test pointsToBust with 10♠ and 5♣
val myHandPointsToBust = pointsToBust(tenSpades + fiveClubs)
println(myHandPointsToBust)
