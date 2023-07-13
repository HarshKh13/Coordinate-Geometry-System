import math
from fraction import Fraction
class Line:
    def __init__(self,x,y,slope):
        self.x = x
        self.y = y
        self.slope = slope
    
    def distance_from_point(self,x,y):
        temp_num = abs((y-self.y) + self.slope*(self.x-x))
        temp_den = math.sqrt(1+self.slope*self.slope)
        distance = temp_num/temp_den
        print("Distance of line from point is : {}".format(distance))
    
        
    
