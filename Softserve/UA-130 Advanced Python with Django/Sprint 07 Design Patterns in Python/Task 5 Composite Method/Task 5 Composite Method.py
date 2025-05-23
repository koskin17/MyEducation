# Imagine we are studying an organizational structure which consists of General Managers, Managers, and Developers. A General Manager may have many Managers working under him and a Manager may have many developers under him. Suppose, you have to determine the total salary of all the employees. 

# One of the best solutions to the above-described problem is using Composite Method by working with a common interface that declares a method for calculating the total salary.

# Note. 

# We attempt to make an organizational hierarchy with sub-organization,
# which may have subsequent sub-organizations, such as:
# GeneralManager                                   [Composite]
#       Manager1                                   [Composite]
#               Developer11                        [Leaf]
#               Developer12                        [Leaf]
#       Manager2                                   [Composite]
#               Developer21                        [Leaf]
#               Developer22                        [Leaf]

# class LeafElement: 
  
#     def __init__(self, *args): 
  
#         ''''Takes the first positional argument and assigns to member variable "position".'''
         
  
#     def showDetails(self): 
  
#         '''Prints the position of the child element.'''
        
  
  
# class CompositeElement: 
  
#     def __init__(self, *args): 
  
#         '''Takes the first positional argument and assigns to member 
#          variable "position". Initializes a list of children elements.'''
        
  
#     def add(self, child): 
  
#         '''Adds the supplied child element to the list of children 
#          elements "children".'''
        
  
#     def remove(self, child): 
  
#         '''Removes the supplied child element from the list of 
#         children elements "children".'''
        
  
#     def showDetails(self): 
  
#         '''Prints the details of the component element first. Then, 
#         iterates over each of its children, prints their details by 
#         calling their showDetails() method.'''

## 🔵 Перевод задачи на русский

# > Представим, что мы изучаем организационную структуру, которая состоит из:
# * **Генеральных директоров** (*General Managers*),
# * **Менеджеров** (*Managers*),
# * **Разработчиков** (*Developers*).

# 🔸 Один **генеральный директор** может иметь под собой **несколько менеджеров**.
# 🔸 Каждый **менеджер** может иметь под собой **нескольких разработчиков**.

# **Цель**: рассчитать общую зарплату всех сотрудников в этой иерархии.

# 💡 Для этого **наилучшим решением будет использование паттерна Composite**, который позволяет обращаться к одиночным объектам и группам одинаково, через **общий интерфейс**.

## 🧩 Зачем нужен Composite-паттерн здесь?
# * Разработчик (Developer) — **листовой элемент** (не содержит других сотрудников);
# * Менеджер и Генеральный менеджер — **составные элементы** (могут содержать других сотрудников).

# **Composite** позволяет:
# * обращаться к элементу или группе единообразно;
# * строить иерархию как дерево;
# * **не думать, кто именно перед тобой — "один" или "группа"**.

## 🏗 Структура решения
# Мы будем использовать 2 класса:
# * `LeafElement` — для разработчиков;
# * `CompositeElement` — для менеджеров и генерального директора.

# Все сотрудники будут иметь:
# * `position` — должность;
# * `salary` — зарплату;
# * `showDetails()` — вывод информации;
# * `get_salary()` — получение своей/групповой зарплаты.

## ✅ Пошаговое решение задачи

### 🔹 1. Класс `LeafElement`
# Это **конечный сотрудник**, у которого:
# * нет подчинённых;
# * есть только имя, должность и зарплата;
# * может показать себя (`showDetails`) и отдать зарплату (`get_salary`).

### 🔹 2. Класс `CompositeElement`
# Это **сотрудник с подчинёнными**:
# * тоже имеет имя, должность и зарплату;
# * может добавлять/удалять сотрудников;
# * выводит себя и всех своих подчинённых;
# * считает свою зарплату + зарплату всех подчинённых.

