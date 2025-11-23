"""
Модульные тесты с использованием TDD подхода (unittest)
"""
import unittest
from math_operations import field, gen_random, filter_data, transform_data, calculate_average, DataProcessor

class TestMathOperationsTDD(unittest.TestCase):
    """TDD тесты для математических операций"""
    
    def setUp(self):
        """Настройка тестовых данных"""
        self.test_data = [
            {'name': 'Анна', 'age': 25, 'salary': 50000},
            {'name': 'Алексей', 'age': 30, 'salary': 60000},
            {'name': 'Мария', 'age': 28, 'salary': 55000},
            {'name': None, 'age': 35, 'salary': 70000},  # name = None
            {'name': 'Ольга', 'salary': 45000}  # отсутствует age
        ]
    
    def test_field_single_field(self):
        """Тест выборки одного поля"""
        # Act
        result = list(field(self.test_data, 'name'))
        
        # Assert - должны получить все не-None значения, включая Ольгу
        expected_names = ['Анна', 'Алексей', 'Мария', 'Ольга']
        self.assertEqual(result, expected_names)
    
    def test_field_multiple_fields(self):
        """Тест выборки нескольких полей"""
        # Act
        result = list(field(self.test_data, 'name', 'age'))
        
        # Assert - должны получить словари для всех элементов, где есть хотя бы одно поле
        self.assertEqual(len(result), 5)  # Все 5 элементов, но с разными наборами полей
        
        # Проверяем конкретные случаи
        for item in result:
            self.assertIsInstance(item, dict)
    
    def test_field_multiple_fields_specific(self):
        """Тест выборки нескольких полей с проверкой конкретных значений"""
        # Arrange
        data = [
            {'name': 'Анна', 'age': 25},
            {'name': 'Борис'},  # нет age
            {'age': 30},  # нет name
            {'name': None, 'age': 35}  # name = None
        ]
        
        # Act
        result = list(field(data, 'name', 'age'))
        
        # Assert
        self.assertEqual(len(result), 4)
        
        # Проверяем содержимое
        expected_results = [
            {'name': 'Анна', 'age': 25},
            {'name': 'Борис'},
            {'age': 30},
            {'age': 35}  # name = None не включается в результат для множественных полей
        ]
        
        for i, expected in enumerate(expected_results):
            self.assertEqual(result[i], expected)
    
    def test_filter_data(self):
        """Тест фильтрации данных"""
        # Arrange
        data = [1, 2, 3, 4, 5, 6]
        
        # Act
        result = filter_data(data, lambda x: x % 2 == 0)
        
        # Assert
        self.assertEqual(result, [2, 4, 6])
    
    def test_transform_data(self):
        """Тест преобразования данных"""
        # Arrange
        data = [1, 2, 3]
        
        # Act
        result = transform_data(data, lambda x: x * 2)
        
        # Assert
        self.assertEqual(result, [2, 4, 6])
    
    def test_calculate_average(self):
        """Тест вычисления среднего значения"""
        # Arrange
        numbers = [10, 20, 30, 40]
        
        # Act
        result = calculate_average(numbers)
        
        # Assert
        self.assertEqual(result, 25.0)
    
    def test_calculate_average_empty_list(self):
        """Тест вычисления среднего для пустого списка"""
        # Act
        result = calculate_average([])
        
        # Assert
        self.assertEqual(result, 0)

class TestDataProcessorTDD(unittest.TestCase):
    """TDD тесты для DataProcessor"""
    
    def setUp(self):
        """Настройка тестовых данных"""
        self.test_data = [
            {'name': 'Анна', 'age': 25, 'salary': 50000},
            {'name': 'Алексей', 'age': 30, 'salary': 60000},
            {'name': 'Анна', 'age': 28, 'salary': 55000},  # Дубликат имени
            {'name': 'Мария', 'age': 35, 'salary': 70000},
            {'name': 'Ольга', 'age': 22},  # Нет salary
            {'name': None, 'age': 40, 'salary': 80000},  # name = None
            {'age': 45, 'salary': 90000}  # Нет name
        ]
        self.processor = DataProcessor(self.test_data)
    
    def test_get_unique_values(self):
        """Тест получения уникальных значений"""
        # Act
        result = self.processor.get_unique_values('name')
        
        # Assert - должны получить 4 уникальных имени: Анна, Алексей, Мария, Ольга
        # None и отсутствующее имя не включаются
        self.assertEqual(len(result), 4)
        self.assertIn('Анна', result)
        self.assertIn('Алексей', result)
        self.assertIn('Мария', result)
        self.assertIn('Ольга', result)
    
    def test_get_unique_values_age(self):
        """Тест получения уникальных значений для поля age"""
        # Act
        result = self.processor.get_unique_values('age')
        
        # Assert - все 7 элементов имеют age
        self.assertEqual(len(result), 7)
    
    def test_filter_by_condition(self):
        """Тест фильтрации по условию"""
        # Act
        result = self.processor.filter_by_condition(lambda x: x.get('age', 0) > 28)
        
        # Assert - 4 элемента с age > 28
        self.assertEqual(len(result), 4)
    
    def test_calculate_field_average(self):
        """Тест вычисления среднего значения поля"""
        # Act
        result = self.processor.calculate_field_average('salary')
        
        # Assert - считаем среднее только для числовых значений salary
        # Элементы с salary: 50000, 60000, 55000, 70000, 80000, 90000
        salaries = [50000, 60000, 55000, 70000, 80000, 90000]
        expected_avg = sum(salaries) / len(salaries)
        self.assertAlmostEqual(result, expected_avg)
    
    def test_calculate_field_average_mixed_data(self):
        """Тест вычисления среднего для поля со смешанными типами"""
        # Arrange
        mixed_data = [
            {'value': 10},
            {'value': 'string'},  # Не число - игнорируется
            {'value': 20},
            {'value': None},  # None - игнорируется
            {'value': 30}
        ]
        processor = DataProcessor(mixed_data)
        
        # Act
        result = processor.calculate_field_average('value')
        
        # Assert - только числовые значения: 10, 20, 30
        expected_avg = (10 + 20 + 30) / 3
        self.assertAlmostEqual(result, expected_avg)

if __name__ == '__main__':
    unittest.main()