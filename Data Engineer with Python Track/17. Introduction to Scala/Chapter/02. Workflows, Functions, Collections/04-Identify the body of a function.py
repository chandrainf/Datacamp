'''
Identify the body of a function


In Twenty-One, it is useful to have a function that determines the maximum of two competing players' hands. For example, imagine a scenario where playerA and playerB have the following hands:

  playerA: queenDiamonds, threeClubs, aceHearts (worth 1), fiveSpades
  playerB: kingHearts, jackHearts

Below is a simple version of that function, called maxHand, that ignores whether or not the hand busts. It also has an if/else expression, which you will learn how to write in an upcoming lesson.

  def maxHand(handA: Int, handB: Int): Int = {
    if (handA > handB) handA
    else handB
  }

In the previous video, the body of the function was emphasized as the only part of a function that you need to know for this course. What is the body of the maxHand function?

Answer the question
50XP

Possible Answers

    - def maxHand(handA: Int, handB: Int)

    - : Int =

    - if (handA > handB) handA

    - else handB

    - Everything within the curly braces.

Answer : Everything within the curly braces.

'''