## ✅ Полный код с комментариями
# class LeafElement:
#     # def __init__(self, name, position, salary):
#     def __init__(self, *args):
#         """
#         Creating an employee without subordinates:
#             :param name: Employee name;
#             :param position: Position;
#             :param salary: Salary.
#         """
#         # self.name = name
#         self.position = position
#         # self.salary = salary

#     def showDetails(self):
#         """ Information about employee """
#         print(f"{self.position}: {self.name}, Salary: {self.salary}")

#     def get_salary(self):
#         """ Salary of employee """
#         return self.salary


# class CompositeElement:
#     def __init__(self, name, position, salary):
#         """
#         Cretaing employee with subordinates:
#             :param name: Name of employee;
#             :param position: Position.
#             :param salary: Salary.
#         """
#         self.name = name
#         self.position = position
#         self.salary = salary
#         self.children = []  # List of subordinates

#     def add(self, child):
#         """ Add a subordinate """
#         self.children.append(child)

#     def remove(self, child):
#         """ Remove a subordinate """
#         self.children.remove(child)

#     def showDetails(self):
#         """ Display all information + information about all subordinates """
#         print(f"{self.position}: {self.name}, Salary: {self.salary}")
#         for child in self.children:
#             child.showDetails()

#     def get_salary(self):
#         """ Salary of employee + salary of all subordinates """
#         total = self.salary
#         for child in self.children:
#             total += child.get_salary()
#         return total

# ## 🧪 Пример использования
# if __name__ == "__main__":
#     # Создание сотрудников
#     dev1 = LeafElement("Alice", "Developer11", 5000)
#     dev2 = LeafElement("Bob", "Developer12", 4800)
#     dev3 = LeafElement("Charlie", "Developer", 4700)
#     dev4 = LeafElement("Diana", "Developer", 4900)

#     # Менеджеры
#     manager1 = CompositeElement("Eva", "Manager1", 8000)
#     manager2 = CompositeElement("Frank", "Manager2", 8200)
#     # Добавляем разработчиков менеджерам
#     manager1.add(dev1)
#     manager1.add(dev2)
#     manager2.add(dev3)
#     manager2.add(dev4)
    
#     # Генеральный директор
#     general_manager = CompositeElement("Grace", "General Manager", 15000)

#     # Добавляем менеджеров директору
#     general_manager.add(manager1)
#     general_manager.add(manager2)

#     # Покажем структуру
#     print("=== Organization Structure ===")
#     general_manager.showDetails()

#     # Общая зарплата
#     print("\nTotal Salary of all employees:", general_manager.get_salary())

# КОД ДЛЯ ЗАДАНИЯ
class LeafElement:
    def __init__(self, *args):
        """
        Creating an employee without subordinates:
            :param name: Employee name;
            :param position: Position;
            :param salary: Salary.
        """
        self.position = args[0]

    def showDetails(self, indent = 0):
        """ Information about employee """
        print("\t" * indent + f"{self.position}")

    def get_salary(self):
        """ Salary of employee """
        return self.salary

class CompositeElement:
    def __init__(self, *args):
        """
        Cretaing employee with subordinates:
            :param name: Name of employee;
            :param position: Position.
            :param salary: Salary.
        """
        self.position = args[0]
        self.children = []  # List of subordinates

    def add(self, child):
        """ Add a subordinate """
        self.children.append(child)

    def remove(self, child):
        """ Remove a subordinate """
        self.children.remove(child)

    def showDetails(self, indent = 0):
        """ Display all information + information about all subordinates """
        print("\t" * indent + f"{self.position}")
        for child in self.children:
            child.showDetails(indent + 1)

    def get_salary(self):
        """ Salary of employee + salary of all subordinates """
        total = self.salary
        for child in self.children:
            total += child.get_salary()
        return total
    
