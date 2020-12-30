'''
Understanding scope


What four values does this script print?

  x = 50

  def one():
    x = 10

  def two():
    global x
    x = 30

  def three():
    x = 100
    print(x)

  for func in [one, two, three]:
    func()
    print(x)

Answer the question
50XP

Possible Answers

    - 50, 30, 100, 50

    - 10, 30, 30, 30

    - 50, 30, 100, 30

    - 10, 30, 100, 50

    - 50, 50, 50, 50

Answer : 50, 30, 100, 30

'''
