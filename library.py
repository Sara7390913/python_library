# Library Management System
# UML Diagram: image/uml_library.jpg

import tkinter as tk
from tkinter import messagebox


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


window = tk.Tk()

window.title("Library Managemant System")
window.geometry("600x500")
window.resizable(False, False)

books = []


def add_book():
    book_window = tk.Toplevel(window)
    book_window.title("Add Book")
    book_window.geometry("350x300")

    tk.Label(book_window, text="Book ID:").pack(pady=5)
    book_id_entry = tk.Entry(book_window)
    book_id_entry.pack()

    tk.Label(book_window, text="Title:").pack(pady=5)
    book_title_entry = tk.Entry(book_window)
    book_title_entry.pack()

    tk.Label(book_window, text="Details:").pack(pady=5)
    book_details_entry = tk.Entry(book_window)
    book_details_entry.pack()

    tk.Label(book_window, text="Publisher:").pack(pady=5)
    book_publisher_entry = tk.Entry(book_window)
    book_publisher_entry.pack()

    def save_book():
        book_id = book_id_entry.get().strip()
        book_title = book_title_entry.get().strip()
        book_details = book_details_entry.get().strip()
        book_publisher = book_publisher_entry.get().strip()

        if not book_id or not book_title or not book_details or not book_publisher:
            messagebox.showerror("Warning", "Please fill all fields.")
            return

        book = Book(book_id, book_title, book_details, book_publisher)
        books.append(book)

        messagebox.showinfo("Success", f"Book '{book.title}' created successfully!")

        book_window.destroy()

    tk.Button(book_window, text="Save Book", command=save_book).pack(pady=15)


def show_books():
    if not books:
        messagebox.showinfo("Library", "No books registered yet.")
        return

    book_window = tk.Toplevel(window)
    book_window.title("Book List")
    book_window.geometry("500x300")

    for book in books:
        book_info = (f"ID: {book.book_id} | " f"Title: {book.title} | " f" Details: {book.details} | " f"Publisher: {book.publisher}")

        tk.Label(book_window, text=book_info, font=("Arial", 10), wraplength=450).pack(pady=5)


def register_student():
    student_window = tk.Toplevel(window)
    student_window.title("Register Student")
    student_window.geometry("400x350")
    student_window.resizable(False, False)

    tk.Label(student_window, text="Register Student:", font=("Arial", 16, "bold")).pack(pady=15)

    tk.Label(student_window, text="Student ID").pack()
    student_id_entry = tk.Entry(student_window, width=30)
    student_id_entry.pack(pady=5)

    tk.Label(student_window, text="Student Name").pack()
    student_name_entry = tk.Entry(student_window, width=30)
    student_name_entry.pack(pady=5)

    tk.Label(student_window, text="Student Age").pack()
    student_age_entry = tk.Entry(student_window, width=30)
    student_age_entry.pack(pady=5)

    tk.Label(student_window, text="Username").pack()
    student_username_entry = tk.Entry(student_window, width=30)
    student_username_entry.pack(pady=5)

    def save_student():
        student_id = student_id_entry.get()
        student_name = student_name_entry.get()
        student_age = student_age_entry.get()
        username = student_username_entry.get()

        if not student_id or not student_name or not student_age or not username:
            messagebox.showwarning("Warning", "Please fill all fields!")
            return



        messagebox.showinfo("Success", f"Student '{student_name}' registered successfully!")
        student_window.destroy()

    tk.Button(student_window, text="Register", width=15, height=1, font=("Arial", 11), command=save_student).pack(pady=15)



def borrow_book():
    messagebox.showinfo("Library", "Borrow Book")


title = tk.Label(window, text="Library Managemant System", font=("Arial", 18, "bold"))
title.pack(pady=45)

tk.Button(window, text="Add Book", width=25, height=2, font=("Arial", 12), command=add_book).pack(pady=10)

tk.Button(window, text="Show Books", width=25, height=2, font=("Arial", 12), command=show_books).pack(pady=10)

tk.Button(window, text="Register Student", width=25, height=2, font=("Arial", 12), command=register_student).pack(
    pady=10)

tk.Button(window, text="Borrow Book", width=25, height=2, font=("Arial", 12), command=borrow_book).pack(pady=10)

window.mainloop()
