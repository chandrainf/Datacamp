'''
Call a function


Now it's time to actually use a function! As a reminder, here is the maxHand function that finds the maximum hand value between two hands (ignoring whether or not each hand busts):

  def maxHand(handA: Int, handB: Int): Int = {
    if (handA > handB) handA
    else handB
  }

In this exercise, you'll create a variable to add the cards in each hand together, then call maxHand and pass in those variables as arguments to determine the maximum hand value. The maxHand function and the card variables you need are already defined.

Instructions
100 XP

- Calculate the hand value for playerA, who has the following cards: queenDiamonds, threeClubs, aceHearts (worth 1), fiveSpades.
- Calculate the hand value for playerB, who has the following cards: kingHearts, jackHearts.
- Call the maxHand function, passing in handPlayerA and handPlayerB as arguments. Pass this function call into the println function to print out the maximum hand value.

'''
// Calculate hand values
var handPlayerA: Int = 19
var handPlayerB: Int = 20

// Find and print the maximum hand value
println(maxHand(handPlayerA, handPlayerB))
