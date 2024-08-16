#define a circle class to create a circle with radius r usinng the constructor
#define an area method of the class which calculates the area of the circle
#define a perimeter method of the class which allows you to calculate the perimeter of the circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14159 * (self.radius ** 2)
    
    def get_perimeter(self):
        return 2 * 3.14159 * self.radius
    
circle1=Circle(5)

print("Area of circle with radius 5 is: ", circle1.get_area())

print("Perimeter of circle with radius 5 is: ", circle1.get_perimeter())