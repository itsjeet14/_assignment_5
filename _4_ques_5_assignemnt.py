"""Challenge 4: Implement a Banking Account"""

class Account:

    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance       

class SavingsAccount(Account):

    def __init__(self, title, balance, interestRate):
        self.interestRate = interestRate
        super().__init__(title, balance)
    
    def display(self):
        print("Customer Name: ",self.title)
        print("Account Balance: Rs",self.balance)
        print("Interest Rate: ", self.interestRate, "%")

name = input("Enter name of candidate: ")
balance = float(input("Enter Balance Amount: Rs "))
interest = float(input("Enter Interest Rate: "))
print("====================================")
acc = SavingsAccount(name,balance,interest)
acc. display()

