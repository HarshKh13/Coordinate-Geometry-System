import math
from fraction import Fraction
class Circle:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.radius = r
    
    def area(self):
        area = math.pi*self.radius*self.radius
        print(area)
    
    def perimeter(self):
        perimeter = 4*math.pi*self.radius
        print(perimeter)

    def position_of_point(self,x,y):
        distance = (self.x-x)**2 + (self.y-y)**2
        distance = math.sqrt(distance)
        ans = ""
        if(distance<self.radius):
            ans = "Point lies inside the circle"
        elif(distance==self.radius):
            ans = "Point lies on the circle"
        else:
            ans = "Point lies outside the circle"
        print(ans)

    def equation_of_tangent(self,x,y):
        if(self.y-y==0): print("Slope of tangent : infinite")
        else:
            slope_num = self.x-x
            slope_den = y-self.y
            slope = slope_num/slope_den
            print("Slope of tangent : {}".format(slope))


    def equation_of_normal(self,x,y):
        if(self.x-x==0): print("Slope of Normal : infinite")
        else:
            slope_num = self.y-y
            slope_den = x-self.x
            slope = slope_num/slope_den
            print("Slope of tangent : {}".format(slope))
        
    def intersection_with_line(self,line):
        r = self.radius
        m = line.slope
        c = line.y = line.slope*line.x
        b = self.y
        a = self.x
        D = 4*(r*r*(1+m**2) - (c+a*m-b)**2)
        if(D<0):
            print("The line and circle do not intersect")
        elif(D==0):
            x_cor = (a+m*b-m*c)/(1+m**2)
            y_cor = m*x_cor + c
            print("The line touches the circle at {},{}".format(x_cor,y_cor))
        else:
            x_cor1 = (a+m*b-m*c+math.sqrt(D))/(1+m**2)
            x_cor2 = (a+m*b-m*c-math.sqrt(D))/(1+m**2)
            y_cor1 = m*x_cor1 + c
            y_cor2 = m*x_cor2 + c
            print("The points of intersection of line and circle are")
            print("{},{} and {},{}".format(x_cor1,y_cor1,x_cor2,y_cor2))
    




