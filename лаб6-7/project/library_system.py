"""
Библиотечная система с шаблонами проектирования
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from datetime import datetime
import random


# ==================== ПОРОЖДАЮЩИЙ: Фабричный метод ====================

class Document(ABC):
    """Абстрактный класс документа"""
    
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self._is_borrowed = False
    
    @abstractmethod
    def get_type(self) -> str:
        pass
    
    @abstractmethod
    def get_loan_period(self) -> int:
        pass
    
    def borrow(self) -> bool:
        if not self._is_borrowed:
            self._is_borrowed = True
            return True
        return False
    
    def return_doc(self) -> bool:
        if self._is_borrowed:
            self._is_borrowed = False
            return True
        return False
    
    def is_available(self) -> bool:
        return not self._is_borrowed
    
    def get_info(self) -> Dict[str, Any]:
        return {
            "type": self.get_type(),
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "available": self.is_available(),
            "loan_period": self.get_loan_period()
        }


class Book(Document):
    """Книга"""
    
    def get_type(self) -> str:
        return "Book"
    
    def get_loan_period(self) -> int:
        return 30


class Magazine(Document):
    """Журнал"""
    
    def get_type(self) -> str:
        return "Magazine"
    
    def get_loan_period(self) -> int:
        return 14


class Article(Document):
    """Статья"""
    
    def get_type(self) -> str:
        return "Article"
    
    def get_loan_period(self) -> int:
        return 7


class DocumentFactory:
    """Фабрика документов"""
    
    @staticmethod
    def create_document(doc_type: str, title: str, author: str, year: int) -> Document:
        doc_type = doc_type.lower()
        if doc_type == "book":
            return Book(title, author, year)
        elif doc_type == "magazine":
            return Magazine(title, author, year)
        elif doc_type == "article":
            return Article(title, author, year)
        else:
            raise ValueError(f"Unknown document type: {doc_type}")


# ==================== СТРУКТУРНЫЙ: Адаптер ====================

class OldLibrarySystem:
    """Старая библиотечная система (несовместимый интерфейс)"""
    
    def __init__(self):
        self._storage = {}
    
    def store_document(self, doc_id: int, doc_data: dict) -> None:
        """Сохраняет документ в старом формате"""
        self._storage[doc_id] = doc_data
    
    def retrieve_document(self, doc_id: int) -> dict:
        """Извлекает документ в старом формате"""
        return self._storage.get(doc_id, {})
    
    def check_status_old(self, doc_id: int) -> str:
        """Проверяет статус в старом формате"""
        doc = self._storage.get(doc_id)
        if not doc:
            return "not_exists"
        return "free" if doc.get("is_free", True) else "taken"


class LibraryAdapter:
    """Адаптер для совместимости со старой системой"""
    
    def __init__(self, old_system: OldLibrarySystem):
        self.old_system = old_system
        self._next_id = 1
    
    def add_document(self, document: Document) -> int:
        """Добавляет документ через адаптер"""
        doc_id = self._next_id
        self._next_id += 1
        
        # Преобразование в старый формат
        old_format_data = {
            "name": document.title,
            "creator": document.author,
            "year_published": document.year,
            "doc_type": document.get_type(),
            "is_free": document.is_available()
        }
        
        self.old_system.store_document(doc_id, old_format_data)
        return doc_id
    
    def get_document(self, doc_id: int) -> Dict[str, Any]:
        """Получает документ в современном формате"""
        old_data = self.old_system.retrieve_document(doc_id)
        if not old_data:
            return {}
        
        # Преобразование в современный формат
        return {
            "id": doc_id,
            "title": old_data.get("name", ""),
            "author": old_data.get("creator", ""),
            "year": old_data.get("year_published", 0),
            "type": old_data.get("doc_type", "unknown"),
            "available": old_data.get("is_free", False)
        }
    
    def is_available(self, doc_id: int) -> bool:
        """Проверяет доступность через адаптер"""
        status = self.old_system.check_status_old(doc_id)
        return status == "free"


# ==================== ПОВЕДЕНЧЕСКИЙ: Наблюдатель ====================

class LibraryEvent:
    """Событие в библиотеке"""
    
    def __init__(self, event_type: str, document: Document, user: str = None):
        self.type = event_type
        self.document = document
        self.user = user
        self.timestamp = datetime.now()
    
    def __str__(self):
        user_info = f" by {self.user}" if self.user else ""
        return f"{self.timestamp}: {self.type} - '{self.document.title}'{user_info}"


class Observer(ABC):
    """Абстрактный наблюдатель"""
    
    @abstractmethod
    def update(self, event: LibraryEvent) -> None:
        pass


class Subject:
    """Субъект для наблюдения"""
    
    def __init__(self):
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, event: LibraryEvent) -> None:
        for observer in self._observers:
            observer.update(event)


class EmailNotifier(Observer):
    """Email уведомления"""
    
    def __init__(self, email: str):
        self.email = email
        self.notifications = []
    
    def update(self, event: LibraryEvent) -> None:
        message = f"Email to {self.email}: {event}"
        self.notifications.append(message)
        print(message)


class SMSNotifier(Observer):
    """SMS уведомления"""
    
    def __init__(self, phone: str):
        self.phone = phone
        self.notifications = []
    
    def update(self, event: LibraryEvent) -> None:
        message = f"SMS to {self.phone}: {event.type} - {event.document.title}"
        self.notifications.append(message)
        print(message)


class Logger(Observer):
    """Логгер событий"""
    
    def __init__(self):
        self.logs = []
    
    def update(self, event: LibraryEvent) -> None:
        log_entry = f"LOG: {event}"
        self.logs.append(log_entry)
        print(log_entry)


# ==================== ОСНОВНАЯ СИСТЕМА ====================

class Library:
    """Основная библиотечная система"""
    
    def __init__(self):
        self.documents: List[Document] = []
        self.factory = DocumentFactory()
        self.old_system = OldLibrarySystem()
        self.adapter = LibraryAdapter(self.old_system)
        self.notifier = Subject()
    
    def add_document(self, doc_type: str, title: str, author: str, year: int) -> Document:
        """Добавляет документ в библиотеку"""
        document = self.factory.create_document(doc_type, title, author, year)
        self.documents.append(document)
        
        # Адаптация для старой системы
        self.adapter.add_document(document)
        
        # Уведомление наблюдателей
        event = LibraryEvent("DOCUMENT_ADDED", document)
        self.notifier.notify(event)
        
        return document
    
    def borrow_document(self, title: str, user: str) -> bool:
        """Выдает документ пользователю"""
        for doc in self.documents:
            if doc.title == title and doc.is_available():
                if doc.borrow():
                    event = LibraryEvent("DOCUMENT_BORROWED", doc, user)
                    self.notifier.notify(event)
                    return True
        return False
    
    def return_document(self, title: str, user: str) -> bool:
        """Возвращает документ в библиотеку"""
        for doc in self.documents:
            if doc.title == title and not doc.is_available():
                if doc.return_doc():
                    event = LibraryEvent("DOCUMENT_RETURNED", doc, user)
                    self.notifier.notify(event)
                    return True
        return False
    
    def get_available_documents(self) -> List[Document]:
        """Возвращает список доступных документов"""
        return [doc for doc in self.documents if doc.is_available()]
    
    def get_document_info(self, title: str) -> Dict[str, Any]:
        """Возвращает информацию о документе"""
        for doc in self.documents:
            if doc.title == title:
                return doc.get_info()
        return {}
    
    def add_observer(self, observer: Observer) -> None:
        """Добавляет наблюдателя"""
        self.notifier.attach(observer)