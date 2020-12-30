'''
You can change me


Let's test out a prototype one-player version of Twenty-One. Your friend Alex is playerA. They are dealt two cards: the jack of clubs (J♣) and the ace of diamonds (A♦). They know the default implementation of the game has aces worth 1 point but they want it to be worth 11 so they can add their two cards together to get 21.

In this exercise, you'll code up this scenario. jackClubs (a val with a point value of 10) and aceDiamonds (a var with a point value of 1) are already defined.

Instructions
100 XP

- Create a var named playerA and with the name Alex as a string literal as its value.
- Change the point value of the ace of diamonds so it is worth 11 points, instead of the original value of 1 point it was assigned.
- Add jackClubs and aceDiamonds to calculate the value of Alex's hand and print the result.

'''
// Create a mutable variable for Alex as player A
var playerA = "Alex"

// Change the point value of A♦ from 1 to 11
aceDiamonds = 11

// Calculate hand value for J♣ and A♦
println(aceDiamonds + jackClubs)
