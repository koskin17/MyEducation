# Create a class hierarchy to represent different types of cars. Your hierarchy should include a base class Car and two subclasses - ElectricCar and HybridElectricCar.

# Each class should have attributes:
# model (car model)
# year (manufacturing year)
# color (color)
# speed (initial speed)

# In the ElectricCar class, add the attribute:
# battery_capacity (battery capacity)

# In the HybridElectricCar class, add the attribute:
# fuel_consumption (fuel consumption)

# Create a method accelerate that increases the speed of the car.
# Implement the magic method to allow comparison of cars based on their speed.

# Create a class CarFleet that contains a list of Car objects. Add a method to add car and methods to sort this list by the speed of the cars.
### **Перевод задачи на русский язык**  

### **Задача**  
# Создайте **иерархию классов**, представляющую **различные типы автомобилей**. Включите **базовый класс `Car`** и два подкласса – `ElectricCar` и `HybridElectricCar`.  

# ### **Атрибуты для всех классов:**  
# - `model` – модель автомобиля  
# - `year` – год выпуска  
# - `color` – цвет автомобиля  
# - `speed` – начальная скорость  

# ### **Дополнительные атрибуты:**  
# ✔ В классе **`ElectricCar`**:  
#   - `battery_capacity` – ёмкость аккумулятора  

# ✔ В классе **`HybridElectricCar`**:  
#   - `fuel_consumption` – расход топлива  

# ### **Методы:**  
# ✔ **Метод `accelerate()`** – увеличивает скорость автомобиля.  
# ✔ **Перегрузка магического метода** – позволяет **сравнивать автомобили по скорости**.  
# ✔ **Класс `CarFleet`** – содержит список объектов `Car`.  
#   - **Метод `add_car()`** – добавляет автомобиль в список.  
#   - **Метод `sort_by_speed()`** – сортирует автомобили по скорости.  

# ---

# ## **Код для решения задачи**
# class Car:
#     """Базовый класс автомобиля"""
#     def __init__(self, model, year, color, speed=0):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.speed = speed

#     def accelerate(self, amount):
#         """Увеличивает скорость автомобиля"""
#         self.speed += amount
#         print(f"{self.model} accelerates to {self.speed} km/h")

#     def __lt__(self, other):
#         """Позволяет сравнивать автомобили по скорости"""
#         return self.speed < other.speed

#     def __str__(self):
#         """Возвращает строковое представление автомобиля"""
#         return f"{self.model} ({self.year}) - {self.color}, Speed: {self.speed} km/h"


# class ElectricCar(Car):
#     """Класс электрического автомобиля"""
#     def __init__(self, model, year, color, battery_capacity, speed=0):
#         super().__init__(model, year, color, speed)
#         self.battery_capacity = battery_capacity

#     def __str__(self):
#         return super().__str__() + f", Battery: {self.battery_capacity} kWh"


# class HybridElectricCar(Car):
#     """Класс гибридного автомобиля"""
#     def __init__(self, model, year, color, fuel_consumption, speed=0):
#         super().__init__(model, year, color, speed)
#         self.fuel_consumption = fuel_consumption

#     def __str__(self):
#         return super().__str__() + f", Fuel Consumption: {self.fuel_consumption} L/100km"


# class CarFleet:
#     """Класс для управления автопарком"""
#     def __init__(self):
#         self.cars = []

#     def add_car(self, car):
#         """Добавляет автомобиль в автопарк"""
#         self.cars.append(car)
#         print(f"{car.model} added to the fleet.")

#     def sort_by_speed(self):
#         """Сортирует автомобили по скорости"""
#         self.cars.sort(reverse=True)  # Сортировка по убыванию скорости
#         print("Fleet sorted by speed.")

#     def display_fleet(self):
#         """Выводит список автомобилей в автопарке"""
#         for car in self.cars:
#             print(car)

# ## **🔎 Подробное объяснение кода**
# ### **🚗 `Car` – базовый класс**
# ✔ Содержит `model`, `year`, `color`, `speed`.  
# ✔ **Метод `accelerate(amount)`** увеличивает `speed`.  
# ✔ **Магический метод `__lt__()`** позволяет сравнивать автомобили **по скорости** (`<`).  
# ✔ `__str__()` – возвращает удобное представление объекта.

