from typing import List, Dict, Any, Union

def field(items: List[Dict], *args: str) -> Union[List, List[Dict]]:
    """
    Генератор для выборки полей из словарей
    
    Args:
        items: Список словарей
        *args: Названия полей для выборки
    
    Yields:
        Если передан один аргумент - значения поля
        Если несколько аргументов - словари с выбранными полями
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