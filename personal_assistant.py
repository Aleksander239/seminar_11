# main.py
from services.note_service import NoteService
from services.task_service import TaskService
from services.contact_service import ContactService
from services.finance_record_service import FinanceService
from utils.Calculator import Calculator
from utils.validation import validate_date, validate_email
from models.note import Note
from models.task import Task
from models.contact import Contact
from models.finance_record import FinanceRecord


def manage_notes():
    note_service = NoteService()
    while True:
        print("\nУправление заметками:")
        print("1. Добавить заметку")
        print("2. Просмотреть все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Экспорт заметок в CSV")
        print("6. Импорт заметок из CSV")
        print("7. Назад")

        choice = input("Ваш выбор: ")

        if choice == '1':
            id = input("Введите идентификатор заметки: ")
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержание заметки: ")
            timestamp = input("Введите время заметки: ")
            if validate_date(timestamp):
                note_service.add_note(Note(id, title, content, timestamp))
                print("Заметка успешно добавлена.")
            else:
                print("Некорректная дата. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.")
        elif choice == '2':
            notes = note_service.get_all_notes()
            for i, note in enumerate(notes):
                print(f"{i + 1}. {note.title}")
        elif choice == '3':
            id = int(input("Введите идентификатор заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            content = input("Введите новое содержание заметки: ")
            timestamp = input("Введите новое время заметки: ")
            note_service.update_note(id, Note(id, title, content, timestamp))
            print("Заметка успешно отредактирована.")
        elif choice == '4':
            id = int(input("Введите идентификатор заметки для удаления: "))
            note_service.delete_note(id)
            print("Заметка успешно удалена.")
        elif choice == '5':
            note_service.export_to_csv()
            print("Заметки успешно экспортированы в файл export.csv.")
        elif choice == '6':
            imported_notes = note_service.import_from_csv()
            for note in imported_notes:
                note_service.add_note(Note(note['id'], note['title'], note['content'], note['timestamp']))
            print("Заметки успешно импортированы.")
        elif choice == '7':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def manage_tasks():
    task_service = TaskService()
    while True:
        print("\nУправление задачами:")
        print("1. Добавить задачу")
        print("2. Просмотреть все задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Экспорт задач в CSV")
        print("6. Импорт задач из CSV")
        print("7. Назад")

        choice = input("Ваш выбор: ")

        if choice == '1':
            id = input("Введите идентификатор задачи: ")
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            priority = input("Введите приоритет задачи: ")
            due_date = input("Введите срок выполнения (ДД-ММ-ГГГГ): ")
            if validate_date(due_date):
                task_service.add_task(Task(id, title, description, title, due_date))
                print("Задача успешно добавлена.")
            else:
                print("Некорректная дата. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.")
        elif choice == '2':
            tasks = task_service.get_all_tasks()
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task.description} (до {task.due_date})")
        elif choice == '3':
            id = int(input("Введите идентификатор задачи для отметки как выполненной: "))
            task_service.mark_as_done(id)
            print("Задача отмечена как выполненная.")
        elif choice == '4':
            id = int(input("Введите ижентификатор задачи для удаления: "))
            task_service.delete_task(id)
            print("Задача успешно удалена.")
        elif choice == '5':
            task_service.export_to_csv()
            print("Задачи успешно экспортированы в файл export.csv.")
        elif choice == '6':
            imported_tasks = task_service.import_from_csv()
            for task in imported_tasks:
                task_service.add_task(Task(task['id'], task['title'], task['description'], task['due_date'], task['priority'], task['done']))
            print("Задачи успешно импортированы.")
        elif choice == '7':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def manage_contacts():
    contact_service = ContactService()
    while True:
        print("\nУправление контактами:")
        print("1. Добавить контакт")
        print("2. Просмотреть все контакты")
        print("3. Обновить контакт")
        print("4. Удалить контакт")
        print("5. Экспорт контактов в CSV")
        print("6. Импорт контактов из CSV")
        print("7. Назад")

        choice = input("Ваш выбор: ")

        if choice == '1':
            id = input("Введите идентификатор контакта: ")
            name = input("Введите имя контакта: ")
            email = input("Введите email контакта: ")
            phone = input("Введите номер телефона контакта: ")
            if validate_email(email):
                contact_service.add_contact(Contact(id, name, email, phone))
                print("Контакт успешно добавлен.")
            else:
                print("Некорректный email. Пожалуйста, проверьте правильность ввода.")
        elif choice == '2':
            contacts = contact_service.get_all_contacts()
            for i, contact in enumerate(contacts):
                print(
                    f"{i + 1}. {contact.name}, Email: {contact.email}, Телефон: {contact.phone}")
        elif choice == '3':
            id = int(input("Введите номер контакта для обновления: "))
            name = input("Введите новое имя контакта: ")
            email = input("Введите новый email контакта: ")
            phone = input("Введите новый номер телефона контакта: ")
            if validate_email(email):
                contact_service.update_contact(id, Contact(id, name, email, phone))
                print("Контакт успешно обновлён.")
            else:
                print("Некорректный email. Пожалуйста, проверьте правильность ввода.")
        elif choice == '4':
            id = int(input("Введите номер контакта для удаления: "))
            contact_service.delete_contact(id)
            print("Контакт успешно удалён.")
        elif choice == '5':
            contact_service.export_to_csv()
            print("Контакты успешно экспортированы в файл export.csv.")
        elif choice == '6':
            imported_contacts = contact_service.import_from_csv()
            for contact in imported_contacts:
                contact_service.add_contact(Contact(contact['id'], contact['name'],
                                                     contact['email'], contact['phone']))
            print("Контакты успешно импортированы.")
        elif choice == '7':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def manage_finances():
    finance_service = FinanceService()
    while True:
        print("\nУправление финансами:")
        print("1. Добавить финансовую запись")
        print("2. Просмотреть все финансовые записи")
        print("3. Сформировать финансовый отчёт")
        print("4. Экспорт финансовых записей в CSV")
        print("5. Импорт финансовых записей из CSV")
        print("6. Назад")

        choice = input("Ваш выбор: ")

        if choice == '1':
            id = input("Введите идентификатор транзакции: ")
            date = input("Введите дату транзакции (ДД-ММ-ГГГГ): ")
            amount = float(input("Введите сумму транзакции: "))
            category = input("Введите категорию транзакции: ")
            discription = input("Введите описание транзакции: ")
            if validate_date(date):
                finance_service.add_record(FinanceRecord(id, date, amount, category, discription))
                print("Финансовая запись успешно добавлена.")
            else:
                print("Некорректная дата. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.")
        elif choice == '2':
            records = finance_service.get_all_records()
            for i, record in enumerate(records):
                print(f"{i + 1}. Дата: {record.date}, Сумма: {record.amount}, Категория: {record.category}")
        elif choice == '3':
            start_date = input("Введите начальную дату периода (ДД-ММ-ГГГГ): ")
            end_date = input("Введите конечную дату периода (ДД-ММ-ГГГГ): ")
            if validate_date(start_date) and validate_date(end_date):
                report = finance_service.generate_report(start_date, end_date)
                report
            else:
                print("Некорректные даты. Пожалуйста, введите даты в формате ДД-ММ-ГГГГ.")
        elif choice == '4':
            finance_service.export_to_csv()
            print("Финансовые записи успешно экспортированы в файл finance_export.csv.")
        elif choice == '5':
            imported_records = finance_service.import_from_csv()
            for record in imported_records:
                finance_service.add_record(FinanceRecord(record['id'], record['date'], record['amount'], record['category'], record['discription']))
            print("Финансовые записи успешно импортированы.")
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def use_calculator():
    calculator = Calculator()
    while True:
        print("\nКалькулятор:")
        expression = input("Введите выражение для вычисления (или 'q' для выхода): ")
        if expression.lower() == 'q':
            break
        result = calculator.calculate(expression)
        print(f"Результат: {result}")


def main():
    print("Добро пожаловать в персонального помощника!")
    while True:
        print("\nМеню:")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансами")
        print("5. Калькулятор")
        print("6. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            manage_notes()
        elif choice == '2':
            manage_tasks()
        elif choice == '3':
            manage_contacts()
        elif choice == '4':
            manage_finances()
        elif choice == '5':
            use_calculator()
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()