# ### **⚡ `ElectricCar` – наследуется от `Car`**
# ✔ Дополнительный атрибут **`battery_capacity`**.  
# ✔ **Переопределение `__str__()`** → добавляет ёмкость аккумулятора к строковому представлению.

# ### **⛽ `HybridElectricCar` – наследуется от `Car`**
# ✔ Дополнительный атрибут **`fuel_consumption`**.  
# ✔ **Переопределение `__str__()`** → добавляет расход топлива к строковому представлению.

# ### **🚙 `CarFleet` – управление автопарком**
# ✔ `cars` – список автомобилей.  
# ✔ `add_car(car)` – добавляет автомобиль в автопарк.  
# ✔ `sort_by_speed()` – сортирует автомобили по скорости (от быстрого к медленному).  
# ✔ `display_fleet()` – выводит список всех машин.

# ## **✅ Тестирование кода**
# # Создаём автомобили
# car1 = Car("Toyota Corolla", 2015, "White", 80)
# car2 = ElectricCar("Tesla Model S", 2022, "Red", 100, 120)
# car3 = HybridElectricCar("Toyota Prius", 2020, "Blue", 4.5, 90)

# # Проверяем ускорение
# car1.accelerate(10)  # Toyota Corolla accelerates to 90 km/h
# car2.accelerate(20)  # Tesla Model S accelerates to 140 km/h

# # Сравниваем автомобили по скорости
# print(car1 < car2)  # True (Toyota Corolla медленнее, чем Tesla Model S)

# # Создаём автопарк
# fleet = CarFleet()
# fleet.add_car(car1)
# fleet.add_car(car2)
# fleet.add_car(car3)

# # Выводим автопарк
# fleet.display_fleet()

# # Сортируем по скорости
# fleet.sort_by_speed()
# fleet.display_fleet()

# ### **🔎 Ожидаемый вывод**
# Toyota Corolla accelerates to 90 km/h
# Tesla Model S accelerates to 140 km/h
# True
# Toyota Corolla added to the fleet.
# Tesla Model S added to the fleet.
# Toyota Prius added to the fleet.
# Toyota Corolla (2015) - White, Speed: 90 km/h
# Tesla Model S (2022) - Red, Speed: 140 km/h, Battery: 100 kWh
# Toyota Prius (2020) - Blue, Speed: 90 km/h, Fuel Consumption: 4.5 L/100km
# Fleet sorted by speed.
# Tesla Model S (2022) - Red, Speed: 140 km/h, Battery: 100 kWh
# Toyota Corolla (2015) - White, Speed: 90 km/h
# Toyota Prius (2020) - Blue, Speed: 90 km/h, Fuel Consumption: 4.5 L/100km

# Ниже приведён исправленный и доработанный вариант кода, который соответствует тестам. Были внесены следующие изменения:

# 1. **Изменён порядок параметров** в конструкторах классов:
#    - Для базового класса `Car`: `model, year, color, speed`
#    - Для класса `ElectricCar`: после `color` сначала значение скорости, затем ­— «battery_capacity»
#    - Для класса `HybridElectricCar`: после `color` сначала значение скорости, затем — «fuel_consumption»
   
# 2. Метод `__str__` теперь возвращает строку в требуемом формате (например, для `Car`:  
#    `"Sedan - Year: 2022, Color: Blue, Speed: 120 km/h"`).

# 3. Реализованы методы `__repr__` для всех классов, чтобы при печати списка объектов выводилось требуемое представление (например,  
#    `Car('Sedan', 2022, 'Blue', 120)`).

# 4. В классе `ElectricCar` переопределён метод `accelerate`, чтобы выводить сообщение  
#    `"Electric car accelerates by {amount} km/h, current speed {self.speed}"`.

# 5. В классе `CarFleet` реализован метод-алиас `sort_cars_by_speed()` (как требуют тесты) для сортировки по скорости и добавлен метод `__repr__`, возвращающий список автомобилей в автопарке.

# Ниже приведён финальный код:

