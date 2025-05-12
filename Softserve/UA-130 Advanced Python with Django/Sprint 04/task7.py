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
class Car:
    """Базовый класс автомобиля"""
    def __init__(self, model, year, color, speed=0):
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed

    def accelerate(self, amount):
        """Увеличивает скорость автомобиля"""
        self.speed += amount
        print(f"{self.model} accelerates to {self.speed} km/h")

    def __lt__(self, other):
        """Позволяет сравнивать автомобили по скорости"""
        return self.speed < other.speed

    def __str__(self):
        """Возвращает строковое представление автомобиля"""
        return f"{self.model} ({self.year}) - {self.color}, Speed: {self.speed} km/h"


class ElectricCar(Car):
    """Класс электрического автомобиля"""
    def __init__(self, model, year, color, battery_capacity, speed=0):
        super().__init__(model, year, color, speed)
        self.battery_capacity = battery_capacity

    def __str__(self):
        return super().__str__() + f", Battery: {self.battery_capacity} kWh"


class HybridElectricCar(Car):
    """Класс гибридного автомобиля"""
    def __init__(self, model, year, color, fuel_consumption, speed=0):
        super().__init__(model, year, color, speed)
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return super().__str__() + f", Fuel Consumption: {self.fuel_consumption} L/100km"


class CarFleet:
    """Класс для управления автопарком"""
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        """Добавляет автомобиль в автопарк"""
        self.cars.append(car)
        print(f"{car.model} added to the fleet.")

    def sort_by_speed(self):
        """Сортирует автомобили по скорости"""
        self.cars.sort(reverse=True)  # Сортировка по убыванию скорости
        print("Fleet sorted by speed.")

    def display_fleet(self):
        """Выводит список автомобилей в автопарке"""
        for car in self.cars:
            print(car)

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
car1 = Car("Toyota Corolla", 2015, "White", 80)
car2 = ElectricCar("Tesla Model S", 2022, "Red", 100, 120)
car3 = HybridElectricCar("Toyota Prius", 2020, "Blue", 4.5, 90)

# # Проверяем ускорение
car1.accelerate(10)  # Toyota Corolla accelerates to 90 km/h
car2.accelerate(20)  # Tesla Model S accelerates to 140 km/h

# # Сравниваем автомобили по скорости
print(car1 < car2)  # True (Toyota Corolla медленнее, чем Tesla Model S)

# # Создаём автопарк
fleet = CarFleet()
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

# # Выводим автопарк
fleet.display_fleet()

# # Сортируем по скорости
fleet.sort_by_speed()
fleet.display_fleet()

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