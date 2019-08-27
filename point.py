from math import *

class Point(object):
    
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def __repr__(self):
        return ("Point({},{})".format(self.x, self.y)) 

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Error trying add two points")

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Error trying sub two points")

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        elif isinstance(other, float) or isinstance(other, int):
            return Point(self.x * other, self.y * other)
        else:
            raise TypeError("Error trying mul point")
            
    def __rmul__(self,other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        elif isinstance(other, float) or isinstance(other, int):
            return Point(self.x * other, self.y * other)
        else:
            raise TypeError("Error trying rmul point")

    def __div__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Point(self.x/other,self.y/other)
        else:
            raise TypeError("Error trying div point")
            