class Car:
    """Базовый класс автомобиля"""
    def __init__(self, model, year, color, speed=0):
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed

    def accelerate(self, amount):
        """Увеличивает скорость автомобиля и возвращает None"""
        self.speed += amount
        return None

    def __str__(self):
        """Пользовательское строковое представление"""
        return f"{self.model} - Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h"

    def __repr__(self):
        """Представление для отладки и тестирования"""
        return f"Car('{self.model}', {self.year}, '{self.color}', {self.speed})"

    def __lt__(self, other):
        """Сравнение автомобилей по скорости для сортировки"""
        return self.speed < other.speed


class ElectricCar(Car):
    """Класс электрического автомобиля"""
    def __init__(self, model, year, color, speed, battery_capacity):
        super().__init__(model, year, color, speed)
        self.battery_capacity = battery_capacity

    def accelerate(self, amount):
        """Увеличивает скорость и возвращает сообщение для электрического автомобиля"""
        self.speed += amount
        return f"Electric car accelerates by {amount} km/h, current speed {self.speed}"

    def __str__(self):
        return (f"{self.model} - Year: {self.year}, Color: {self.color}, "
                f"Speed: {self.speed} km/h, Battery Capacity: {self.battery_capacity} kWh")

    def __repr__(self):
        return f"ElectricCar('{self.model}', {self.year}, '{self.color}', {self.speed}, {self.battery_capacity})"


class HybridElectricCar(Car):
    """Класс гибридного автомобиля"""
    def __init__(self, model, year, color, speed, fuel_consumption):
        super().__init__(model, year, color, speed)
        self.fuel_consumption = fuel_consumption

    # Наследуем accelerate из Car (возвращает None)

    def __str__(self):
        return f"{self.model} - Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h"

    def __repr__(self):
        return f"HybridElectricCar('{self.model}', {self.year}, '{self.color}', {self.speed}, {self.fuel_consumption})"


class CarFleet:
    """Класс для управления автопарком"""
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        """Добавляет автомобиль в автопарк (без вывода сообщений)"""
        self.cars.append(car)

    def sort_by_speed(self):
        """Сортирует автомобили по скорости по месту (без возврата нового списка)"""
        self.cars.sort()

    def sort_cars_by_speed(self):
        """Возвращает новый список автомобилей, отсортированный по скорости (по возрастанию)"""
        return sorted(self.cars, key=lambda car: car.speed)

    def __repr__(self):
        return f"{self.cars}"

# Ниже приведён подробный разбор окончательного варианта кода, с пояснением каждого этапа и для чего он нужен.

# ## 1. Класс `Car`
# class Car:
#     """Базовый класс автомобиля"""
#     def __init__(self, model, year, color, speed=0):
#         self.model = model         # Модель автомобиля (например, "Sedan")
#         self.year = year           # Год выпуска (например, 2022)
#         self.color = color         # Цвет автомобиля (например, "Blue")
#         self.speed = speed         # Начальная скорость. Значение по умолчанию — 0

#     def accelerate(self, amount):
#         """Увеличивает скорость автомобиля и возвращает None"""
#         self.speed += amount       # Прибавляется заданное количество к текущей скорости
#         return None                # Функция возвращает None, как и требуется тестами

#     def __str__(self):
#         """
#         Возвращает строковое представление для пользователя.
#         Этот метод вызывается, когда мы делаем print(obj) или преобразуем объект в строку.
#         Формат: "Sedan - Year: 2022, Color: Blue, Speed: 120 km/h"
#         """
#         return f"{self.model} - Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h"

#     def __repr__(self):
#         """
#         Возвращает представление для отладки и тестирования.
#         __repr__ должен возвращать строку, которую можно использовать для воссоздания объекта.
#         Формат: Car('Sedan', 2022, 'Blue', 120)
#         """
#         return f"Car('{self.model}', {self.year}, '{self.color}', {self.speed})"

#     def __lt__(self, other):
#         """
#         Магический метод для поддержки оператора <.
#         Позволяет сравнивать два автомобиля по их скорости (self.speed < other.speed).
#         Это нужно для сортировки автомобилей.
#         """
#         return self.speed < other.speed
# ```

# **Пояснения к классу `Car`:**

