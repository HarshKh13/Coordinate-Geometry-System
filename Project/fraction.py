import math
class Fraction:
    def __init__(self,num,den):
        self.num = num
        self.den = den

    def gcd(self,temp_num,temp_den):
        gcd = math.gcd(temp_num,temp_den)
        temp_num = temp_num/gcd
        temp_den = temp_den/gcd
        return temp_num,temp_den
    
    def __add__(self,other):
        temp_num = self.num*other.den + self.den*other.num
        temp_den = self.den*other.den
        num,den = self.gcd(temp_num,temp_den)
        return "{}/{}".format(num,den)

    def __sub__(self,other):
        temp_num = self.num*other.den - self.den*other.num
        temp_den = self.den*other.den
        num,den = self.gcd(temp_num,temp_den)
        return "{}/{}".format(num,den)
    
    def __mul__(self,other):
        temp_num = self.num*other.num
        temp_den = self.den*other.den
        num,den = self.gcd(temp_num,temp_den)
        return "{}/{}".format(num,den)
    
    def __truediv__(self,other):
        temp_num = self.num*other.den
        temp_den = self.den*other.num
        num,den = self.gcd(temp_num,temp_den)
        return "{}/{}".format(num,den)
    


