# Task:

# Develop a book library management system using object-oriented programming (OOP) in Python. Implement classes for books, the library, customers, and the library management system. Consider the quantity of each book in the library.

# Class Book:
# Attributes: title (book title), author (author), year (publication year), quantity (number of copies of the book in the library, default is 1).

# Method display_info, which prints information about the book.

# Class EBook:
# Inherits from the Book class.
# Attribute: format_type (format of the electronic book, e.g., PDF).
# Overrides the display_info method to print additional information about the electronic book format.

# Class Library:
# Attributes: books (list of books in the library), book_count (total number of books in the library).
# Method add_book, which adds a new book to the library and increments book_count.
# Method display_books, which prints the list of all books in the library.

# Class Customer:
# Attributes: name (customer name), borrowed_books (list of borrowed books).
# Method borrow_book, allowing the customer to borrow a book from the library.
# Method return_book, allowing the customer to return a borrowed book.

# Class LibraryManagementSystem:
# Attributes: library (object of the Library class), customers (list of customers).
# Method register_customer, which adds a new customer to the system.
# Method display_customer_books, which prints the list of books borrowed by a specific customer at the current time.
# Method display_all_books, which prints the list of all books in the library.

### **Перевод задачи на русский язык**  

### **Задача:**  
# Разработать **систему управления библиотекой** с использованием **объектно-ориентированного программирования (OOP) в Python**.  
# Реализовать классы для **книг, библиотеки, клиентов и системы управления библиотекой**.  
# Необходимо учитывать **количество экземпляров** каждой книги в библиотеке.  

# ### **Классы и их описание:**  
# 1️⃣ **Класс `Book`**  
#    - **Атрибуты**:  
#      - `title` – название книги  
#      - `author` – автор  
#      - `year` – год издания  
#      - `quantity` – количество экземпляров в библиотеке (по умолчанию = 1)  
#    - **Метод `display_info`** – печатает информацию о книге.  

# 2️⃣ **Класс `EBook` (наследуется от `Book`)**  
#    - **Дополнительный атрибут**:  
#      - `format_type` – формат электронной книги (например, PDF).  
#    - **Переопределённый метод `display_info`** – добавляет формат книги в вывод.  

# 3️⃣ **Класс `Library`**  
#    - **Атрибуты**:  
#      - `books` – список книг в библиотеке  
#      - `book_count` – общее количество книг  
#    - **Методы**:  
#      - `add_book()` – добавляет книгу в библиотеку, увеличивая `book_count`.  
#      - `display_books()` – выводит список всех книг.  

# 4️⃣ **Класс `Customer`**  
#    - **Атрибуты**:  
#      - `name` – имя клиента  
#      - `borrowed_books` – список взятых книг  
#    - **Методы**:  
#      - `borrow_book()` – клиент берёт книгу из библиотеки.  
#      - `return_book()` – клиент возвращает книгу в библиотеку.  

# 5️⃣ **Класс `LibraryManagementSystem`**  
#    - **Атрибуты**:  
#      - `library` – объект класса `Library`  
#      - `customers` – список клиентов  
#    - **Методы**:  
#      - `register_customer()` – регистрирует нового клиента.  
#      - `display_customer_books()` – выводит список книг, которые клиент сейчас держит.  
#      - `display_all_books()` – выводит список всех книг в библиотеке.  

## **Код решения**  
class Book:
    def __init__(self, title, author, year, quantity=1):
        """Инициализация объекта книги"""
        self.title = title
        self.author = author
        self.year = year
        self.quantity = quantity

    def display_info(self):
        """Вывод информации о книге"""
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Quantity: {self.quantity}")


class EBook(Book):
    def __init__(self, title, author, year, format_type, quantity=1):
        """Инициализация объекта электронной книги"""
        super().__init__(title, author, year, quantity)
        self.format_type = format_type

    def display_info(self):
        """Вывод информации о книге, включая формат"""
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Format: {self.format_type}, Quantity: {self.quantity}")


class Library:
    def __init__(self):
        """Инициализация библиотеки с пустым списком книг"""
        self.books = []
        self.book_count = 0

    def add_book(self, book):
        """Добавление книги в библиотеку"""
        self.books.append(book)
        self.book_count += book.quantity

    def display_books(self):
        """Вывод списка всех книг в библиотеке"""
        if not self.books:
            print("Library is empty.")
        else:
            for book in self.books:
                book.display_info()


