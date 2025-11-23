"""
Демонстрация работы библиотечной системы
"""
from library_system import *


def main():
    print(" ДЕМОНСТРАЦИЯ БИБЛИОТЕЧНОЙ СИСТЕМЫ")
    print("=" * 50)
    
    # Создание библиотеки
    library = Library()
    
    # Добавление наблюдателей
    email_notifier = EmailNotifier("admin@library.ru")
    sms_notifier = SMSNotifier("+7-999-123-45-67")
    logger = Logger()
    
    library.add_observer(email_notifier)
    library.add_observer(sms_notifier)
    library.add_observer(logger)
    
    print("\n1. СОЗДАНИЕ ДОКУМЕНТОВ ЧЕРЕЗ ФАБРИКУ:")
    print("-" * 40)
    
    # Создание документов разных типов
    book = library.add_document("book", "Python Programming", "John Doe", 2023)
    magazine = library.add_document("magazine", "Science Today", "Editor", 2024)
    article = library.add_document("article", "AI Research", "Dr. Smith", 2023)
    
    print(f" Создана книга: {book.title}")
    print(f" Создан журнал: {magazine.title}") 
    print(f" Создана статья: {article.title}")
    
    print("\n2. РАБОТА АДАПТЕРА:")
    print("-" * 40)
    
    # Демонстрация работы адаптера
    doc_id = library.adapter.add_document(book)
    doc_info = library.adapter.get_document(doc_id)
    
    print(f" ID документа в старой системе: {doc_id}")
    print(f" Информация: {doc_info['title']} ({doc_info['type']})")
    print(f" Доступен: {doc_info['available']}")
    
    print("\n3. ВЫДАЧА И ВОЗВРАТ ДОКУМЕНТОВ:")
    print("-" * 40)
    
    # Workflow выдачи и возврата
    print(" Выдача книги...")
    library.borrow_document("Python Programming", "user123")
    
    print(" Возврат книги...")
    library.return_document("Python Programming", "user123")
    
    print("\n4. СТАТИСТИКА:")
    print("-" * 40)
    
    print(f" Всего документов: {len(library.documents)}")
    print(f" Доступно: {len(library.get_available_documents())}")
    print(f" Email уведомлений: {len(email_notifier.notifications)}")
    print(f" SMS уведомлений: {len(sms_notifier.notifications)}")
    print(f" Логов: {len(logger.logs)}")
    
    print("\n" + "=" * 50)
    print(" Демонстрация завершена успешно!")


if __name__ == "__main__":
    main()