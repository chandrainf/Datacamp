'''
if expressions result in a value


In Scala, if is an expression, and expressions result in a value. That means the result of if can be assigned to a variable.

Imagine you're playing Twenty-One. You receive cards from the dealer and would like to know where your hand stands. If your hand is greater than 21, a "Bust!" message informing us of this result would be disappointing but helpful. If our hand is 21 exactly, the congratulatory "Twenty-One!" message applies. If less than 21, the program should ask us, "Hit or stay?"

In this exercise, you'll improve the code you wrote last exercise. You'll write an if-else if-else expression to store an appropriate message for the player's current hand in a variable. The card variables you need are already defined.

Instructions
100 XP

- Read the provided code, then fill in the type annotation for the informPlayer variable.
- Write appropriate if, else if, and else conditions based on the provided code.
- Change fiveSpades to fourSpades, then click "Run Code" and observe the output.
- Change fourSpades to threeSpades, then click "Submit Answer".

'''
// Point value of a player's hand
val hand = sevenClubs + kingDiamonds + threeSpades

// Inform a player where their current hand stands
val informPlayer: String = {
    if (hand > 21)
    "Bust! :("
    else if (hand == 21)
    "Twenty-One! :)"
    else
    "Hit or stay?"
}

// Print the message
print(informPlayer)
