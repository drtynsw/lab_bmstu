from typing import List, Any, Callable

def sort(arr: List[Any], key: Callable = None, reverse: bool = False) -> List[Any]:
    """
    Функция сортировки с использованием быстрой сортировки
    
    Args:
        arr: Список для сортировки
        key: Функция ключа для сравнения
        reverse: Обратный порядок сортировки
    
    Returns:
        Отсортированный список
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    
    if key:
        pivot_val = key(pivot)
        left = [x for x in arr if key(x) < pivot_val]
        middle = [x for x in arr if key(x) == pivot_val]
        right = [x for x in arr if key(x) > pivot_val]
    else:
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
    
    result = sort(left, key, reverse) + middle + sort(right, key, reverse)
    
    return result if not reverse else result[::-1]

# Альтернативная реализация как класс
class sort_by:
    def __init__(self, items, **kwargs):
        self.key = kwargs.get('key', None)
        self.reverse = kwargs.get('reverse', False)
        self.sorted_items = self._quicksort(list(items))
        self.index = 0
    
    def _quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        
        if self.key:
            pivot_val = self.key(pivot)
            left = [x for x in arr if self.key(x) < pivot_val]
            middle = [x for x in arr if self.key(x) == pivot_val]
            right = [x for x in arr if self.key(x) > pivot_val]
        else:
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
        
        result = self._quicksort(left) + middle + self._quicksort(right)
        return result if not self.reverse else result[::-1]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.sorted_items):
            result = self.sorted_items[self.index]
            self.index += 1
            return result
        raise StopIteration