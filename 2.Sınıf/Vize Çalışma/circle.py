#Circle 

class circle():
    def __init__(self,radius):
        self.radius=radius
        self.pi=3.14
    def hesap(self):
        print( self.radius * self.radius * self.pi )
    # def setradius(self,radius):
    #     self.radius=radius
    # def getradius(self):
    #     return self.radius

c1=circle(5)
c1.hesap()