if __name__ == "__main__":
    # Тесты из задания
    print()
    print('Tests from task:')
    topLevelMenu = CompositeElement("GeneralManager")
    subMenuItem1 = CompositeElement("Manager1")
    subMenuItem2 = CompositeElement("Manager2")
    subMenuItem11 = LeafElement("Developer11")
    subMenuItem12 = LeafElement("Developer12")
    subMenuItem21 = LeafElement("Developer21")
    subMenuItem22 = LeafElement("Developer22")
    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem2.add(subMenuItem22)
    subMenuItem2.add(subMenuItem22)
    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    topLevelMenu.showDetails()

## 💡 Почему так устроено?
# | Что                                                   | Почему                                                         |
# | ------------------------------------------------------| -------------------------------------------------------------- |
# | `LeafElement` и `CompositeElement` имеют одинаковые   | Чтобы работать с ними одинаково, как требует паттерн Composite |
# | методы                                                |  |
# | У `CompositeElement` есть список `children`           | Для хранения подчинённых                                       |
# | Метод `get_salary()` вызывает сам себя на подчинённых | Это **рекурсия** по иерархии сотрудников                       |

# Хочешь — могу добавить вывод дерева в виде отступов (`General Manager → Manager → Developer`) или сделать сохранение структуры в JSON/XML.

# Чтобы **вывести организационную структуру в виде дерева с отступами**, мы добавим параметр `indent` в метод `showDetails()` — он будет показывать **глубину текущего элемента в иерархии**.

## 🔧 Обновим методы `showDetails()`:

### ✅ Обновлённый `LeafElement.showDetails()`:
# def showDetails(self, indent=0):
#     print("    " * indent + f"{self.position}: {self.name}, Salary: {self.salary}")

# ### ✅ Обновлённый `CompositeElement.showDetails()`:
# def showDetails(self, indent=0):
#     print("    " * indent + f"{self.position}: {self.name}, Salary: {self.salary}")
#     for child in self.children:
#         child.showDetails(indent + 1)

# ## ✅ Обновлённый пример использования
# if __name__ == "__main__":
#     dev1 = LeafElement("Alice", "Developer", 5000)
#     dev2 = LeafElement("Bob", "Developer", 4800)
#     dev3 = LeafElement("Charlie", "Developer", 4700)
#     dev4 = LeafElement("Diana", "Developer", 4900)

#     manager1 = CompositeElement("Eva", "Manager", 8000)
#     manager2 = CompositeElement("Frank", "Manager", 8200)

#     manager1.add(dev1)
#     manager1.add(dev2)
#     manager2.add(dev3)
#     manager2.add(dev4)

#     general_manager = CompositeElement("Grace", "General Manager", 15000)
#     general_manager.add(manager1)
#     general_manager.add(manager2)

#     print("=== Organization Structure ===")
#     general_manager.showDetails()

#     print("\nTotal Salary of all employees:", general_manager.get_salary())

# ## ✅ Результат вывода
# === Organization Structure ===
# General Manager: Grace, Salary: 15000
#     Manager: Eva, Salary: 8000
#         Developer: Alice, Salary: 5000
#         Developer: Bob, Salary: 4800
#     Manager: Frank, Salary: 8200
#         Developer: Charlie, Salary: 4700
#         Developer: Diana, Salary: 4900

# Total Salary of all employees: 50400

# ## 📌 Пояснение

# * `"    " * indent` добавляет отступы: `0` → нет отступа, `1` → 4 пробела, `2` → 8 пробелов и т.д.
# * Мы передаём `indent + 1` каждому подчинённому, чтобы он выводился **глубже**.
# * Структура теперь читается как **иерархическое дерево** — от директора до разработчика.

# Хочешь — можно добавить цвет, номера уровней или визуальные символы (`├──`, `└──`).

# Отличный вопрос — и нет, тебе **не нужно существенно менять весь код**, чтобы получать зарплату **только конкретного сотрудника**.

# Ты уже можешь это сделать, потому что каждый объект (сотрудник) — это **отдельный экземпляр класса**, и у каждого есть своё поле `salary`.

