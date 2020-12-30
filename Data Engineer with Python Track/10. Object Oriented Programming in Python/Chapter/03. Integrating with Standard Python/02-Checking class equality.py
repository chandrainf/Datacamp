'''
Checking class equality

In the previous exercise, you defined a BankAccount class with a number attribute that was used for comparison. But if you were to compare a BankAccount object to an object of another class that also has a number attribute, you could end up with unexpected results.

For example, consider two classes


  class Phone:
    def __init__(self, number):
      self.number = number

    def __eq__(self, other):
      return self.number == \
            other.number

  pn = Phone(873555333)

  class BankAccount:
    def __init__(self, number):
      self.number = number

    def __eq__(self, other):
      return self.number == \
            other.number

  acct = BankAccount(873555333)
  
Running acct == pn will return True, even though we're comparing a phone number with a bank account number.

It is good practice to check the class of objects passed to the __eq__() method to make sure the comparison makes sense.

Instructions
100 XP

Both the Phone and the BankAccount classes have been defined. Try running the code as-is using the "Run code" button and examine the output.

-Modify the definition of BankAccount to only return True if the number attribute is the same and the type() of both objects passed to it is the same.

Run the code and examine the output again

'''


class BankAccount:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance

    def withdraw(self, amount):
        self.balance -= amount

    # MODIFY to add a check for the type()
    def __eq__(self, other):
        return (self.number == other.number) and \
            (type(self) == type(other))


acct = BankAccount(873555333)
pn = Phone(873555333)
print(acct == pn)
