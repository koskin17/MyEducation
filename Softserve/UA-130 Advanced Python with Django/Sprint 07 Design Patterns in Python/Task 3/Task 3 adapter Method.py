# Imagine you are creating an application that shows the data about all different types of vehicles present. It takes the data from APIs of different vehicle organizations in XML format and then displays the information.
# But suppose at some time you want to upgrade your application with a Machine Learning algorithms that work beautifully on the data and fetch the important data only. But there is a problem, it takes data in JSON format only.
# It will be a really poor approach to make changes in Machine Learning Algorithm so that it will take data in XML format.

# For solving the problem we defined above, you can use Adapter Method that helps by creating an Adapter object.
# To use an adapter in your code:

# Client should make a request to the adapter by calling a method on it using the target interface.
# Using the Adaptee interface, the Adapter should translate that request on the adaptee.
# Result of the call is received the client and he/she is unaware of the presence of the Adapter’s presence.
# Class diagram for the Adapter method:
    
# Заготовка кода:
# class MotorCycle: 
  
#     """Class for MotorCycle"""
  
#     def __init__(self): 
#         self.name = "MotorCycle"
  
#     def TwoWheeler(self): 
#         return "TwoWheeler"
  
# class Truck: 
 
# class Car:    
  
# class Adapter: 
#     """ 
#     Adapts an object by replacing methods. 
#     Usage: 
#     motorCycle = MotorCycle() 
#     motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler) 
#     """
  
#     def __init__(self, obj, **adapted_methods): 
#         """We set the adapted methods in the object's dict"""
        
  
#     def __getattr__(self, attr): 
#         """All non-adapted calls are passed to the object"""
        
  
#     def original_dict(self): 
#         """Print original object dict"""

## ✅ **1. Перевод задачи на русский**
# > Представь, что ты создаёшь приложение, которое отображает данные о разных типах транспортных средств. Эти данные приходят из разных организаций в формате **XML**.
# > Со временем ты хочешь улучшить приложение, добавив **машинное обучение**. Но есть проблема — алгоритмы ML работают только с **JSON**, а не с XML.
# > ❌ Плохая идея — переделывать всю ML-систему, чтобы она принимала XML.
# 🔧 Вместо этого мы используем **паттерн “Adapter”**:
# * Он будет **преобразовывать XML в JSON**,
# * ML-модуль **не узнает**, что под капотом работает “переводчик”.

## ✅ **2. Что за заготовка и зачем она нужна**
# Здесь у нас:
# * Классы `MotorCycle`, `Truck`, `Car` — представляют разные транспортные средства.
# * Каждый имеет свои уникальные методы: например, `MotorCycle.TwoWheeler()`.

# ❗ Проблема: у этих классов **нет общего интерфейса**. ML-модуль хочет видеть `wheels()` или `get_data()`, но такого метода **нет**.

### 💡 Как решить:
# Создаём класс **`Adapter`**, который:
# * Оборачивает объект (например, `MotorCycle`);
# * Подменяет/переименовывает методы (например, `TwoWheeler → wheels`);
# * Даёт единый интерфейс: теперь можно делать `obj.wheels()` независимо от того, `Car` это или `Truck`.

## ✅ **3. Подробное объяснение и шаги решения**
### 🛠 Классы-исходники
# class MotorCycle:
#     def __init__(self):
#         self.name = "MotorCycle"
#     def TwoWheeler(self):
#         return "TwoWheeler"

# # Тоже самое будет и для других:

# class Truck:
#     def __init__(self):
#         self.name = "Truck"
#     def EightWheeler(self):
#         return "EightWheeler"

# class Car:
#     def __init__(self):
#         self.name = "Car"
#     def FourWheeler(self):
#         return "FourWheeler"

### 🧩 Зачем нужен `Adapter`
# Если ты хочешь, чтобы все объекты имели метод `wheels()`, а у них он называется по-разному (`TwoWheeler`, `FourWheeler`...), ты:
# * **не можешь изменить эти классы** (они приходят откуда-то, например, из API);
# * **не хочешь писать “if obj is Truck: obj.EightWheeler()” — это нарушает OOP.**

