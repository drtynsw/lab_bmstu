from .rectangle import Rectangle

class Square(Rectangle):
    """Класс Квадрат (наследуется от Прямоугольника)"""
    
    def __init__(self, side, color):
        # Вызываем конструктор родительского класса
        super().__init__(side, side, color)
        self._name = "Квадрат"
    
    @property
    def name(self):
        return self._name
    
    def __repr__(self):
        return "{} {} цвета со стороной {} площадью {:.2f}".format(
            self.name, 
            self.color_property.color, 
            self.width,  # или self.height, они равны
            self.area()
        )