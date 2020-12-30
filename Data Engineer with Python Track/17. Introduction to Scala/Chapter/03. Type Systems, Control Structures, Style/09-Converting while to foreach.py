'''
Converting while to foreach


Previously, you wrote a while loop in the imperative style to find and print the number of points to bust for five hands (one for each player) in a round of Twenty-One:

  // Define counter variable
  var i = 0

  // Create list with five hands of Twenty-One
  var hands = List(16, 21, 8, 25, 4)

  // Loop through hands
  while(i < hands.length) {
    // Find and print number of points to bust
    println(pointsToBust(hands(i)))
    // Increment the counter variable
    i += 1
  }
  
In this exercise, you'll convert that code to a more functional, Scala-preferred style using the foreach method. The bust function is already defined for you. A modified pointsToBust function (with println) is provided in the sample code.

Instructions
100 XP

-Call the foreach method on the hands array of arrays, looping through each round to find the number of points to bust using the pointsToBust function.

'''
// Find the number of points that will cause a bust


def pointsToBust(hand: Int) = {
    // If the hand is a bust, 0 points remain
    if (bust(hand))
    println(0)
    // Otherwise, calculate the difference between 21 and the current hand
    else
    println(21 - hand)
}


// Create list with five hands of Twenty-One
var hands = List(16, 21, 8, 25, 4)

// Loop through hands, finding each hand's number of points to bust
hands.foreach(pointsToBust)