# - **`__init__`**: Конструктор, который инициализирует атрибуты автомобиля. Он задаёт базовую информацию: модель, год, цвет и скорость. Это необходимо, чтобы у каждого автомобиля были собственные характеристики, по которым потом можно показывать информацию или сравнивать их.

# - **`accelerate`**: Метод, который увеличивает скорость автомобиля на определённое значение (`amount`). Он изменяет внутреннее состояние (`self.speed`) и возвращает `None`, как требуется в тестах. Мы не печатаем здесь сообщение, чтобы вернуть именно значение `None`.

# - **`__str__`**: Этот метод используется, когда требуется текстовое представление объекта для вывода пользователю (например, через `print()`). Он форматирует строку согласно требованиям тестов: модель, год, цвет и скорость выводятся в понятном виде.

# - **`__repr__`**: Возвращает строку, которая используется для отладки и тестирования (например, при выводе списка объектов). Именно этот метод позволяет тестам сравнивать вывод списка, чтобы он выглядел так, как:  
#   `Car('Sedan', 2022, 'Blue', 120)`

# - **`__lt__`**: Метод сравнения для оператора «<». Он позволяет сортировать объекты класса Car по скорости. Если скорость одного автомобиля меньше скорости другого, то результат сравнения будет `True`.

# ---

# ## 2. Класс `ElectricCar`

# ```python
# class ElectricCar(Car):
#     """Класс электрического автомобиля"""
#     def __init__(self, model, year, color, speed, battery_capacity):
#         super().__init__(model, year, color, speed)
#         self.battery_capacity = battery_capacity  # Дополнительный атрибут для электрических автомобилей

#     def accelerate(self, amount):
#         """
#         Переопределённый метод accelerate.
#         Увеличивает скорость и возвращает строку с сообщением,
#         что требуется в тестах для электрических автомобилей.
#         Например, "Electric car accelerates by 20 km/h, current speed 170"
#         """
#         self.speed += amount
#         return f"Electric car accelerates by {amount} km/h, current speed {self.speed}"

#     def __str__(self):
#         """
#         Возвращает строковое представление объекта для пользователя.
#         Добавляем информацию о бутылерии (Battery Capacity)
#         Формат: "Tesla - Year: 2023, Color: Black, Speed: 150 km/h, Battery Capacity: 60 kWh"
#         """
#         return (f"{self.model} - Year: {self.year}, Color: {self.color}, "
#                 f"Speed: {self.speed} km/h, Battery Capacity: {self.battery_capacity} kWh")

#     def __repr__(self):
#         """
#         Возвращает представление для отладки.
#         Формат: ElectricCar('Tesla', 2023, 'Black', 150, 60)
#         """
#         return f"ElectricCar('{self.model}', {self.year}, '{self.color}', {self.speed}, {self.battery_capacity})"
# ```

# **Пояснения к классу `ElectricCar`:**
# - **Наследование**: Класс наследует все атрибуты и методы от `Car`. Он использует `super().__init__()`, чтобы не дублировать код.
# - **Дополнительный атрибут `battery_capacity`**: Хранит информацию о ёмкости аккумулятора, специфичную для электрического автомобиля.
# - **Переопределение `accelerate`**: Метод меняет скорость и возвращает строку с сообщением, как требуется тестами для электрических машин, вместо простого печатания.
# - **`__str__`** и **`__repr__`**: Методы возвращают форматированный вывод, который включает информацию о ёмкости аккумулятора. Это необходимо, чтобы тесты получали именно требуемый формат.

# ## 3. Класс `HybridElectricCar`
# class HybridElectricCar(Car):
#     """Класс гибридного автомобиля"""
#     def __init__(self, model, year, color, speed, fuel_consumption):
#         super().__init__(model, year, color, speed)
#         self.fuel_consumption = fuel_consumption  # Расход топлива, специфичный для гибридного авто
#     # Для гибридного автомобиля метод accelerate остаётся базовым (наследуется от Car)
#     def __str__(self):
#         """
#         Строковое представление для пользователя.
#         Формат: "Toyota - Year: 2022, Color: Silver, Speed: 130 km/h"
#         В тестах не требуется выводить расход топлива.
#         """
#         return f"{self.model} - Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h"
#     def __repr__(self):
#         """
#         Представление для отладки.
#         Формат: HybridElectricCar('Toyota', 2022, 'Silver', 130, 0.05)
#         """
#         return f"HybridElectricCar('{self.model}', {self.year}, '{self.color}', {self.speed}, {self.fuel_consumption})"

