# Create a Pizza class with the attributes order_number and ingredients (which is given as a list). Only the ingredients will be given as input.

# You should also make it so that its possible to choose a ready made pizza flavour rather than typing out the ingredients manually! As well as creating this Pizza class, hard-code the following pizza flavours.

# Examples:
# p1 = Pizza(["bacon", "parmesan", "ham"])   # order 1
# p2 = Pizza.garden_feast()                  # order 2
# p1.ingredients ➞ ["bacon", "parmesan", "ham"]
# p2.ingredients ➞ ["spinach", "olives", "mushroom"]
# p1.order_number ➞ 1
# p2.order_number ➞ 2

# Задача требует создать класс Pizza, который:
# - Хранит атрибуты order_number и ingredients.
# - Позволяет создавать экземпляры как с пользовательскими ингредиентами, так и через готовые варианты (garden_feast, hawaiian, meat_festival).
# - Учитывает автоматическое увеличение order_number для каждого нового заказа.

class Pizza:
    # Общий счетчик для номеров заказов
    order_counter = 0

    def __init__(self, ingredients):
        """Создание нового объекта Pizza с указанными ингредиентами"""
        Pizza.order_counter += 1  # Увеличиваем номер заказа
        self.order_number = Pizza.order_counter
        self.ingredients = ingredients  # Сохраняем ингредиенты

    @classmethod
    def hawaiian(cls):
        """Создает пиццу Hawaiian с фиксированными ингредиентами"""
        return cls(["ham", "pineapple"])

    @classmethod
    def meat_festival(cls):
        """Создает пиццу Meat Festival с фиксированными ингредиентами"""
        return cls(["beef", "meatball", "bacon"])

    @classmethod
    def garden_feast(cls):
        """Создает пиццу Garden Feast с фиксированными ингредиентами"""
        return cls(["spinach", "olives", "mushroom"])


# ✅ **Примеры использования**
p1 = Pizza(["bacon", "parmesan", "ham"])  # order 1
p2 = Pizza.garden_feast()                 # order 2

print(p1.ingredients)  # ➞ ["bacon", "parmesan", "ham"]
print(p2.ingredients)  # ➞ ["spinach", "olives", "mushroom"]
print(p1.order_number) # ➞ 1
print(p2.order_number) # ➞ 2

#  Разбор решения
# 1️⃣ Атрибут order_counter
# - Я сделал order_counter статической переменной (Pizza.order_counter), чтобы каждый новый заказ получал уникальный номер.
# - Он увеличивается при каждом создании экземпляра Pizza.
# 2️⃣ Конструктор __init__
# - Принимает список ingredients и сохраняет его.
# - Присваивает уникальный номер заказа (self.order_number).
# 3️⃣ Методы класса @classmethod
# - hawaiian(), meat_festival(), garden_feast() создают предопределенные пиццы.
# - Используется cls(...), чтобы возвращать новый экземпляр Pizza с нужными ингредиентами.

# 🚀 Почему решение правильное?
# ✔ Соответствует условиям: можно создавать пиццу по готовым рецептам и с любыми ингредиентами.
# ✔ Сохраняет номера заказов: order_number увеличивается автоматически.
# ✔ Код структурирован: легко читаемый, масштабируемый.

p1 = Pizza(['bacon', 'parmesan', 'ham'])
print(p1.ingredients)

p2 = Pizza.garden_feast()
print(p2.ingredients)

p3 = Pizza.hawaiian()
print(p3.ingredients)

p4 = Pizza.meat_festival()
print(p4.ingredients)

p5 = Pizza(["pepperoni", "bacon"])
print(p5.ingredients)

my_pizza = Pizza(['cheese', 'caviar', 'oyster', 'uranium'])
print(my_pizza.ingredients)

print(p1.order_number)
print(p2.order_number)
print(p3.order_number)
print(p4.order_number)
print(p5.order_number)
print(my_pizza.order_number)