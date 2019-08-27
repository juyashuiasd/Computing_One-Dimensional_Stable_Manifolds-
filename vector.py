from math import *
from point import *

class Vector(object):
    def __init__(self, *args):
        if len(args) == 2:
            if isinstance(args[0], Point) and isinstance(args[1], Point):
                self.x = args[1].x - args[0].x
                self.y = args[1].y - args[0].y
            elif((isinstance(args[0], int) 
                or isinstance(args[0], float))
                and (isinstance(args[1], int) 
                or isinstance(args[1], float))):
                self.x = float(args[0])
                self.y = float(args[1])
        elif len(args) == 1:
            if isinstance(args[0], Vector):
                self.x = args[0].x
                self.y = args[0].y
        
    def __repr__(self):
        return ("Vector({},{})".format(self.x, self.y))
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
        elif isinstance(other, float) or isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("Error trying mul vector")
            
    def __rmul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
        elif isinstance(other, float) or isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("Error trying rmul vector")
            
    def __div__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.x/other,self.y/other)
        else:
            raise TypeError("Error trying div vector")
        
    def module(self):
        return sqrt(self.x**2 + self.y**2)
    
    def dotProduct(self, v):
        return self.x * v.x + self.y * v.y
    
    def normalize(self):
        return Vector(self.x / self.module(), self.y / self.module())
    
    def signs(self):
        return (self.x/abs(self.x),self.y/abs(self.y))
