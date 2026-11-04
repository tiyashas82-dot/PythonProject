import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * radius * radius
        self.perimeter = 2 * math.pi * radius
    def Cresult(self):
        print("Area:", self.area)
        print("Perimeter:", self.perimeter)

