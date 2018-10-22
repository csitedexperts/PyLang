# https://www.w3schools.com/python/python_classes.asp

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self, radius):
        area = 3.14 * radius * radius
        print("Area of a circle with radius : ", self.radius , " is: ", area)
    
c1 = Circle(10)

print(c1.radius)
c1.area(10)
