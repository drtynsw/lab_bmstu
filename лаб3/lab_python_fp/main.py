from process_data import f1, f2, f3, f4, main as process_main
from unique import Unique, unique
from sort import sort, sort_by
from field import field
from gen_random import gen_random
from cm_timer import cm_timer_1, cm_timer_2
from print_result import print_result

def test_unique():
    print("=== Тестирование unique ===")
    
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print("Исходные данные:", data)
    print("Уникальные:", list(Unique(data)))
    
    data_str = ['a', 'A', 'b', 'B', 'a', 'A', 'c']
    print("Исходные строки:", data_str)
    print("Уникальные (без ignore_case):", list(Unique(data_str)))
    print("Уникальные (с ignore_case):", list(Unique(data_str, ignore_case=True)))
    
    # Тестирование класса unique
    print("Класс unique:", list(unique(data_str, ignore_case=True)))

def test_sort():
    print("\n=== Тестирование sort ===")
    
    data = [5, 2, 8, 1, 9]
    print("Исходные данные:", data)
    print("Отсортированные:", sort(data))
    print("Обратная сортировка:", sort(data, reverse=True))
    
    data_str = ['banana', 'apple', 'cherry']
    print("Исходные строки:", data_str)
    print("Отсортированные:", sort(data_str))
    print("По длине:", sort(data_str, key=len))
    
    # Тестирование класса sort_by
    print("Класс sort_by:", list(sort_by(data_str, key=len)))

def test_field():
    print("\n=== Тестирование field ===")
    
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': None, 'price': 1500, 'color': 'blue'},
        {'title': 'Стул', 'color': 'white'}
    ]
    
    print("Только названия:", list(field(goods, 'title')))
    print("Названия и цены:", list(field(goods, 'title', 'price')))
    print("Все поля:", list(field(goods, 'title', 'price', 'color')))

def test_gen_random():
    print("\n=== Тестирование gen_random ===")
    
    print("5 случайных чисел от 1 до 10:", gen_random(5, 1, 10))
    print("3 случайных числа от 100 до 200:", gen_random(3, 100, 200))

def test_cm_timer():
    print("\n=== Тестирование cm_timer ===")
    
    with cm_timer_1():
        time.sleep(0.5)
    
    with cm_timer_2():
        time.sleep(0.3)

def test_print_result():
    print("\n=== Тестирование print_result ===")
    
    @print_result
    def test_function(x, y=10):
        return [x * i for i in range(1, y+1)]
    
    result = test_function(2, y=5)

def main():
    """Основная функция тестирования всех компонентов"""
    print("Лабораторная работа: Функциональное программирование в Python")
    print("=" * 60)
    
    test_unique()
    test_sort()
    test_field()
    test_gen_random()
    test_print_result()
    test_cm_timer()
    
    print("\n" + "=" * 60)
    print("Тестирование основного пайплайна:")
    print("=" * 60)
    
    # Запуск основного пайплайна из process_data
    process_main()

if __name__ == "__main__":
    import time
    main()