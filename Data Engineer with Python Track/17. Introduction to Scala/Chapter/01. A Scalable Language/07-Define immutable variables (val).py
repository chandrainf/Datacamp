'''
Define immutable variables (val)


Scala has two kinds of variables: val and var. val are immutable, which means once initialized, they can't be reassigned.

In Twenty-One, a val is like any non-ace card. That is, 2 through 10 (worth 2 through 10 points) and all face cards (jack, queen, and king are worth 10 points) all have the same point value throughout the game.

In this exercise, you will define variables for some non-ace cards, each as a val of type Int (one of the four most common value types for data-related tasks). In the next lesson, you'll learn why immutable variables are preferred in Scala.

Instructions
100 XP

- Define variables for cards 2, 3, and 4 for the suit clubs (♣). Explicitly specify their type as Int.

'''
// Define immutable variables for clubs 2♣ through 4♣
val twoClubs: Int = 2
val threeClubs: Int = 3
val fourClubs: Int = 4
