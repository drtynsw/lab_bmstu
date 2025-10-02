class FigureColor:
    """Класс Цвет фигуры"""
    
    def __init__(self):
        self._color = None
    
    @property
    def color(self):
        """Getter для цвета"""
        return self._color
    
    @color.setter
    def color(self, value):
        """Setter для цвета"""
        self._color = value