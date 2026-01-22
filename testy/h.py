import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.a = Point(ax, ay)
        self.b = Point(bx, by)
        self.c = Point(cx, cy)
        self.d = Point(dx, dy)

    def area(self):
        obsah = (self.c.x - self.a.x) * (self.c.y - self.b.y)
        return obsah
    
    def move(self, dx, dy):
        self.a.x += dx
        self.a.y += dy

        self.b.x += dx
        self.b.y += dy

        self.c.x += dx
        self.c.y += dy

        self.d.x += dx
        self.d.y += dy

    def scale(self, factor):
        ab = self.b.x - self.a.x
        cd = self.b.y - self.c.y
        
        self.b.x = factor * ab + self.a.x
        self.d.x = factor * cd + self.c.x
        

    

    

    
    

    

        







