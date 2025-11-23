"""
Тесты с использованием Mock объектов
"""
import unittest
from unittest.mock import patch, MagicMock
from math_operations import gen_random, DataProcessor

class TestMockOperations(unittest.TestCase):
    """Тесты с Mock объектами"""
    
    @patch('math_operations.random.randint')
    def test_gen_random_with_mock(self, mock_randint):
        """Тест gen_random с mock random.randint"""
        # Arrange
        mock_randint.return_value = 42
        
        # Act
        result = gen_random(5, 1, 100)
        
        # Assert
        self.assertEqual(result, [42, 42, 42, 42, 42])
        self.assertEqual(mock_randint.call_count, 5)
        # Проверяем, что mock вызывался с правильными аргументами
        mock_randint.assert_called_with(1, 100)
    
    def test_data_processor_with_mock_data(self):
        """Тест DataProcessor с mock данными"""
        # Arrange
        mock_data = [
            {'name': 'Test1', 'age': 25, 'salary': 100},
            {'name': 'Test2', 'age': 30, 'salary': 200},
            {'name': 'Test1', 'age': 35, 'salary': 300}  # Дубликат имени
        ]
        processor = DataProcessor(mock_data)
        
        # Act & Assert
        unique_names = processor.get_unique_values('name')
        self.assertEqual(len(unique_names), 2)
        self.assertIn('Test1', unique_names)
        self.assertIn('Test2', unique_names)
        
        filtered = processor.filter_by_condition(lambda x: x['age'] > 25)
        self.assertEqual(len(filtered), 2)
        
        average_salary = processor.calculate_field_average('salary')
        self.assertEqual(average_salary, 200.0)
    
    @patch('math_operations.field')
    def test_calculate_average_with_mock_field(self, mock_field):
        """Тест calculate_field_average с mock field"""
        # Arrange
        mock_field.return_value = [100, 200, 300, 400]  # Mock возвращает значения зарплат
        processor = DataProcessor([{'name': 'Test', 'salary': 100}])  # Любые данные
        
        # Act
        result = processor.calculate_field_average('salary')
        
        # Assert
        self.assertEqual(result, 250.0)  # (100+200+300+400)/4 = 250
        mock_field.assert_called_once_with([{'name': 'Test', 'salary': 100}], 'salary')
    
    @patch('math_operations.gen_random')
    def test_process_pipeline_with_mock_gen_random(self, mock_gen_random):
        """Тест пайплайна обработки с mock gen_random"""
        # Arrange
        mock_gen_random.return_value = [150000, 180000]
        
        # Импортируем здесь, чтобы mock применился
        from process_data import process_pipeline
        
        test_data = [
            {'name': 'Анна', 'salary': 50000},
            {'name': 'Андрей', 'salary': 60000},
            {'name': 'Мария', 'salary': 55000}
        ]
        
        # Act
        result = process_pipeline(test_data)
        
        # Assert
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 2)
        mock_gen_random.assert_called_once_with(2, 100000, 200000)

if __name__ == '__main__':
    unittest.main()