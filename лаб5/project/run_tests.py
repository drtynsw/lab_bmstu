"""
Запуск всех тестов
"""
import unittest
import subprocess
import sys

def run_tdd_tests():
    """Запуск TDD тестов"""
    print("Запуск TDD тестов...")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName('test_math_operations_tdd')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()

def run_bdd_tests():
    """Запуск BDD тестов"""
    print("\nЗапуск BDD тестов...")
    try:
        result = subprocess.run([sys.executable, '-m', 'behave', 'features/math_operations.feature'], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Ошибки:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Ошибка запуска BDD тестов: {e}")
        return False

def run_mock_tests():
    """Запуск Mock тестов"""
    print("\nЗапуск Mock тестов...")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName('test_mock_operations')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()

if __name__ == '__main__':
    print("=== ЗАПУСК ВСЕХ ТЕСТОВ ===")
    
    tdd_success = run_tdd_tests()
    bdd_success = run_bdd_tests() 
    mock_success = run_mock_tests()
    
    print("\n=== РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ ===")
    print(f"TDD тесты: {'ПРОЙДЕНЫ' if tdd_success else 'НЕ ПРОЙДЕНЫ'}")
    print(f"BDD тесты: {'ПРОЙДЕНЫ' if bdd_success else 'НЕ ПРОЙДЕНЫ'}")
    print(f"Mock тесты: {'ПРОЙДЕНЫ' if mock_success else 'НЕ ПРОЙДЕНЫ'}")
    
    if all([tdd_success, bdd_success, mock_success]):
        print("\n Все тесты пройдены успешно!")
        sys.exit(0)
    else:
        print("\n Некоторые тесты не пройдены!")
        sys.exit(1)