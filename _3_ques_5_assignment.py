"""Challenge 3: Implement the Complete Student Class"""

class Student:
   
    def setName(self, name):
        self.__name = name
    def getName(self):
        print("Student Name: ", self.__name)
    
    def setRollNumber(self, roll_number):
        self.__roll_number = roll_number
    def getRollNumber(self):
        print("Roll number: ", self.__roll_number)

name = input("Enter name: ")
roll_number = int(input("Enter Roll number: "))
print("=============================")
stu = Student()
stu.setName(name)
stu.getName()

stu.setRollNumber(roll_number)
stu.getRollNumber()