'''
Overloading equality


When comparing two objects of a custom class using ==, Python by default compares just the object references, not the data contained in the objects. To override this behavior, the class can implement the special __eq__() method, which accepts two arguments -- the objects to be compared -- and returns True or False. This method will be implicitly called when two objects are compared.

The BankAccount class from the previous chapter is available for you in the script pane. It has one attribute, balance, and a withdraw() method. Two bank accounts with the same balance are not necessarily the same account, but a bank account usually has an account number, and two accounts with the same account number should be considered the same.

Instructions
100 XP

Try selecting the code in lines 1-7 and pressing the "Run code" button. Then try to create a few BankAccount objects in the console and compare them.

- Modify the __init__() method to accept a new parameter - number - and initialize a new number attribute.
- Define an __eq__() method that returns True if the number attribute of two objects is equal.
- Examine the print statements and the output in the console.

'''


class BankAccount:
   # MODIFY to initialize a number attribute
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount

    # Define __eq__ that returns True if the number attributes are equal
    def __eq__(self, other):
        return self.number == other.number


# Create accounts and compare them
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)
