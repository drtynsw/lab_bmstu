from functools import wraps
import inspect

def print_result(func):
    """
    Декоратор для вывода результата функции
    
    Выводит название функции и её результат в отформатированном виде
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\nНазвание функции: {func.__name__}")
        
        # Получаем сигнатуру функции для красивого вывода аргументов
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print("Аргументы:", dict(bound_args.arguments))
        
        result = func(*args, **kwargs)
        
        print("Результат:")
        if isinstance(result, (list, tuple, set)):
            for item in result:
                print(f"  {item}")
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"  {key}: {value}")
        else:
            print(f"  {result}")
        
        return result
    return wrapper