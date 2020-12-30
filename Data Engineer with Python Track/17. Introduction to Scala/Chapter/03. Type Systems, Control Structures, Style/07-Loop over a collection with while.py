'''
Loop over a collection with while


The while construct causes the block of code between its curly braces to be executed repeatedly until the boolean expression at the top becomes false.

In the previous lesson, you created the body of the pointsToBust function to calculate the specific number of points. In this exercise, you'll write a while loop that loops through five hands (one for each player in the game) and finds the number of points to bust for each. Writing this while loop instead of calling the pointsToBust function five times makes our program more concise and readable.

Instructions
100 XP

- Define a counter variable, i. Set it equal to zero to start.
- Using the counter variable i, write a while loop that proceeds through the loop hands.length times.
- Find and print the winning hand's value for the ith hand.
- Increment the counter variable.

'''
// Define counter variable
var i = 0

// Create list with five hands of Twenty-One
var hands = List(16, 21, 8, 25, 4)

// Loop through hands
while (i < hands.length) {
    // Find and print number of points to bust
    println(pointsToBust(hands(i)))
    // Increment the counter variable
    i += 1
}
