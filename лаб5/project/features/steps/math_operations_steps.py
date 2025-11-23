"""
BDD шаги для тестирования математических операций
"""
from behave import given, when, then
from math_operations import field, filter_data, transform_data, calculate_average, DataProcessor

@given('у меня есть список словарей')
def step_given_test_data(context):
    """Шаг: задание тестовых данных"""
    context.test_data = [
        {'name': 'Анна', 'age': 25, 'salary': 50000},
        {'name': 'Алексей', 'age': 30, 'salary': 60000},
        {'name': 'Мария', 'age': 28, 'salary': 55000},
        {'name': None, 'age': 35, 'salary': 70000}
    ]

@given('у меня есть DataProcessor с тестовыми данными')
def step_given_data_processor(context):
    """Шаг: создание DataProcessor"""
    test_data = [
        {'name': 'Анна', 'age': 25, 'salary': 50000},
        {'name': 'Алексей', 'age': 30, 'salary': 60000},
        {'name': 'Анна', 'age': 28, 'salary': 55000},  # Дубликат
        {'name': 'Мария', 'age': 35, 'salary': 70000}
    ]
    context.processor = DataProcessor(test_data)

@when('я выбираю поле "{field_name}" с помощью функции field')
def step_when_field_single(context, field_name):
    """Шаг: выборка одного поля"""
    context.result = list(field(context.test_data, field_name))

@when('я фильтрую данные по условию возраста больше {age:d}')
def step_when_filter_by_age(context, age):
    """Шаг: фильтрация по возрасту"""
    context.result = context.processor.filter_by_condition(lambda x: x['age'] > age)

@when('я получаю уникальные значения поля "{field_name}"')
def step_when_unique_values(context, field_name):
    """Шаг: получение уникальных значений"""
    context.result = context.processor.get_unique_values(field_name)

@when('я вычисляю среднее значение поля "{field_name}"')
def step_when_calculate_average(context, field_name):
    """Шаг: вычисление среднего значения"""
    context.result = context.processor.calculate_field_average(field_name)

@then('я получаю список из {count:d} имен')
def step_then_get_names_list(context, count):
    """Шаг: проверка списка имен"""
    assert len(context.result) == count, f"Ожидалось {count} имен, получено {len(context.result)}"

@then('я получаю {count:d} записей')
def step_then_get_records_count(context, count):
    """Шаг: проверка количества записей"""
    assert len(context.result) == count, f"Ожидалось {count} записей, получено {len(context.result)}"

@then('я получаю {count:d} уникальных значений')
def step_then_get_unique_count(context, count):
    """Шаг: проверка количества уникальных значений"""
    assert len(context.result) == count, f"Ожидалось {count} уникальных значений, получено {len(context.result)}"

@then('среднее значение равно {expected_value:f}')
def step_then_average_value(context, expected_value):
    """Шаг: проверка среднего значения"""
    assert abs(context.result - expected_value) < 0.01, f"Ожидалось {expected_value}, получено {context.result}"