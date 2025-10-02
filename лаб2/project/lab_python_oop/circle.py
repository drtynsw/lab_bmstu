import math
from .figure import Figure
from .color import FigureColor

class Circle(Figure):
    """Класс Круг"""
    
    def __init__(self, radius, color):
        self.radius = radius
        self.color_property = FigureColor()
        self.color_property.color = color
        self._name = "Круг"
    
    @property
    def name(self):
        return self._name
    
    def area(self):
        """Вычисление площади круга"""
        return math.pi * self.radius ** 2
    
    def __repr__(self):
        return "{} {} цвета радиусом {} площадью {:.2f}".format(
            self.name, 
            self.color_property.color, 
            self.radius, 
            self.area()
        )