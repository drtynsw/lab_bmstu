import random
from typing import List

def gen_random(num_count: int, min_value: int, max_value: int) -> List[int]:
    """
    Генератор случайных чисел
    
    Args:
        num_count: Количество чисел
        min_value: Минимальное значение
        max_value: Максимальное значение
    
    Returns:
        Список случайных чисел
    """
    return [random.randint(min_value, max_value) for _ in range(num_count)]

# Альтернативная реализация как генератор
def gen_random_generator(num_count: int, min_value: int, max_value: int):
    """
    Генератор случайных чисел (реализация как генератор)
    """
    for _ in range(num_count):
        yield random.randint(min_value, max_value)