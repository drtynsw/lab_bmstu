"""
Основной модуль обработки данных
"""
from math_operations import field, gen_random, filter_data, transform_data, DataProcessor
from print_result import print_result

@print_result
def process_pipeline(data):
    """
    Основной пайплайн обработки данных
    """
    # Шаг 1: Получить уникальные имена
    unique_names = sorted(list(set(field(data, 'name'))), key=lambda x: x.lower())
    
    # Шаг 2: Отфильтровать имена, начинающиеся на 'А'
    filtered_names = filter_data(unique_names, lambda x: x.lower().startswith('а'))
    
    # Шаг 3: Добавить фразу к каждому имени
    transformed_names = transform_data(filtered_names, lambda x: f"{x} смотрит в будущее")
    
    # Шаг 4: Сопоставить имена со случайными зарплатами
    result_dict = dict(zip(transformed_names, gen_random(len(transformed_names), 100000, 200000)))
    
    return result_dict

def main():
    """Основная функция"""
    # Тестовые данные
    test_data = [
        {'name': 'Анна', 'age': 25, 'salary': 50000},
        {'name': 'Алексей', 'age': 30, 'salary': 60000},
        {'name': 'Мария', 'age': 28, 'salary': 55000},
        {'name': 'Андрей', 'age': 35, 'salary': 70000},
        {'name': 'Ольга', 'age': 22, 'salary': 45000}
    ]
    
    # Обработка данных
    result = process_pipeline(test_data)
    return result

if __name__ == "__main__":
    main()