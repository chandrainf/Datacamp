'''
Initialize an array


Once parameterized, initializing the array is done by passing in the desired data inside parentheses ((___)). This contrasts with square brackets ([___]), like in programming languages like Java and Python. Arrays in Scala are zero-indexed.

In this exercise, you'll initialize the hands array you created and parameterized in the previous exercise with the starting hand (i.e., first two cards) for each player. The card variables you need are already defined (they are all of type Int).

Instructions
100 XP

- nitialize the first player's hand in the hands array.
- Initialize the second player's hand in the hands array.
- Initialize the third player's hand in the hands array.

'''
// Create and parameterize an array for a round of Twenty-One
val hands: Array[Int] = new Array[Int](3)

// Initialize the first player's hand in the array
hands(0) = tenClubs + fourDiamonds

// Initialize the second player's hand in the array
hands(1) = nineSpades + nineHearts

// Initialize the third player's hand in the array
hands(2) = twoClubs + threeSpades
