from print_result import print_result
from field import field
from gen_random import gen_random
from cm_timer import cm_timer_1
import json
import sys

# Пример данных по умолчанию
DEFAULT_DATA = [
    {'name': 'Ksenia', 'age': 25, 'city': 'Moscow', 'salary': 50000},
    {'name': 'Ivan', 'age': 30, 'city': 'St Petersburg', 'salary': 60000},
    {'name': 'Maria', 'age': 28, 'city': 'Moscow', 'salary': 55000},
    {'name': 'Alexey', 'age': 35, 'city': 'Kazan', 'salary': 70000},
    {'name': 'Olga', 'age': 22, 'city': 'Moscow', 'salary': 45000},
    {'name': 'Anna', 'age': 29, 'city': 'Moscow', 'salary': 48000},
    {'name': 'Andrey', 'age': 32, 'city': 'St Petersburg', 'salary': 65000}
]

@print_result
def f1(arg):
    """Получить уникальные имена, отсортированные по алфавиту"""
    return sorted(list(set(field(arg, 'name'))), key=lambda x: x.lower())

@print_result
def f2(arg):
    """Отфильтровать имена, начинающиеся на 'А' или 'A'"""
    return list(filter(lambda x: x.lower().startswith('а'), arg))

@print_result
def f3(arg):
    """Добавить фразу к каждому имени"""
    return list(map(lambda x: x + " смотрит в будущее", arg))

@print_result
def f4(arg):
    """Сопоставить имена со случайными зарплатами"""
    return dict(zip(arg, gen_random(len(arg), 100000, 200000)))

def main():
    # Инициализация данных
    data = DEFAULT_DATA
    
    # Чтение данных из файла, если он указан
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"Данные загружены из файла: {sys.argv[1]}")
        except FileNotFoundError:
            print(f"Файл {sys.argv[1]} не найден. Используются данные по умолчанию.")
        except json.JSONDecodeError:
            print(f"Ошибка чтения JSON из файла {sys.argv[1]}. Используются данные по умолчанию.")
        except Exception as e:
            print(f"Ошибка при загрузке файла: {e}. Используются данные по умолчанию.")
    else:
        print("Используются данные по умолчанию.")
    
    print(f"Всего записей: {len(data)}")
    
    # Выполнение пайплайна с замером времени
    with cm_timer_1():
        result = f4(f3(f2(f1(data))))
    
    return result

if __name__ == "__main__":
    main()