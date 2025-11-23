"""
Декоратор для вывода результатов
"""
from functools import wraps

def print_result(func):
    """
    Декоратор для вывода результата функции
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        print(f"\nРезультат функции {func.__name__}:")
        if isinstance(result, dict):
            for key, value in result.items():
                print(f"  {key}: {value}")
        elif isinstance(result, list):
            for item in result:
                print(f"  {item}")
        else:
            print(f"  {result}")
        
        return result
    return wrapper