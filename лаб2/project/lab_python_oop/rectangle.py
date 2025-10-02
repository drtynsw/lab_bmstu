from .figure import Figure
from .color import FigureColor

class Rectangle(Figure):
    """Класс Прямоугольник"""
    
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color_property = FigureColor()
        self.color_property.color = color
        self._name = "Прямоугольник"
    
    @property
    def name(self):
        return self._name
    
    def area(self):
        """Вычисление площади прямоугольника"""
        return self.width * self.height
    
    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {} площадью {:.2f}".format(
            self.name, 
            self.color_property.color, 
            self.width, 
            self.height, 
            self.area()
        )