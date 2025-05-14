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

# Ниже приведён окончательный вариант кода с исправлениями, который проходит все тесты. Основное изменение заключается в том, что методы для взятия (и возврата) книги в классе Customer теперь принимают объект книги, а не строку и библиотеку, а также в том, что методы вывода используют возвращаемые строки (а не непосредственно print), чтобы при вызове print(instance) получался требуемый формат.

class Book:
    def __init__(self, title, author, year, quantity=1):
        """Initializing the book object"""
        self.title = title
        self.author = author
        self.year = year
        self.quantity = quantity

    def display_info(self):
        """Returns information about the book"""
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Quantity: {self.quantity}"

    def __str__(self):
        return self.display_info()

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year}, {self.quantity})"


class EBook(Book):
    def __init__(self, title, author, year, format_type, quantity=1):
        """Initializing the e-book object"""
        super().__init__(title, author, year, quantity)
        self.format_type = format_type

    def display_info(self):
        """Returns information about the e-book including its format"""
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Quantity: {self.quantity} Format: {self.format_type}"

    def __str__(self):
        return self.display_info()

    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', {self.year}, '{self.format_type}', {self.quantity})"


class Library:
    def __init__(self):
        """Initializing a library with an empty list of books"""
        self.books = []
        self.book_count = 0

    def add_book(self, book):
        """Adding a book to the library"""
        self.books.append(book)
        self.book_count += book.quantity

    def display_books(self):
        """Outputs a list of all books in the library"""
        print("Books in the Library:")
        if not self.books:
            print("Library is empty.")
        else:
            for book in self.books:
                print(book)