# **Пояснения к классу `HybridElectricCar`:**
# - **Наследование и атрибут fuel_consumption**: Наследуем от Car все базовые атрибуты, а также добавляем расход топлива — специфическая характеристика для гибридных машин.
# - **Метод `accelerate`**: Не переопределяется, поэтому используется тот, который унаследован от Car — он увеличивает скорость и возвращает None, что удовлетворяет тестам.
# - **`__str__`**: При выводе пользователю не нужно показывать расход топлива, поэтому строка выведена без этой информации.
# - **`__repr__`**: Предоставляет полное представление объекта с расходом топлива, чтобы тесты, сравнивающие вывод списка объектов, прошли успешно.

# ## 4. Класс `CarFleet`
# class CarFleet:
#     """Класс для управления автопарком"""
#     def __init__(self):
#         self.cars = []  # Список автомобилей в автопарке

#     def add_car(self, car):
#         """
#         Метод добавляет автомобиль в автопарк.
#         Сообщения не выводятся, так как тесты ожидают чистое добавление.
#         """
#         self.cars.append(car)

#     def sort_by_speed(self):
#         """
#         Метод сортирует автомобили в автопарке «на месте» (в списке self.cars)
#         по возрастанию скорости.
#         """
#         self.cars.sort()

#     def sort_cars_by_speed(self):
#         """
#         Метод возвращает новый список автомобилей, отсортированных по скорости.
#         Используется функция sorted с ключом, зависящим от атрибута speed.
#         """
#         return sorted(self.cars, key=lambda car: car.speed)

#     def __repr__(self):
#         """
#         Возвращает строковое представление автопарка для отладки.
#         Формат: [Car(...), ElectricCar(...), HybridElectricCar(...)]
#         """
#         return f"{self.cars}"
    
# **Пояснения к классу `CarFleet`:**

# - **`__init__`**: Инициализирует автопарк как пустой список объектов.
# - **`add_car`**: Метод добавляет автомобиль в автопарк. Он не выводит никаких сообщений, чтобы соответствовать требованиям тестов: вывод списка автопарка должен производиться через `__repr__` (то есть просто выводится список объектов, а не сообщения о добавлении).
# - **`sort_by_speed`**: Сортирует список автомобилей внутри автопарка (изменяя self.cars). Это может быть полезно, если нужно изменить порядок само́го списка.
# - **`sort_cars_by_speed`**: Возвращает новый отсортированный список по скорости (с использованием встроенной функции `sorted`). Тесты ожидают именно этот метод.
# - **`__repr__`**: Формат вывода автопарка — список объектов, каждый из которых будет представлен по формату, заданному в методе `__repr__` соответствующего класса.

# ## Применение к тестам
# 1. **Тест ускорения**:  
#    При вызове методов `accelerate`:
#    - `car1.accelerate(10)` меняет скорость с 120 на 130 и возвращает `None`, что соответствует ожиданию.
#    - `electric_car1.accelerate(20)` меняет скорость с 150 на 170 и возвращает строку `"Electric car accelerates by 20 km/h, current speed 170"`.
#    - `hybrid_car1.accelerate(15)` меняет скорость с 130 на 145 и возвращает `None`.

# 2. **Тест вывода автопарка**:  
#    При вызове `print(car_fleet)` выводится строковое представление автопарка, которое вызывает метод `__repr__` и показывает список автомобилей с их текущими характеристиками:
#    ```
#    [Car('Sedan', 2022, 'Blue', 130), ElectricCar('Tesla', 2023, 'Black', 170, 60), HybridElectricCar('Toyota', 2022, 'Silver', 145, 0.05)]
#    ```
#    Это именно то, что ожидается по тестам.

