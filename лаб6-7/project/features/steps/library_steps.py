"""
BDD шаги для библиотечной системы
"""
from behave import given, when, then
from library_system import *


@given('библиотечная система')
def step_create_library(context):
    context.library = Library()


@given('фабрика документов')
def step_create_factory(context):
    context.factory = DocumentFactory()


@given('адаптер для старой системы')
def step_create_adapter(context):
    context.old_system = OldLibrarySystem()
    context.adapter = LibraryAdapter(context.old_system)


@given('email уведомления для "{email}"')
def step_create_email_notifier(context, email):
    context.email_notifier = EmailNotifier(email)
    context.library.add_observer(context.email_notifier)


@given('документ "{doc_type}" с названием "{title}" автора "{author}" {year:d} года')
def step_create_document(context, doc_type, title, author, year):
    context.document = context.factory.create_document(doc_type, title, author, year)


@given('добавлен документ "{doc_type}" с названием "{title}" автора "{author}" {year:d} года')
def step_add_document_to_library(context, doc_type, title, author, year):
    context.library.add_document(doc_type, title, author, year)


@when('я создаю документ "{doc_type}" с названием "{title}" автора "{author}" {year:d} года')
def step_create_document_action(context, doc_type, title, author, year):
    context.document = context.factory.create_document(doc_type, title, author, year)


@when('я добавляю документ в библиотеку')
def step_add_document_to_library_action(context):
    context.library.documents.append(context.document)


@when('пользователь "{user}" берет документ "{title}"')
def step_borrow_document(context, user, title):
    context.borrow_result = context.library.borrow_document(title, user)


@when('пользователь "{user}" возвращает документ "{title}"')
def step_return_document(context, user, title):
    context.return_result = context.library.return_document(title, user)


@when('я добавляю документ через адаптер')
def step_add_document_via_adapter(context):
    context.doc_id = context.adapter.add_document(context.document)


@then('документ должен быть типа "{doc_type}"')
def step_check_document_type(context, doc_type):
    assert context.document.get_type() == doc_type


@then('период выдачи должен быть {days:d} дней')
def step_check_loan_period(context, days):
    assert context.document.get_loan_period() == days


@then('документ должен быть доступен')
def step_check_document_available(context):
    assert context.document.is_available()


@then('документ должен быть недоступен')
def step_check_document_unavailable(context):
    assert not context.document.is_available()


@then('операция выдачи должна быть успешной')
def step_check_borrow_success(context):
    assert context.borrow_result is True


@then('операция возврата должна быть успешной')
def step_check_return_success(context):
    assert context.return_result is True


@then('я должен получить ID документа')
def step_check_document_id(context):
    assert hasattr(context, 'doc_id')
    assert isinstance(context.doc_id, int)


@then('уведомление должно быть отправлено')
def step_check_notification_sent(context):
    assert len(context.email_notifier.notifications) > 0