'''
Initialize a list using cons and Nil


You just initialized the prizes list like this:

val prizes = List(10, 15, 20, 25, 30)
That's works great! There's also another commonly used technique that combines the cons (::) operator and Nil, which is the empty list.

In this exercise, you'll initialize the same prizes list from last exercise, just using this fancy, efficient shorthand.

Instructions
100 XP

- Using :: and Nil, initialize a list named prizes with an element each round's prize, where the first through fifth round's prizes are 10, 15, 20, 25, and 30, respectively.

'''
// Initialize a list with an element each round's prize
val prizes = 10: : 15 : : 20 : : 25 : : 30 : : Nil
println(prizes)
