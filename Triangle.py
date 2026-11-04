class triangle:
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.area=self.side1*self.side2*(1/2)
        self.perimeter=self.side1+self.side2+self.side3
    def Tresult(self):
        print(self.area)
        print(self.perimeter)