class Customer:
    def __init__(self, name):
        """Инициализация клиента"""
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, title):
        """Взятие книги из библиотеки"""
        for book in library.books:
            if book.title == title and book.quantity > 0:
                self.borrowed_books.append(book)
                book.quantity -= 1
                print(f"{self.name} borrowed {title}.")
                return
        print(f"{title} is not available.")

    def return_book(self, library, title):
        """Возврат книги в библиотеку"""
        for book in self.borrowed_books:
            if book.title == title:
                self.borrowed_books.remove(book)
                book.quantity += 1
                print(f"{self.name} returned {title}.")
                return
        print(f"{self.name} does not have {title}.")


class LibraryManagementSystem:
    def __init__(self):
        """Инициализация системы управления библиотекой"""
        self.library = Library()
        self.customers = []

    def register_customer(self, name):
        """Регистрация нового клиента"""
        customer = Customer(name)
        self.customers.append(customer)
        print(f"Customer {name} registered.")
        return customer

    def display_customer_books(self, customer):
        """Вывод списка книг, взятых клиентом"""
        if not customer.borrowed_books:
            print(f"{customer.name} has no borrowed books.")
        else:
            print(f"Books borrowed by {customer.name}:")
            for book in customer.borrowed_books:
                book.display_info()

    def display_all_books(self):
        """Вывод списка всех книг в библиотеке"""
        self.library.display_books()

## **🔎 Пошаговое объяснение кода**

### **📚 `Book` и `EBook`**
# ✔ **`Book`** хранит заголовок, автора, год издания и количество экземпляров.  
# ✔ **`EBook`** наследуется от `Book`, добавляя `format_type` (формат, например `PDF`).  
# ✔ **Метод `display_info()`** **переопределяется в `EBook`**, чтобы показать формат книги.

### **🏛 `Library`**
# ✔ **Хранит список книг (`books`) и их количество (`book_count`).**  
# ✔ **Метод `add_book()`** добавляет книгу в библиотеку.  
# ✔ **Метод `display_books()`** показывает все книги.

### **👤 `Customer`**
# ✔ **Хранит имя клиента и список книг, которые он взял (`borrowed_books`).**  
# ✔ **Метод `borrow_book()`** позволяет клиенту взять книгу (если она доступна).  
# ✔ **Метод `return_book()`** позволяет клиенту вернуть книгу.

### **🏢 `LibraryManagementSystem`**
# ✔ **Хранит объект `Library` и список `customers`.**  
# ✔ **Метод `register_customer()`** добавляет клиента.  
# ✔ **Метод `display_customer_books()`** показывает, какие книги клиент держит.  
# ✔ **Метод `display_all_books()`** выводит все книги библиотеки.

## **✅ Тестирование системы**
# Создаём систему управления библиотекой
system = LibraryManagementSystem()

# Добавляем книги
book1 = Book("1984", "George Orwell", 1949, 3)
book2 = EBook("Python for Beginners", "John Doe", 2020, "PDF", 5)

system.library.add_book(book1)
system.library.add_book(book2)

# Регистрируем клиентов
alice = system.register_customer("Alice")
bob = system.register_customer("Bob")

# Клиенты берут книги
alice.borrow_book(system.library, "1984")
bob.borrow_book(system.library, "Python for Beginners")

# Проверяем книги, которые держат клиенты
system.display_customer_books(alice)
system.display_customer_books(bob)

# Проверяем все книги в библиотеке
system.display_all_books()

### **🔎 Выходные данные**
# Customer Alice registered.
# Customer Bob registered.
# Alice borrowed 1984.
# Bob borrowed Python for Beginners.
# Books borrowed by Alice:
# Title: 1984, Author: George Orwell, Year: 1949, Quantity: 2
# Books borrowed by Bob:
# Title: Python for Beginners, Author: John Doe, Year: 2020, Format: PDF, Quantity: 4
# Title: 1984, Author: George Orwell, Year: 1949, Quantity: 2
# Title: Python for Beginners, Author: John Doe, Year: 2020, Format: PDF, Quantity: 4