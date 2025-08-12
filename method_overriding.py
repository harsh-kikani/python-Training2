class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)
        
    def area(self):
        return 3.14 * self.radius * self.radius
rec = shape(5, 10)
print(rec.area())  
    
c = circle(7)
print(c.area()) 