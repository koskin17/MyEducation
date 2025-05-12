# Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords. 

# Each instance should have a name and a lastname attributes plus one more attribute for each of the keywords, if any.

# Examples:
# john = Employee("John Doe")
# mary = Employee("Mary Major", salary=120000)
# richard = Employee("Richard Roe", salary=110000, height=178)
# giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
# mary.lastname ➞ "Major"
# richard.height ➞ 178
# giancarlo.nationality ➞ "Italian"
# john.name ➞ "John"

# Задание:
# Создайте класс Employee, который принимает полное имя (full_name) в качестве аргумента, а также любой набор дополнительных параметров (один, несколько или вообще никаких).
# Каждый экземпляр класса Employee должен иметь два атрибута:
# - name — имя сотрудника
# - lastname — фамилия сотрудника
# Кроме того, если при создании объекта переданы дополнительные параметры (например, salary=120000, height=178), они должны быть добавлены в объект как отдельные атрибуты.


class Employee:
    def __init__(self, full_name, **kwargs):
        """Инициализация объекта Employee"""
        self.name, self.lastname = full_name.split(" ", 1)  # Разделяем имя и фамилию
        for key, value in kwargs.items():
            setattr(self, key, value)  # Создаём дополнительные атрибуты

# ✅ Примеры использования
john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

# 🔹 Проверяем атрибуты
print(john.name)        # "John"
print(mary.lastname)    # "Major"
print(richard.height)   # 178
print(giancarlo.nationality)  # "Italian"

# Разбор решения
# 1️⃣ Разделение full_name на name и lastname
# - split(" ", 1) разделяет имя и фамилию по первому пробелу.
# - Если имя состоит из двух слов ("John Doe"), self.name = "John", self.lastname = "Doe".
# 2️⃣ Передача дополнительных атрибутов через **kwargs
# - kwargs.items() содержит переданные параметры (salary, height, nationality и др.).
# - setattr(self, key, value) создаёт динамические атрибуты.

john = Employee('John Doe')
print(john.lastname)

mary = Employee('Mary Major', salary=120000)
print(mary.salary)

richard = Employee('Richard Roe', salary=110000, height=178)
print(richard.salary)
print(richard.height)

giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
print(giancarlo.name)
print(giancarlo.nationality)

peng = Employee('Peng Zhu', salary=500000, height=185, nationality='Chinese', subordinates=[i.lastname for i in (john, mary, richard, giancarlo)])
print(peng.subordinates)
