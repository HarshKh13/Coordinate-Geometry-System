import math
class Ellipse:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def eccentricity(self):
        e = math.sqrt(1 - (self.b/self.a)**2)
        print(e)

    def minor_axis(self):
        length = 2*self.b
        print(length)

    def major_axis(self):
        length = 2*self.a
        print(length)
    
    def latus_rectum(self):
        length = 2*self.b*self.b/self.a
    
    def area(self):
        area = math.pi*self.a*self.b
        print(area)
    
    def circumference(self):
        circum = math.sqrt(2*(self.a**2 + self.b**2))
        circum = math.pi*circum
        print(circum)

    def position_of_point(self,x,y):
        value = ((x**2/self.a**2) + (y**2/self.b**2)-1)
        if(value<0):
            print("Point lies inside the ellipse")
        elif(value==0):
            print("Point lies on the ellipse")
        else:
            print("Point lies outside the ellipse")
    
    def tangent(self,x,y):
        slope = -((x*self.b**2)/(y*self.a**2))
        c = y + ((x*x*self.b*self.b)/(y*self.a*self.a))
        print("Equation of Tangent:")
        print("y={}x + {}".format(slope,c))

    

