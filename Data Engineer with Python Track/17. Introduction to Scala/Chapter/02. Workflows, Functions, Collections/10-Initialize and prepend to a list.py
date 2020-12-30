'''
Initialize and prepend to a list


The List in Scala is like the Array in that they are a sequence of objects that share the same type. The List collection, however, is immutable. When performing operations on lists, the result will be a new list with a new value. The cons operator (::) prepends an element to a list.

Imagine you wanted to raise the stakes a little when playing Twenty-One by adding a monetary prize for each round. The winner of round one gets $10, the winner of round two gets $15, etc.

In this exercise, you'll create a list to store these prize values for five rounds, then prepend to it to accommodate another round.

Instructions
100 XP

- Initialize a list named prizes with an element for each round's prize, where the first through fifth round's prizes are 10, 15, 20, 25, and 30, respectively.
-Prepend to prizes using the cons (::) operator so a new first round is added, worth $5. Name the new list newPrizes

'''
// Initialize a list with an element for each round's prize
val prizes = List(10, 15, 20, 25, 30)
println(prizes)

// Prepend to prizes to add another round and prize
val newPrizes = 5: : prizes
println(newPrizes)