# 3. **Тест сортировки**:  
#    `sort_cars_by_speed` возвращает отсортированный список, где сначала идёт автомобиль с наименьшей скоростью (Sedan), затем HybridElectricCar (Toyota), затем ElectricCar (Tesla). При выводе каждого объекта вызывается метод `__str__`, который даст требуемый формат:
#    - "Sedan - Year: 2022, Color: Blue, Speed: 130 km/h"
#    - "Toyota - Year: 2022, Color: Silver, Speed: 145 km/h"
#    - "Tesla - Year: 2023, Color: Black, Speed: 170 km/h, Battery Capacity: 60 kWh"

# ---

# ## Заключение

# - **Наследование и переопределение**:  
#   Подклассы `ElectricCar` и `HybridElectricCar` наследуют базовую функциональность класса `Car`, но при этом добавляют или переопределяют методы так, чтобы удовлетворять специфическим требованиям (например, формат сообщения при ускорении или представление объекта).

# - **Методы строкового представления** (__str__ и __repr__):  
#   Они используются для корректного вывода объектов в консоль — __str__ для общего вида, __repr__ для тестирования и отладки.

# - **Метод сортировки** (__lt__ in Car + sort_cars_by_speed):  
#   Это позволяет удобно сравнивать автомобили по их скорости, что востребовано для теста сортировки автопарка.

# - **Разделение логики для автопарка**:  
#   Класс `CarFleet` аккумулирует автомобили, предоставляет методы для их добавления и сортировки, а также корректный вывод в виде списка.

# Каждый фрагмент кода написан с учётом требований тестов, поэтому итоговый вариант соответствует всем ожидаемым результатам. Если останутся вопросы или потребуется доработка деталей — обращайтесь!

# ### Примеры использования и проверка тестов

car1 = Car("Sedan", 2022, "Blue", 120)
print(car1)
print()

electric_car1 = ElectricCar("Tesla", 2023, "Black", 150, 60)
print(electric_car1)
print()

	
hybrid_car1 = HybridElectricCar("Toyota", 2022, "Silver", 130, 0.05)
print(hybrid_car1)
print()

car1 = Car("Sedan", 2022, "Blue", 120)
electric_car1 = ElectricCar("Tesla", 2023, "Black", 150, 60)
hybrid_car1 = HybridElectricCar("Toyota", 2022, "Silver", 130, 0.05)
print([car1, electric_car1, hybrid_car1])
print()

	
car1 = Car("Sedan", 2022, "Blue", 120)
electric_car1 = ElectricCar("Tesla", 2023, "Black", 150, 60)
hybrid_car1 = HybridElectricCar("Toyota", 2022, "Silver", 130, 0.05)

car_fleet = CarFleet()
car_fleet.add_car(car1)
car_fleet.add_car(electric_car1)
car_fleet.add_car(hybrid_car1)

print(car_fleet)
print()

car1 = Car("Sedan", 2022, "Blue", 120)
electric_car1 = ElectricCar("Tesla", 2023, "Black", 150, 60)
hybrid_car1 = HybridElectricCar("Toyota", 2022, "Silver", 130, 0.05)
car_fleet = CarFleet()
car_fleet.add_car(car1)
car_fleet.add_car(electric_car1)
car_fleet.add_car(hybrid_car1)

accelerate_car1 = car1.accelerate(10)
accelerate_electric_car1 = electric_car1.accelerate(20)
accelerate_hybrid_car1 = hybrid_car1.accelerate(15)

print(accelerate_car1)
print(accelerate_electric_car1)
print(accelerate_hybrid_car1)
print(car_fleet)
print()

car1 = Car("Sedan", 2022, "Blue", 120)
electric_car1 = ElectricCar("Tesla", 2023, "Black", 150, 60)
hybrid_car1 = HybridElectricCar("Toyota", 2022, "Silver", 130, 0.05)
car_fleet = CarFleet()
car_fleet.add_car(car1)
car_fleet.add_car(electric_car1)
car_fleet.add_car(hybrid_car1)
car1.accelerate(10)
electric_car1.accelerate(20)
hybrid_car1.accelerate(15)

sorted_cars = car_fleet.sort_cars_by_speed()
for car in sorted_cars:
    print(car)