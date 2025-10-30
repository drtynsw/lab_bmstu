from typing import List, Any, Callable

def Unique(arr: List[Any], ignore_case: bool = False) -> List[Any]:
    """
    Генератор для получения уникальных элементов из списка
    
    Args:
        arr: Входной список
        ignore_case: Игнорировать регистр для строк
    
    Yields:
        Уникальные элементы в порядке первого появления
    """
    seen = set()
    
    for item in arr:
        if ignore_case and isinstance(item, str):
            key = item.lower()
        else:
            key = item
        
        if key not in seen:
            seen.add(key)
            yield item

# Альтернативная реализация как класс
class unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            item = next(self.items)
            key = item.lower() if self.ignore_case and isinstance(item, str) else item
            
            if key not in self.seen:
                self.seen.add(key)
                return item