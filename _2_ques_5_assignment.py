"""Challenge 2: Implement a Calculator Class"""

class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1/self.num2

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

cal = Calculator(num1, num2)

choice = 1
while choice != 0:
    print("\nSelect any one option, you want to perform: ")
    print("0. Exit")
    print("1. Addition")
    print("2. Subtraction")    
    print("3. Multiplication")
    print("4. Division")   
    
    choice = int(input("\nEnter your choice: "))
 

    if choice == 1:
        print("Add: ",cal.add())
    elif choice == 2:
        print("Subtract: ",cal.subtract())
    elif choice == 3:
        print("Multiply: ",cal.multiply())
    elif choice == 4:
        print("Division: ",cal.divide())
    elif choice == 0:
        print("Exit")
    else:
        print("Invalid choice")
        