# Define a class Employee. In the class Employee implement the instance attributes as firstname, lastname and salary.

# Create the static method from_string() which parses a string containing these attributes and assigns them to the correct properties. Properties will be separated by a dash.

# Examples:
# emp1 = Employee("Mary", "Sue", 60000)
# emp2 = Employee.from_string("John-Smith-55000")
# emp1.firstname ➞ "Mary"
# emp1.salary ➞ 60000
# emp2.firstname ➞ "John"

class Employee:
    def __init__(self, firstname, lastname, salary):
        """Инициализация экземпляра класса Employee"""
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @staticmethod
    def from_string(emp_string):
        """Статический метод для создания объекта Employee из строки"""
        firstname, lastname, salary = emp_string.split("-")  # Разбиваем строку по '-'
        return Employee(firstname, lastname, int(salary))  # Создаём объект и возвращаем его


# Примеры использования:
emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

# Проверяем атрибуты
print(emp1.firstname)  # Mary
print(emp1.salary)     # 60000
print(emp2.firstname)  # John
print('Конец проверки атрибутов')
print()

# Пошаговое объяснение работы кода:
# 1. Определение класса Employee
# - Класс Employee представляет сотрудников, у которых есть имя (firstname), фамилия (lastname) и зарплата (salary).
# - Определён метод __init__, который инициализирует объект при создании и заполняет атрибуты на основе переданных данных.
# 2. Определение статического метода from_string
# - from_string принимает строку в формате "имя-фамилия-зарплата" и создаёт объект Employee из неё.
# - Внутри метода:
# - split("-") разделяет строку по символу -, получая список ["John", "Smith", "55000"].
# - Затем переводим зарплату в int (так как она приходит в виде строки).
# - Возвращаем новый объект Employee с этими данными.
# 3. Использование класса
# - Создаём emp1 обычным способом:
# emp1 = Employee("Mary", "Sue", 60000)
# - Создаём emp2 через from_string:
# emp2 = Employee.from_string("John-Smith-55000")
# - Проверяем значения атрибутов (emp2.firstname == "John" — всё работает! ✅)
# ⚡ Почему @staticmethod?
# - Статический метод не требует self и не использует атрибуты класса напрямую.
# - Он просто выполняет функцию, относящуюся к классу (парсинг строки) без доступа к конкретному объекту.

emp1 = Employee("Mary", "Sue", 60000)
print(emp1.firstname)
print(emp1.lastname)
print(emp1.salary)
print(isinstance(emp1.salary, int))
print('Конец первых тестов')
print()
# Mary
# Sue
# 60000
# True
# Mary
# Sue
# 60000
# True

emp2 = Employee.from_string("John-Smith-55000")
print(emp2.firstname)
print(emp2.lastname)
print(emp2.salary)
print(isinstance(emp2.salary, int))
# John
# Smith
# 55000
# True
# John
# Smith
# 55000
# True
print('Конец вторых тестов')
print()

emp3 = Employee.from_string("Susan-Walker-70000")
print(emp3.firstname)
print(emp3.lastname)
print(emp3.salary)
print('Конец третьих тестов')
print()

emp4 = Employee.from_string("Michael-Ferry-90000")
print(emp4.firstname)
print(emp4.lastname)
print(emp4.salary)
print('Конец четвёртых тестов')
print()

emp5 = Employee("Graham", "Derrell", 55000)
print(emp5.firstname)
print(emp5.lastname)
print(emp5.salary)
print('Конец пятых тестов')
print()

import inspect
print(isinstance(inspect.getattr_static(Employee, "from_string"), staticmethod))