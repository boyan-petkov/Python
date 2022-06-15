# Create a class Circle. In the __init__ method, the circle should only receive one parameter - its diameter. 
# Create a class attribute called __pi that is equal to 3.14. The class should also have the following methods:
# •	calculate_circumference() - returns the circumference of the circle
# •	calculate_area() - returns the area of the circle
# •	calculate_area_of_sector(angle) - gives the central angle in degrees, returns the area that fills the sector
# Notes: Search the formulas on the internet. Name your methods and variables exactly as in the description! Submit only the class.
#   Test your class before submitting it!

class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circumference = self.diameter * self.__pi
        return circumference

    def calculate_area(self):
        r = self.diameter / 2
        area = self.__pi * (r ** 2)
        return area

    def calculate_area_of_sector(self, angle):
        r = self.diameter / 2
        sector_area = (angle / 360) * self.__pi * (r ** 2)
        return sector_area


