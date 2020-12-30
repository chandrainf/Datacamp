'''
if and printing


The if/else control structure allows you to chose the way your program control flows. You don't always need else, as you'll experience in this exercise.

If a player reaches 21 points, they'd probably appreciate a little recognition!

In this exercise, you'll use the if keyword to print a congratulations when a player's hand equals 21. Remember, when there is no else, use curly braces for good Scala style! The card variables you need are already defined.

Instructions
100 XP

- Write code that accomplishes the following: if a player's hand is equal to 21, print "Twenty-One!" to output.
- Click "Run Code" and observe the output.
- Change fourSpades to threeSpades, then click "Submit Answer".

'''
// Point value of a player's hand
val hand = sevenClubs + kingDiamonds + threeSpades

// Congratulate the player if they have reached 21

if (hand == 21) {
    println("Twenty-One!")
}
