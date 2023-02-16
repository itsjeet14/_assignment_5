"""Challenge 5: Handling a Bank Account"""

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
        print("Customer Name: ", self.title)
        print("Balance Amount: Rs", self.balance)
    
    def withdrawal(self):
        amount = float(input("\nEnter amount to withdraw: "))
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("The withdraw is successful and the balance is Rs %f"%self.balance)
        else:
            print("Insuficient Balance")

    def deposit(self):
        amount = float(input("\nEnter the amount to be deposit: "))
        self.balance = self.balance + amount
        print("The deposit is successful and the balance is Rs %f" %self.balance)
       
    def getBalance(self):
        print("\nBalance in the account is Rs %f "%self.balance)
       

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        print("Interest amount: Rs", (self.balance*self.interestRate)*(1/100))


acc = SavingsAccount("Ashish", 2000, 5)   # initializing a SavingsAccount object
acc.withdrawal()
acc.deposit()
acc.getBalance()
acc.interestAmount()