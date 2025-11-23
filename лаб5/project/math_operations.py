"""
Модуль математических операций для тестирования
"""
import random

def field(items, *args):
    """
    Генератор для выборки полей из словарей
    """
    if len(args) == 0:
        return
    
    for item in items:
        if not isinstance(item, dict):
            continue
            
        if len(args) == 1:
            field_name = args[0]
            if field_name in item and item[field_name] is not None:
                yield item[field_name]
        else:
            result = {}
            has_valid_fields = False
            for field_name in args:
                if field_name in item and item[field_name] is not None:
                    result[field_name] = item[field_name]
                    has_valid_fields = True
            if has_valid_fields:
                yield result

def gen_random(num_count, min_value, max_value):
    """
    Генератор случайных чисел
    """
    return [random.randint(min_value, max_value) for _ in range(num_count)]

def filter_data(data, condition_func):
    """
    Фильтрация данных по условию
    """
    return list(filter(condition_func, data))

def transform_data(data, transform_func):
    """
    Преобразование данных с помощью функции
    """
    return list(map(transform_func, data))

def calculate_average(numbers):
    """
    Вычисление среднего значения списка чисел
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

class DataProcessor:
    """Класс для обработки данных"""
    
    def __init__(self, data):
        self.data = data
    
    def get_unique_values(self, field_name):
        """Получить уникальные значения поля"""
        values = list(field(self.data, field_name))
        return list(set(values))
    
    def filter_by_condition(self, condition_func):
        """Отфильтровать данные по условию"""
        return filter_data(self.data, condition_func)
    
    def calculate_field_average(self, field_name):
        """Вычислить среднее значение поля"""
        values = list(field(self.data, field_name))
        # Фильтруем только числовые значения
        numeric_values = [v for v in values if isinstance(v, (int, float))]
        return calculate_average(numeric_values)