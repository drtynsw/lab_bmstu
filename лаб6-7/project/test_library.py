"""
Модульные тесты для библиотечной системы
"""
import unittest
from unittest.mock import Mock, MagicMock, patch
from library_system import *


class TestDocumentFactory(unittest.TestCase):
    """Тесты фабрики документов"""
    
    def test_create_book(self):
        book = DocumentFactory.create_document("book", "Test Book", "Author", 2023)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.get_type(), "Book")
        self.assertEqual(book.get_loan_period(), 30)
    
    def test_create_magazine(self):
        magazine = DocumentFactory.create_document("magazine", "Test Magazine", "Editor", 2023)
        self.assertIsInstance(magazine, Magazine)
        self.assertEqual(magazine.get_type(), "Magazine")
        self.assertEqual(magazine.get_loan_period(), 14)
    
    def test_create_article(self):
        article = DocumentFactory.create_document("article", "Test Article", "Researcher", 2023)
        self.assertIsInstance(article, Article)
        self.assertEqual(article.get_type(), "Article")
        self.assertEqual(article.get_loan_period(), 7)
    
    def test_invalid_document_type(self):
        with self.assertRaises(ValueError):
            DocumentFactory.create_document("invalid", "Test", "Author", 2023)


class TestDocumentMethods(unittest.TestCase):
    """Тесты методов документов"""
    
    def setUp(self):
        self.book = Book("Python Programming", "John Doe", 2023)
    
    def test_borrow_and_return(self):
        self.assertTrue(self.book.is_available())
        
        self.assertTrue(self.book.borrow())
        self.assertFalse(self.book.is_available())
        
        self.assertTrue(self.book.return_doc())
        self.assertTrue(self.book.is_available())
    
    def test_double_borrow(self):
        self.assertTrue(self.book.borrow())
        self.assertFalse(self.book.borrow())  # Нельзя взять уже занятую книгу
    
    def test_get_info(self):
        info = self.book.get_info()
        self.assertEqual(info["title"], "Python Programming")
        self.assertEqual(info["author"], "John Doe")
        self.assertEqual(info["type"], "Book")
        self.assertTrue(info["available"])


class TestAdapterPattern(unittest.TestCase):
    """Тесты паттерна Адаптер"""
    
    def setUp(self):
        self.old_system = OldLibrarySystem()
        self.adapter = LibraryAdapter(self.old_system)
        self.book = Book("Adapter Test", "Test Author", 2023)
    
    def test_add_document_via_adapter(self):
        doc_id = self.adapter.add_document(self.book)
        
        self.assertIsInstance(doc_id, int)
        
        old_data = self.old_system.retrieve_document(doc_id)
        self.assertEqual(old_data["name"], "Adapter Test")
        self.assertEqual(old_data["creator"], "Test Author")
    
    def test_get_document_via_adapter(self):
        doc_id = self.adapter.add_document(self.book)
        modern_data = self.adapter.get_document(doc_id)
        
        self.assertEqual(modern_data["title"], "Adapter Test")
        self.assertEqual(modern_data["author"], "Test Author")
        self.assertEqual(modern_data["type"], "Book")
    
    def test_check_availability(self):
        doc_id = self.adapter.add_document(self.book)
        self.assertTrue(self.adapter.is_available(doc_id))
        
        self.book.borrow()
        doc_id2 = self.adapter.add_document(self.book)
        self.assertFalse(self.adapter.is_available(doc_id2))


class TestObserverPattern(unittest.TestCase):
    """Тесты паттерна Наблюдатель"""
    
    def setUp(self):
        self.subject = Subject()
        self.email_observer = EmailNotifier("test@example.com")
        self.sms_observer = SMSNotifier("+1234567890")
        self.book = Book("Observer Test", "Author", 2023)
    
    def test_attach_and_notify(self):
        self.subject.attach(self.email_observer)
        self.subject.attach(self.sms_observer)
        
        event = LibraryEvent("TEST_EVENT", self.book, "user123")
        self.subject.notify(event)
        
        self.assertEqual(len(self.email_observer.notifications), 1)
        self.assertEqual(len(self.sms_observer.notifications), 1)
    
    def test_detach_observer(self):
        self.subject.attach(self.email_observer)
        self.subject.attach(self.sms_observer)
        
        self.subject.detach(self.email_observer)
        
        event = LibraryEvent("TEST_EVENT", self.book)
        self.subject.notify(event)
        
        self.assertEqual(len(self.email_observer.notifications), 0)
        self.assertEqual(len(self.sms_observer.notifications), 1)


class TestLibraryIntegration(unittest.TestCase):
    """Интеграционные тесты библиотеки"""
    
    def setUp(self):
        self.library = Library()
        self.email_notifier = EmailNotifier("user@example.com")
        self.library.add_observer(self.email_notifier)
    
    def test_add_document(self):
        document = self.library.add_document("book", "Integration Test", "Author", 2023)
        
        self.assertIsInstance(document, Book)
        self.assertEqual(len(self.library.documents), 1)
        self.assertEqual(len(self.email_notifier.notifications), 1)
    
    def test_borrow_return_workflow(self):
        document = self.library.add_document("book", "Workflow Test", "Author", 2023)
        
        # Выдача
        borrow_result = self.library.borrow_document("Workflow Test", "user123")
        self.assertTrue(borrow_result)
        self.assertFalse(document.is_available())
        
        # Возврат
        return_result = self.library.return_document("Workflow Test", "user123")
        self.assertTrue(return_result)
        self.assertTrue(document.is_available())
    
    def test_get_available_documents(self):
        self.library.add_document("book", "Available Book", "Author", 2023)
        self.library.add_document("magazine", "Borrowed Magazine", "Editor", 2023)
        
        # Занимаем один документ
        borrowed_doc = self.library.documents[1]
        borrowed_doc.borrow()
        
        available = self.library.get_available_documents()
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0].title, "Available Book")
    
    def test_get_document_info(self):
        self.library.add_document("book", "Info Test", "Author", 2023)
        
        info = self.library.get_document_info("Info Test")
        self.assertEqual(info["title"], "Info Test")
        self.assertEqual(info["author"], "Author")
        self.assertEqual(info["type"], "Book")
        self.assertTrue(info["available"])


if __name__ == '__main__':
    unittest.main()