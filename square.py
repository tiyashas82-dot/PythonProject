class square:
    def __init__(self,side):
        self.side=side
        self.area= self.side **2
        self.perimeter= 4*2
    def Sresult(self):
        print('Area:',self.area)
        print('Perimeter:',self.perimeter)