class circle(object):
    def __init__(self,radius,color):
        self.radius = radius                 # self es como la variable propia de la clase y se puede invokar en toda la clase.
        self.color = color
        
    def add_radius(self,r):
        print(f'El Radio es de Color = {self.color}')        
        self.radius = self.radius + r
        return (self.radius)
    
redCircle = circle(10,'red')    
print(f'Ka SUma al Radio es = {redCircle.add_radius(5)}')
