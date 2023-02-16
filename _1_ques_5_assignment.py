"""Challenge 1: Square Numbers and Return Their Sum"""

class Point:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def sqSum(self):
        sq_x = self.x**2
        sq_y = self.y**2
        sq_z = self.z**2
        print(f"{sq_x} + {sq_y} + {sq_z}")
        return (sq_x + sq_y + sq_z)

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
print("\nSum of square of given numbers: ")
res_object = Point(x,y,z)
print("Result: ", res_object.sqSum())