## ✅ Пример: как получить зарплату конкретного сотрудника
# dev1 = LeafElement("Alice", "Developer", 5000)
# print("Зарплата Alice:", dev1.salary)  # 👉 напрямую

# manager1 = CompositeElement("Bob", "Manager", 8000)
# print("Зарплата менеджера Bob:", manager1.salary)  # 👉 напрямую

# Или, если хочешь использовать метод `get_salary()` и **не учитывать подчинённых**, то достаточно добавить **вот такой метод** в оба класса:

## 🔄 Альтернатива: сделать отдельный метод `get_own_salary()`

### В `LeafElement`:
# def get_own_salary(self):
#     return self.salary

### В `CompositeElement`:
# def get_own_salary(self):
    # return self.salary

# 📌 Тогда ты сможешь вызывать:
# print("Только зарплата менеджера Bob:", manager1.get_own_salary())
# print("Только зарплата Alice:", dev1.get_own_salary())

## 🔁 А если хочешь **и общее, и личное** — ты уже всё это умеешь
# * `get_salary()` — зарплата с учётом всех подчинённых
# * `salary` или `get_own_salary()` — только его личная

## 🧠 Почему это гибко

# Это и есть сила объектно-ориентированного подхода:
# * каждый объект — как самостоятельная "ячейка"
# * ты можешь обращаться к нему напрямую или в составе иерархии
# * не нужно переписывать архитектуру

# Ты абсолютно верно заметил: в задании `__init__` действительно использует `*args`, а я в решении предложил более **явный и читаемый способ** — с `name`, `position`, `salary`. Но давай теперь разберёмся, **что делает `*args`**, **можно ли его использовать** и **в чём плюсы и минусы**.

## ✅ Что такое `*args`?
# Когда ты пишешь:
# def __init__(self, *args):
# Это означает: **метод может принять любое количество позиционных аргументов**, и все они будут **собраны в кортеж `args`**.
# Пример:
# obj = LeafElement("Alice", "Developer", 5000)
# Внутри метода `__init__` ты получишь:
# args = ("Alice", "Developer", 5000)
## ✅ Как работать с `*args` внутри конструктора?
# Ты можешь **распаковать их вручную**, например:
# def __init__(self, *args):
#     self.name = args[0]
#     self.position = args[1]
#     self.salary = args[2]
# И всё будет работать так же, как в "красивом" варианте `__init__(self, name, position, salary)`.
## 🔍 Так в чём разница?

# | Вариант                        | Плюсы                                                             | Минусы                                             |
# | -------------------------------| ------------------------------------------------------------------| -------------------------------------------------- |
# | `__init__(self, *args)`        | ✅ Гибкость — можно передавать любое количество аргументов       | ❌ Нельзя понять по сигнатуре, что именно ожидается |
# | `__init__(self, name,
#               position, salary)` | ✅ Ясность — код читается проще, IDE подсказывает названия аргументов | ❌ Нужно передавать аргументы строго по именам      |

## 🔧 Когда стоит использовать `*args`?
# * Когда ты **не знаешь заранее**, сколько будет аргументов.
# * Или когда ты **делаешь базу под универсальный шаблон** (например, парсинг из файла).
# * Или когда это **явно указано в задании**, как в нашем случае — просто как тренировка работы с `*args`.

## ✅ Как выглядел бы `LeafElement` с `*args`?
# class LeafElement:
#     def __init__(self, *args):
#         self.name = args[0]
#         self.position = args[1]
#         self.salary = args[2]

#     def get_salary(self):
#         return self.salary

#     def showDetails(self, indent=0):
#         print("    " * indent + f"{self.position}: {self.name}, Salary: {self.salary}")
# И ты всё равно сможешь создавать объекты так:
# dev = LeafElement("Alice", "Developer", 5000)

## 📌 Вывод
# * ✅ Да, ты **можешь использовать `*args`** — особенно если так указано в задании.
# * 🔧 Но для **реального кода в команде** обычно предпочитают явные параметры — это читаемо, безопасно и удобно для автодополнения в IDE.