# → 🔥 Здесь помогает **Adapter**:
# * Он берёт объект
# * Подменяет (или адаптирует) его методы
# * Даёт клиенту единый интерфейс.

### 📦 Как устроен `Adapter`
# class Adapter:
#     def __init__(self, obj, **adapted_methods):
#         self._object = obj
#         self.__dict__.update(adapted_methods)

# * `obj` — оригинальный объект, который мы адаптируем.
# * `**adapted_methods` — словарь типа `{'wheels': obj.FourWheeler}`

# Метод `__getattr__()` нужен, чтобы если мы обращаемся к другим методам (неподменённым) — они всё равно работали:
# def __getattr__(self, attr):
#     return getattr(self._object, attr)

# `original_dict()` — просто чтобы увидеть, что внутри:
# def original_dict(self):
#     return self._object.__dict__

## ✅ **4. Полный рабочий код с примером**
# Classes for vehicle types
class MotorCycle:
    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"

class Truck:
    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"

class Car:
    def __init__(self):
        self.name = "Car"

    def FourWheeler(self):
        return "FourWheeler"

# Adapter
class Adapter:
    """
    Адаптирует объект: подменяет его методы, создавая единый интерфейс
    Пример: Adapter(obj, wheels=obj.TwoWheeler)
    """

    def __init__(self, obj, **adapted_methods):
        self._object = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self._object, attr)

    def original_dict(self):
        return self._object.__dict__

# Клиентский код
if __name__ == "__main__":
    # Оригинальные объекты
    objects = [
        MotorCycle(),
        Truck(),
        Car()
    ]

    # Адаптируем к единому интерфейсу
    adapted_objects = [
        Adapter(obj, wheels=getattr(obj, obj.__class__.__dict__[list(obj.__class__.__dict__.keys())[1]].__name__))  # немного динамики
        if hasattr(obj, 'TwoWheeler') else
        Adapter(obj, wheels=obj.FourWheeler) if hasattr(obj, 'FourWheeler') else
        Adapter(obj, wheels=obj.EightWheeler)
        for obj in objects
    ]

    # Теперь все объекты поддерживают метод wheels()
    for vehicle in adapted_objects:
        print(f"{vehicle.name} has {vehicle.wheels()}")

## 🔍 Что выведет:
# MotorCycle has TwoWheeler
# Truck has EightWheeler
# Car has FourWheeler

## 📌 Вывод
# * **Adapter** позволяет использовать **старые классы** в **новой системе**, не переписывая их.
# * Ты **создаёшь новый интерфейс**, под который удобно писать ML-модели, UI, логику и т.д.
# * Программа становится **гибкой, расширяемой и чистой** с точки зрения OOP.

# Теперь давай разберём **весь код по строчкам**, **предельно простыми словами**, без сложных терминов. Буду объяснять так, как будто ты впервые видишь Python 😊

## 📦 Часть 1: Классы транспортных средств
# class MotorCycle:
#     def __init__(self):
#         self.name = "MotorCycle"

#     def TwoWheeler(self):
#         return "TwoWheeler"

### Что происходит:
# * `class MotorCycle:` — мы создаём **класс**, то есть **шаблон** для мотоциклов.
# * `__init__()` — это **конструктор**, он вызывается **сразу, когда создаём объект**.
# * `self.name = "MotorCycle"` — объекту присваивается имя `"MotorCycle"`.
# * `def TwoWheeler(self):` — метод, который возвращает строку `"TwoWheeler"` — то есть **этот транспорт двухколёсный**.

# Аналогично с `Truck` и `Car`:
# class Truck:
#     def __init__(self):
#         self.name = "Truck"
#     def EightWheeler(self):
#         return "EightWheeler"

# class Car:
#     def __init__(self):
#         self.name = "Car"
#     def FourWheeler(self):
#         return "FourWheeler"

