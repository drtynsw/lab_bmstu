import sys

def is_valid_float(value):
    """Проверяет, можно ли преобразовать значение в действительное число"""
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_coefficient(prompt, param_value=None):
    """
    Получает коэффициент от пользователя.
    Если параметр задан в командной строке и корректен - использует его.
    Иначе запрашивает ввод с клавиатуры.
    """
    if param_value is not None:
        if is_valid_float(param_value):
            coefficient = float(param_value)
            print(f"{prompt} = {coefficient}")
            return coefficient
        else:
            print(f"Некорректное значение параметра '{param_value}'. Требуется ввод с клавиатуры.")
    
    while True:
        try:
            value = input(prompt)
            if is_valid_float(value):
                return float(value)
            else:
                print("Ошибка: введите действительное число!")
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем.")
            sys.exit(0)

def solve_biquadratic():
    """Основная функция решения биквадратного уравнения"""
    print("Решение биквадратного уравнения вида: A*x⁴ + B*x² + C = 0")
    print("=" * 50)
    
    # Получаем коэффициенты из параметров командной строки или с клавиатуры
    a_param = sys.argv[1] if len(sys.argv) > 1 else None
    b_param = sys.argv[2] if len(sys.argv) > 2 else None
    c_param = sys.argv[3] if len(sys.argv) > 3 else None
    
    A = get_coefficient("Введите коэффициент A: ", a_param)
    
    # Проверка, что A ≠ 0 (иначе уравнение не биквадратное)
    while A == 0:
        print("Ошибка: коэффициент A не может быть равен 0 для биквадратного уравнения!")
        A = get_coefficient("Введите коэффициент A: ")
    
    B = get_coefficient("Введите коэффициент B: ", b_param)
    C = get_coefficient("Введите коэффициент C: ", c_param)
    
    print("\n" + "=" * 50)
    print(f"Уравнение: {A}*x⁴ + {B}*x² + {C} = 0")
    
    # Решаем как квадратное уравнение относительно t = x²
    # Уравнение: A*t² + B*t + C = 0
    
    # Вычисляем дискриминант
    D = B**2 - 4*A*C
    print(f"Дискриминант D = {D}")
    
    if D < 0:
        print("Дискриминант отрицательный. Действительных корней нет.")
        return
    
    # Вычисляем корни квадратного уравнения относительно t
    t1 = (-B + D**0.5) / (2*A)
    t2 = (-B - D**0.5) / (2*A)
    
    print(f"Корни относительно t = x²: t1 = {t1}, t2 = {t2}")
    
    real_roots = []
    
    # Находим действительные корни биквадратного уравнения
    if t1 >= 0:
        root1 = t1**0.5
        root2 = -t1**0.5
        real_roots.extend([root1, root2])
        if t1 == 0:  # Если корень нулевой, он будет повторяться
            real_roots = list(set(real_roots))  # Убираем дубликаты
    
    if t2 >= 0 and t2 != t1:  # Проверяем t2, если оно отличается от t1
        root3 = t2**0.5
        root4 = -t2**0.5
        real_roots.extend([root3, root4])
        if t2 == 0:  # Если корень нулевой, он будет повторяться
            real_roots = list(set(real_roots))  # Убираем дубликаты
    
    # Убираем дубликаты и сортируем
    real_roots = sorted(list(set(real_roots)))
    
    if real_roots:
        print(f"Действительные корни уравнения: {real_roots}")
        print(f"Количество действительных корней: {len(real_roots)}")
    else:
        print("Действительных корней нет.")

def main():
    """Главная функция программы"""
    print("Программа для решения биквадратного уравнения")
    print("Биквадратное уравнение: A*x⁴ + B*x² + C = 0")
    
    if len(sys.argv) > 1:
        print("Обнаружены параметры командной строки.")
        if len(sys.argv) > 4:
            print("Предупреждение: задано больше 3 параметров. Будут использованы первые 3.")
    
    try:
        solve_biquadratic()
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()