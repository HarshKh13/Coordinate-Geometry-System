import math
class Parabola:
    def __init__(self,a):
        self.a = a
    
    def focus(self):
        focus_x = self.a
        focus_y = 0
        print("Focus is at {},{}".format(focus_x,focus_y))
    
    def latus_rectum(self):
        lr = 4*self.a
        print(lr)

    def length_of_chord(self,line):
        a = self.a
        m = line.slope
        c = line.y - line.slope*line.x
        lc = math.sqrt(a*(1+m**2)*(a-m**c))
        lc = 4*lc/(m**2)
        print(lc)
    
    def tangent(self,x,y):
        slope = y/2
        c = self.a/slope
        print("Equation of Tangent:")
        print("y={}x + {}".format(slope,c))
    
    def normal(self,x,y):
        slope = -y/(2*self.a)
        c = y*(1 + x/(2*self.a))
        print("Equation of Normal:")
        print("y={}x + {}".format(slope,c))
