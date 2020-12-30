'''
Polymorphic methods
To design classes effectively, you need to understand how inheritance and polymorphism work together.

In this exercise, you have three classes - one parent and two children - each of which has a talk() method. Analyze the following code:

    class Parent:
        def talk(self):
            print("Parent talking!")     

    class Child(Parent):
        def talk(self):
            print("Child talking!")          

    class TalkativeChild(Parent):
        def talk(self):
            print("TalkativeChild talking!")
            Parent.talk(self)


    p, c, tc = Parent(), Child(), TalkativeChild()

    for obj in (p, c, tc):
        obj.talk()

What is the output of the code above?

1.
    Parent talking!
    Parent talking!
    Parent talking!      

      
2.
    Parent talking!
    Child talking!
    Talkative Child talking!     
      
      
3.
    Parent talking!
    Child talking!
    Parent talking! 
    Talkative Child talking!
    Parent talking!      

      
4.
    Parent talking!
    Child talking!
    Talkative Child talking!
    Parent talking!      

      
You should be able to complete the exercise just by reading the code, without running it in the console!

Answer the question
50XP

Possible Answers :

    - 1

    - 2

    - 3

    - 4

    - Code causes an error

Answer : 4

'''
