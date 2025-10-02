from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

# Импорт внешнего пакета (colorama для цветного вывода)
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)  # Инициализация colorama
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    print("Colorama не установлен. Установите: pip install colorama")

def main():
    """Основная функция тестирования"""
    
    # Номер варианта (замените N на ваш номер)
    N = 4  # вариант 4
    
    print("Демонстрация работы с геометрическими фигурами")
    print("=" * 50)
    
    # Создание объектов
    rectangle = Rectangle(width=N, height=N, color="синего")
    circle = Circle(radius=N, color="зеленого")
    square = Square(side=N, color="красного")
    
    # Вывод информации о фигурах
    if COLORAMA_AVAILABLE:
        print(Fore.BLUE + str(rectangle))
        print(Fore.GREEN + str(circle))
        print(Fore.RED + str(square))
        
        # Демонстрация работы внешнего пакета
        print("\n" + "=" * 50)
        print(Fore.YELLOW + Back.BLACK + "Демонстрация внешнего пакета colorama:")
        print(Fore.CYAN + "Этот текст выведен с использованием colorama!")
        print(Fore.MAGENTA + Style.BRIGHT + "Яркий цветной текст")
        print(Style.RESET_ALL + "Текст сброшен к стандартному формату")
    else:
        # Вывод без цветов, если colorama не установлен
        print(rectangle)
        print(circle)
        print(square)
        print("\n" + "=" * 50)
        print("Colorama не установлен. Для цветного вывода установите: pip install colorama")
    
    # Дополнительная информация о фигурах
    print("\n" + "=" * 50)
    print("Дополнительная информация:")
    print(f"Площадь {rectangle.name}: {rectangle.area():.2f}")
    print(f"Площадь {circle.name}: {circle.area():.2f}")
    print(f"Площадь {square.name}: {square.area():.2f}")

if __name__ == "__main__":
    main()