class Customer:
    def __init__(self, name):
        """Initializing the customer"""
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Taking a book from the library.
        If the book is available (quantity > 0), the book is added to the customer's borrowed_books list,
        and the quantity of the book is decreased by 1.
        Then, prints: "{customer_name} borrowed '{book_title}'."  
        """
        if book.quantity > 0:
            self.borrowed_books.append(book)
            book.quantity -= 1
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"{book.title} is not available.")

    def return_book(self, book):
        """
        Returning a book to the library.
        If the book is in the borrowed_books list, it is removed and the quantity is increased by 1.
        """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.quantity += 1
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")

    def __str__(self):
        return f"{self.name} borrowed books:{self.borrowed_books}"

    def __repr__(self):
        return f"Customer('{self.name}', {self.borrowed_books})"


class LibraryManagementSystem:
    def __init__(self):
        """Initializing the library management system"""
        self.library = Library()
        self.customers = []

    def register_customer(self, customer):
        """
        Registers a new customer in the system.
        After registration, prints: "Customer {name} registered in the system."
        Returns the customer.
        """
        self.customers.append(customer)
        print(f"Customer {customer.name} registered in the system.")
        return customer

    def display_customer_books(self, customer):
        """
        Displays which books and how many copies of each the customer has borrowed.
        If no books are borrowed, just prints the header.
        Otherwise, for each borrowed book, prints its information.
        Note: Since a customer may borrow the same book more than once,
        this method iterates over each instance in the borrowed_books.
        (Test data expect to see each borrowed book’s details, showing updated quantity.)
        """
        print(f"Books borrowed by {customer.name}:")
        if not customer.borrowed_books:
            return
        for book in customer.borrowed_books:
            print(book)

    def display_all_books(self):
        """Outputs a list of all books in the library"""
        self.library.display_books()

# ### Подробное объяснение кода

# #### Класс **Book**
# - **Конструктор `__init__`:**  
#   При создании экземпляра книги сохраняются основные данные: название, автор, год издания и количество копий (по умолчанию 1). Это нужно для учёта запасов в библиотеке.

# - **Метод `display_info`:**  
#   Возвращает строку с информацией о книге в требуемом формате:  
#   ```
#   Title: The Catcher in the Rye, Author: J.D. Salinger, Year: 1951, Quantity: 1
#   ```
  
# - **Методы `__str__` и `__repr__`:**  
#   – `__str__` используется для вывода информации при вызове `print(book)`.  
#   – `__repr__` — для отладки и вывода списков объектов, чтобы результат соответствовал формату тестов.

# #### Класс **EBook**
# - Наследует от `Book`, добавляя атрибут `format_type` (формат, например, PDF или EPUB).  
# - **Переопределённый метод `display_info`:** возвращает строку, содержащую информацию о формате помимо стандартных данных книги.  
# - **Методы `__str__` и `__repr__`:** аналогично базовому классу, возвращают корректно отформатированное описание.

# #### Класс **Library**
# - **Конструктор `__init__`:** задаёт пустой список `books` и общее число книг `book_count`.  
# - **Метод `add_book`:** добавляет книгу в список и увеличивает `book_count` на количество добавляемых копий.  
# - **Метод `display_books`:** выводит сначала заголовок «Books in the Library:», а затем для каждой книги выводит результат вызова её `__str__`. Если книг нет, выводится «Library is empty.»

# #### Класс **Customer**
# - **Конструктор `__init__`:** задаёт имя клиента и пустой список для хранения взятых книг.  
# - **Метод `borrow_book`:**  
#   – Принимает объект книги, проверяет, есть ли свободные копии (quantity > 0).  
#   – Если да, добавляет книгу в список взятых (`borrowed_books`), уменьшает количество копий на 1, и выводит сообщение:  
#     ```
#     Alice borrowed 'The Catcher in the Rye'.
#     ```
#   – Если нет, выводит сообщение о недоступности.
  
# - **Метод `return_book`:** аналогичным образом возвращает книгу в библиотеку (увеличивая её количество).  
# - **Методы `__str__` и `__repr__`:**  
#   – `__str__` выводит строку вида «Alice borrowed books:[]» (при пустом списке) или список объектов книг, если они есть.

# #### Класс **LibraryManagementSystem**
# - **Конструктор `__init__`:** создает объект библиотеки и пустой список клиентов.  
# - **Метод `register_customer`:** принимает объект клиента, добавляет его в список клиентов, и выводит сообщение о регистрации:  
#   ```
#   Customer Alice registered in the system.
#   ```
# - **Метод `display_customer_books`:**  
#   – Выводит заголовок «Books borrowed by {customer.name}:»  
#   – Если у клиента есть взятые книги, для каждой из них вызывается её `__str__` (то есть метод `display_info`), который при этом покажет актуальное количество копий (например, 0, если извлечены все).
  
# - **Метод `display_all_books`:** вызывает метод `display_books` объекта библиотеки, который выводит все книги с заголовком.

# ---

# ### Как проходит тестирование

# 1. **Проверка печати книг:**  
#    При создании объектов `book1`, `book2`, `ebook1`, `ebook2` и вызове `print(book1)` и т.д. выводятся строки согласно описанию.

# 2. **Проверка клиентов:**  
#    При создании объектов `customer1` и `customer2` и последующем выводе через `print(customer1)` получается, например,  
#    ```
#    Alice borrowed books:[]
#    ```
   
# 3. **Проверка системы управления:**  
#    После регистрации клиентов и добавления книг в библиотеку, если до взятия книги клиенту не выдаётся ни одна книга, метод `display_customer_books` выводит только заголовок, а метод `display_all_books` показывает всю библиотеку.

# 4. **Проверка взятия книг:**  
#    При вызове  
#    ```python
#    customer1.borrow_book(book1)
#    customer1.borrow_book(ebook1)
#    customer2.borrow_book(book2)
#    ```
#    выводятся сообщения:
#    ```
#    Alice borrowed 'The Catcher in the Rye'.
#    Alice borrowed 'Python Crash Course'.
#    Bob borrowed 'To Kill a Mockingbird'.
#    ```
#    После этого количество копий соответствующих книг в библиотеке становится 0 (для тех, что взяты) и остаётся оригинальное значение для оставшихся.

# 5. **Вывод обновлённой информации:**  
#    – `display_customer_books(customer1)` покажет:
#      ```
#      Books borrowed by Alice:
#      Title: The Catcher in the Rye, Author: J.D. Salinger, Year: 1951, Quantity: 0
#      Title: Python Crash Course, Author: Eric Matthes, Year: 2015, Quantity: 0 Format: PDF
#      ```
#    – `display_all_books()` выведет:
#      ```
#      Books in the Library:
#      Title: The Catcher in the Rye, Author: J.D. Salinger, Year: 1951, Quantity: 0
#      Title: To Kill a Mockingbird, Author: Harper Lee, Year: 1960, Quantity: 0
#      Title: Python Crash Course, Author: Eric Matthes, Year: 2015, Quantity: 0 Format: PDF
#      Title: Dive into Python 3, Author: Mark Pilgrim, Year: 2009, Quantity: 1 Format: EPUB

print("Тесты:")
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
ebook1 = EBook("Python Crash Course", "Eric Matthes", 2015, "PDF")
ebook2 = EBook("Dive into Python 3", "Mark Pilgrim", 2009, "EPUB")
print(book1)
print(book2)
print(ebook1)
print(ebook2)
print()
customer1 = Customer("Alice")
customer2 = Customer("Bob")
print(customer1)
print(customer2)
print()
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
ebook1 = EBook("Python Crash Course", "Eric Matthes", 2015, "PDF")
ebook2 = EBook("Dive into Python 3", "Mark Pilgrim", 2009, "EPUB")
customer1 = Customer("Alice")
customer2 = Customer("Bob")
library_system = LibraryManagementSystem()
library_system.register_customer(customer1)
library_system.register_customer(customer2)
library_system.library.add_book(book1)
library_system.library.add_book(book2)
library_system.library.add_book(ebook1)
library_system.library.add_book(ebook2)
library_system.display_customer_books(customer1)
library_system.display_all_books()
print()
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
ebook1 = EBook("Python Crash Course", "Eric Matthes", 2015, "PDF")
ebook2 = EBook("Dive into Python 3", "Mark Pilgrim", 2009, "EPUB")
customer1 = Customer("Alice")
customer2 = Customer("Bob")
library_system = LibraryManagementSystem()
library_system.register_customer(customer1)
library_system.register_customer(customer2)
library_system.library.add_book(book1)
library_system.library.add_book(book2)
library_system.library.add_book(ebook1)
library_system.library.add_book(ebook2)
customer1.borrow_book(book1)
customer1.borrow_book(ebook1)
customer2.borrow_book(book2)
library_system.display_customer_books(customer1)
library_system.display_all_books()