'''
Create and parameterize an array


The Scala Array is a mutable collection that stores a fixed-size sequential collection of elements of the same type.

In the context of Twenty-One, an array is a good choice to represent something that can change, like the particular players playing (their names specifically). Something else that changes: the specific hands in each round.

In this exercise, you'll create and parameterize an array for the first round of Twenty-One with three players (i.e., each player has one hand in this round). Note: you won't initialize the array with data yet!

Instructions
100 XP

- Create and parameterize an array (named hands) of type Int with a length of 3. Explicitly provide the type parameterization.

'''
// Create and parameterize an array for a round of Twenty-One
val hands: Array[Int] = new Array[Int](3)
