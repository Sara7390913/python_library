#Library Management System
#UML Diagram: image/uml_library.jpg
class User:
    def __init__(self, user_id, name, age, username, password):
        self._user_id = user_id
        self.name = name
        self.age = age
        self._username = username
        self._password = password

    def create(self):
        pass

    def update(self):
        pass


class Student(User):
    def __init__(self, user_id, name, age, username, password, course, year):
        super().__init__(user_id, name, age, username, password)
        self.course = course
        self.year = year

    def browse_books(self):
        pass


class Librarian(User):
    def __init__(self, user_id, name, age, username, password, department):
        super().__init__(user_id, name, age, username, password)
        self.department = department

    def _enable_user(self):
        pass

    def _disable_user(self):
        pass


class Book:
    def __init__(self, book_id, title, details, publisher):
        self.book_id = book_id
        self.title = title
        self.details = details
        self.publisher = publisher



    def add(self):
        pass


    def update(self):
        pass


class Borrowing:
    def __init__(self, borrowing_id, bookname, borrower, date_borrowed, date_due):
        self.borrowing_id = borrowing_id
        self.bookname = bookname
        self.borrower = borrower
        self.date_borrowed = date_borrowed
        self.date_due = date_due


    def create(self):
        pass



    def update(self):
        pass


class Transaction:
    def __init__(self, transaction_id, details, date):
        self.transaction_id = transaction_id
        self.details = details
        self.date = date


    def update(self):
        pass
