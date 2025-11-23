"""
Тесты с использованием Mock объектов
"""
import unittest
from unittest.mock import Mock, MagicMock, patch
from library_system import *


class TestMockObjects(unittest.TestCase):
    """Тесты с mock объектами"""
    
    def test_mock_document(self):
        """Тест с mock документом"""
        mock_doc = MagicMock()
        mock_doc.title = "Mock Book"
        mock_doc.is_available.return_value = True
        mock_doc.borrow.return_value = True
        
        library = Library()
        library.documents = [mock_doc]
        
        result = library.borrow_document("Mock Book", "user123")
        self.assertTrue(result)
        mock_doc.borrow.assert_called_once()
    
    def test_mock_observer(self):
        """Тест с mock наблюдателем"""
        mock_observer = Mock(spec=Observer)
        subject = Subject()
        subject.attach(mock_observer)
        
        book = Book("Test Book", "Author", 2023)
        event = LibraryEvent("TEST_EVENT", book)
        
        subject.notify(event)
        mock_observer.update.assert_called_once_with(event)
    
    @patch('library_system.DocumentFactory.create_document')
    def test_mock_factory(self, mock_factory):
        """Тест с mock фабрикой"""
        mock_book = MagicMock()
        mock_factory.return_value = mock_book
        
        library = Library()
        document = library.add_document("book", "Any Title", "Any Author", 2023)
        
        mock_factory.assert_called_once_with("book", "Any Title", "Any Author", 2023)
        self.assertEqual(document, mock_book)
    
    def test_mock_adapter(self):
        """Тест с mock адаптером"""
        mock_adapter = MagicMock()
        mock_adapter.add_document.return_value = 42
        
        library = Library()
        library.adapter = mock_adapter
        
        book = Book("Test Book", "Author", 2023)
        library.documents.append(book)
        
        # Имитируем вызов через адаптер
        doc_id = library.adapter.add_document(book)
        self.assertEqual(doc_id, 42)
        mock_adapter.add_document.assert_called_once_with(book)


class TestMockIntegration(unittest.TestCase):
    """Интеграционные тесты с моками"""
    
    @patch('library_system.DocumentFactory.create_document')
    @patch('library_system.LibraryAdapter')
    def test_complete_workflow_with_mocks(self, MockAdapter, mock_factory):
        """Полный workflow с моками"""
        # Настройка моков
        mock_book = MagicMock()
        mock_book.title = "Mock Book"
        mock_book.is_available.return_value = True
        mock_book.borrow.return_value = True
        mock_book.return_doc.return_value = True
        
        mock_factory.return_value = mock_book
        
        mock_adapter_instance = MagicMock()
        MockAdapter.return_value = mock_adapter_instance
        
        # Создание системы
        library = Library()
        library.factory = mock_factory
        library.adapter = mock_adapter_instance
        
        mock_notifier = MagicMock()
        library.notifier = mock_notifier
        
        # Выполнение workflow
        document = library.add_document("book", "Mock Book", "Author", 2023)
        borrow_result = library.borrow_document("Mock Book", "user123")
        return_result = library.return_document("Mock Book", "user123")
        
        # Проверки
        self.assertEqual(document, mock_book)
        self.assertTrue(borrow_result)
        self.assertTrue(return_result)
        
        mock_factory.assert_called_once_with("book", "Mock Book", "Author", 2023)
        self.assertEqual(mock_notifier.notify.call_count, 3)


if __name__ == '__main__':
    unittest.main()