## 🧩 Часть 2: Класс `Adapter`
# class Adapter:
#     def __init__(self, obj, **adapted_methods):
#         self._object = obj
#         self.__dict__.update(adapted_methods)

### Объяснение:
# * `class Adapter:` — мы создаём **обёртку** вокруг любого объекта, чтобы он выглядел одинаково.
# * `__init__()` — конструктор, принимает:
#   * `obj` — это **любой объект**, например, `Car()`.
#   * `**adapted_methods` — это **переименованные методы**, например:
#     `wheels=obj.FourWheeler`.
# * `self._object = obj` — мы сохраняем объект внутри адаптера.
# * `self.__dict__.update(adapted_methods)` — это **фокус**:
#   * `__dict__` — это **все свойства и методы объекта**;
#   * `update(...)` — добавляет новые атрибуты.
#   * То есть: мы как бы вставляем метод `wheels` внутрь адаптера, и теперь можно обращаться к нему.

    # def __getattr__(self, attr):
    #     return getattr(self._object, attr)
# * Этот метод срабатывает, если мы **обращаемся к методу, которого нет у адаптера**.
# * Он тогда пробует взять его у **оригинального объекта**.
# * Пример:

#   * `adapter.name` → если нет `name` у адаптера, берёт у `Car()`.
    # def original_dict(self):
    #     return self._object.__dict__

# * Просто показывает, **что хранится внутри оригинального объекта**.
# * Это для отладки, не обязательно.

## 🚀 Часть 3: Клиентский код
# if __name__ == "__main__":

# * Это специальная строчка, которая говорит:

#   > "Если мы запускаем файл напрямую — начни выполнять следующий код".

### Создаём объекты:
    # objects = [
    #     MotorCycle(),
    #     Truck(),
    #     Car()
    # ]
# * Мы создали **список** из трёх объектов: мотоцикл, грузовик, машина.

### Адаптируем их:
    # adapted_objects = [
    #     Adapter(obj, wheels=obj.TwoWheeler) if hasattr(obj, 'TwoWheeler') else
    #     Adapter(obj, wheels=obj.FourWheeler) if hasattr(obj, 'FourWheeler') else
    #     Adapter(obj, wheels=obj.EightWheeler)
    #     for obj in objects
    # ]

# Объясняю пошагово:
# * Мы проходим по каждому объекту `obj` в списке `objects`.
# * `hasattr(obj, 'TwoWheeler')` — проверяет, есть ли у объекта метод `TwoWheeler`.
# * Если есть:
#   Adapter(obj, wheels=obj.TwoWheeler)
#   — создаёт адаптер, который называет метод `TwoWheeler()` как `wheels()`.
# * И так далее: проверка `FourWheeler`, потом `EightWheeler`.

# В результате все объекты **получают метод `wheels()`**, и теперь ML-модель может спокойно вызывать:
# vehicle.wheels()
# независимо от типа транспорта!

### Выводим результат
    # for vehicle in adapted_objects:
    #     print(f"{vehicle.name} has {vehicle.wheels()}")
# * Пробегаем по каждому адаптированному объекту.
# * `vehicle.name` — имя, например `"Car"`.
# * `vehicle.wheels()` — вернёт, например, `"FourWheeler"`.

## 📋 Вывод программы:
# MotorCycle has TwoWheeler
# Truck has EightWheeler
# Car has FourWheeler

## 💡 ИТОГ
# | Элемент                | Объяснение                                                    |
# | ---------------------- | ------------------------------------------------------------- |
# | `Adapter`              | Оборачивает объект и даёт ему “универсальные” методы          |
# | `__dict__.update(...)` | Добавляет новые методы прямо в объект                         |
# | `__getattr__`          | Позволяет использовать старые методы                          |
# | `hasattr`              | Проверка: есть ли такой метод у объекта                       |
# | `wheels=`              | Мы вручную указываем: какой метод будет называться `wheels()` |

