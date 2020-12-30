'''
Handling exception hierarchies


Previously, you defined an Employee class with a method get_bonus() that raises a BonusError and a SalaryError depending on parameters. But the BonusError exception was inherited from the SalaryError exception. How does exception inheritance affect exception handling?

The Employee class has been defined for you. It has a minimal salary of 30000 and a maximal bonus amount of 5000.

Instructions 1/2
50 XP

Question :

Experiment with the following code

  emp = Employee("Katze Rik", salary=50000)
  try:
    emp.give_bonus(7000)
  except SalaryError:
    print("SalaryError caught!")

  try:
    emp.give_bonus(7000)
  except BonusError:
    print("BonusError caught!")

  try:
    emp.give_bonus(-100000)
  except SalaryError:
    print("SalaryError caught again!")

  try:
    emp.give_bonus(-100000)
  except BonusError:
    print("BonusError caught again!")

and select the statement which is TRUE about handling parent/child exception classes:

Possible Answers

    - except block for a parent exception will catch child exceptions

    - except block for a parent exception will not catch child exceptions

Answer : except block for a parent exception will catch child exceptions

'''


'''
Instructions 2/2
50 XP

Question :
Experiment with two pieces of code:


  emp = Employee("Katze Rik",\
                      50000)
  try:
    emp.give_bonus(7000)
  except SalaryError:
    print("SalaryError caught")
  except BonusError:
    print("BonusError caught")
      

  emp = Employee("Katze Rik",\
                      50000)
  try:
    emp.give_bonus(7000)
  except BonusError:
    print("BonusError caught")
  except SalaryError:
    print("SalaryError caught")
      
(one catches BonusError before SalaryError, and the other -SalaryError before BonusError)

Select the statement which is TRUE about the order of except blocks:

Possible Answers : 

    - The order of except blocks doesn't matter: the result is the same.

    - It's better to include an except block for a parent exception before the block for a child exception to ensure that the most general exception is handled first.

    - It's better to include an except block for a child exception before the block for a parent exception, otherwise the child exceptions will be always be caught in the parent block, and the except block for the child will never be executed.

Answer : It's better to include an except block for a child exception before the block for a parent exception, otherwise the child exceptions will be always be caught in the parent block, and the except block for the child will never be executed.

'''
