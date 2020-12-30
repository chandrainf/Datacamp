'''
A simple while loop


A while loop is another control structure, like if/else. while lets us automate the repetition of instructions to make our code more readable and concise.

In this exercise, you will write a while loop that loops three times. Using an incrementing counter variable and if/else logic, you will print "winner" in the first iteration of the loop, "winner" again in the second iteration, and "chicken dinner" in the third and final iteration. This printed message won't be used in the Twenty-One program exactly, though it could be used in the context of congratulating a player if they win a round.

Instructions
100 XP

- Define a counter variable, i, equal to zero.
- Define the number of iterations for the while loop, numRepetitions, equal to three.
- Fill out the first if clause so "winner" is printed in the first iteration of the loop, then "winner" again in the second iteration, and "chicken dinner" in the final iteration.
- Increment the counter variable by one.

'''
// Define counter variable
var i = 0

// Define the number of loop iterations
val numRepetitions = 3

// Loop to print a message for winner of the round
while (i < numRepetitions) {
    if (i < 2)
    println("winner")
    else
    println("chicken dinner")
    // Increment the counter variable
    i = i+1
}
