from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth

    def area(self):
        return self.length*self.bredth
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        

    def area(self):
        return 3.14*self.radius*self.radius
    

rect=Rectangle(5,4)
print(f"Area of rectangle: {rect.area()}")
circle=Circle(3)
print(f"Area of circle: {circle.area()}")