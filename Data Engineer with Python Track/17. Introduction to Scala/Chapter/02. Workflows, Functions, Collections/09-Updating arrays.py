'''
Updating arrays


Since arrays are mutable, the elements in them can be updated.

In the context of Twenty-One, this could mean adding to an element in the array if that player chooses to hit to get closer to 21.

In this exercise, you'll do just that. The card variables you need are already defined, as well as the hands array you created, parameterized, and initialized previously.

If you run the code more than once, you will keep adding to hands since arrays are mutable. Your final result will then be different from the expected solution. Reloading the page will reset the hands array.

Instructions
100 XP

- Add a fiveClubs to the first player's hand in hands.
- Add a queenSpades to the second player's hand in hands.
- Add a kingClubs to the third player's hand in hands.

'''
// Initialize player's hand and print out hands before each player hits
hands(0) = tenClubs + fourDiamonds
hands(1) = nineSpades + nineHearts
hands(2) = twoClubs + threeSpades
hands.foreach(println)

// Add 5♣ to the first player's hand
hands(0) = hands(0) + fiveClubs

// Add Q♠ to the second player's hand
hands(1) = hands(1) + queenSpades

// Add K♣ to the third player's hand
hands(2) = hands(2) + kingClubs

// Print out hands after each player hits
hands.foreach(println)
