# You have to create a main course and a dessert at an Italian and a French restaurant, but you won't mix one cuisine with the other. 

# Your task is:

# 1) define a class Product with an abstract method cook(). This class would be base class for the next classes:
# - class FettuccineAlfredo with field name ("Fettuccine Alfredo"), method cook() provides an output of the formatted string "Italian main course prepared: " and name of the dish;
#  - class Tiramisu, with field name ("Tiramisu"), method cook() provides an output of the formatted string "Italian dessert prepared:" and name of the dish;
# - class DuckALOrange, with field name ("Duck À L'Orange"), method cook() provides an output of the formatted string "French main course prepared: " and name of the dish;
# - class CremeBrulee,  with field name ("Crème brûlée"), method cook() provides an output of the formatted string "French dessert prepared: " and name of the dish.
# 2) define a class Factory with an abstract method get_dish() that takes  type_of_meal as a parameter. This class would be base class for the classes ItalianDishesFactory and FrenchDishesFactory. The method get_dish() according to type_of_meal ("main" or "dessert") invokes the dish of appropriate cousine;
# 3) define a class FactoryProducer with the method get_factory(). The method takes the parameter type_of_factory and invokes the appropriate dishes factory (classes ItalianDishesFactory or FrenchDishesFactory).

## 🔷 Что требуется по сути задачи?
# Ты создаёшь систему, в которой:
# * можно **получить блюда (main / dessert)** из разных кухонь (Итальянской, Французской),
# * при этом **не смешивать кухни** — это ключевая идея **абстрактной фабрики**.

## 🔧 Краткий обзор архитектуры решения
### 1. **Product** (абстрактный класс):
# * Базовый класс для всех блюд с методом `cook()`
### 2. **Concrete Products**:
# * `FettuccineAlfredo`, `Tiramisu` — итальянские блюда
# * `DuckALOrange`, `CremeBrulee` — французские блюда
### 3. **Factory** (абстрактный класс):
# * Метод `get_dish(type_of_meal)`, который должен вернуть блюдо (main/dessert)
### 4. **Concrete Factories**:
# * `ItalianDishesFactory`
# * `FrenchDishesFactory`
### 5. **FactoryProducer**:
# * Возвращает нужную фабрику по строковому значению `type_of_factory`

## 🔄 Паттерн Abstract Factory — зачем?
# Ты хочешь получать **разные объекты одной “семьи”**, но не смешивать семейства (в нашем случае — кухни).
# → Abstract Factory идеально подходит для этого!

## ✅ Полное решение задачи:
from abc import ABC, abstractmethod

# Abstract class for dishes
class Product(ABC):
    @abstractmethod
    def cook(self):
        pass

# Class for italian dishes
class FettuccineAlfredo(Product):
    def __init__(self):
        self.name = "Fettuccine Alfredo"

    def cook(self):
        print(f"Italian main course prepared: {self.name}")

class Tiramisu(Product):
    def __init__(self):
        self.name = "Tiramisu"

    def cook(self):
        print(f"Italian dessert prepared: {self.name}")

# Class for french dishes
class DuckALOrange(Product):
    def __init__(self):
        self.name = "Duck À L'Orange"

    def cook(self):
        print(f"French main course prepared: {self.name}")

class CremeBrulee(Product):
    def __init__(self):
        self.name = "Crème brûlée"

    def cook(self):
        print(f"French dessert prepared: {self.name}")

# Abstract factory class
class Factory(ABC):
    @abstractmethod
    def get_dish(self, type_of_meal):
        pass

# Factory class for italian dishes
class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == "main":
            return FettuccineAlfredo()
        elif type_of_meal == "dessert":
            return Tiramisu()
        else:
            raise ValueError("Invalid type of meal. Choose 'main' or 'dessert'.")

# Factory class for french dishes
class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == "main":
            return DuckALOrange()
        elif type_of_meal == "dessert":
            return CremeBrulee()
        else:
            raise ValueError("Invalid type of meal. Choose 'main' or 'dessert'.")

# === Step 5: Factory of Factories ===
class FactoryProducer:
    def get_factory(self, type_of_factory):
        if type_of_factory == "italian":
            return ItalianDishesFactory()
        elif type_of_factory == "french":
            return FrenchDishesFactory()
        else:
            raise ValueError("Invalid factory type. Choose 'italian' or 'french'.")

## 📌 Пример использования:
if __name__ == "__main__":
    producer = FactoryProducer()

    # Итальянский десерт
    italian_factory = producer.get_factory("italian")
    italian_dessert = italian_factory.get_dish("dessert")
    italian_dessert.cook()  # → Italian dessert prepared: Tiramisu

    # Французское основное блюдо
    french_factory = producer.get_factory("french")
    french_main = french_factory.get_dish("main")
    french_main.cook()  # → French main course prepared: Duck À L'Orange

## ✅ Итого:
# * ✅ Использован паттерн **Abstract Factory**
# * ✅ Классы разделены по иерархии
# * ✅ Метод `cook()` реализован у всех продуктов
# * ✅ Объекты создаются фабриками, без прямого вызова классов-продуктов
# * ✅ Решение полностью соответствует всем условиям задачи

# ## 🔧 **Что мы вообще делаем?**

# Мы хотим:

# * готовить **итальянские** и **французские** блюда;
# * у каждой кухни есть **основное блюдо (main)** и **десерт (dessert)**;
# * главное — **не мешать кухни** между собой;
# * и сделать это **гибко**: чтобы легко добавлять новые кухни и блюда в будущем.

# ---

# ## 🔶 ЭТАП 1: БАЗОВЫЙ КЛАСС ДЛЯ ВСЕХ БЛЮД

# ```python
# class Product(ABC):
#     @abstractmethod
#     def cook(self):
#         pass

# ### Что здесь происходит:
# * `Product` — это **родительский (абстрактный) класс**. Все блюда (итальянские и французские) будут его "детьми".
# * Метод `cook()` — это как бы **шаблон**, который **каждое блюдо обязано переопределить**.
#   То есть, любой класс-блюдо должен иметь метод `cook()`.

# ## 🍝 ЭТАП 2: КОНКРЕТНЫЕ БЛЮДА
# ### Итальянские:
# class FettuccineAlfredo(Product):
#     def __init__(self):
#         self.name = "Fettuccine Alfredo"

#     def cook(self):
#         print(f"Italian main course prepared: {self.name}")
# * Это итальянское основное блюдо.
# * Когда вызовешь `cook()`, напечатает: `Italian main course prepared: Fettuccine Alfredo`

# class Tiramisu(Product):
#     def __init__(self):
#         self.name = "Tiramisu"

#     def cook(self):
#         print(f"Italian dessert prepared: {self.name}")
# * Это десерт.

# ### Французские:
# class DuckALOrange(Product):
#     def __init__(self):
#         self.name = "Duck À L'Orange"

#     def cook(self):
#         print(f"French main course prepared: {self.name}")

# class CremeBrulee(Product):
#     def __init__(self):
#         self.name = "Crème brûlée"

#     def cook(self):
#         print(f"French dessert prepared: {self.name}")

# ## 🏭 ЭТАП 3: АБСТРАКТНАЯ ФАБРИКА
# class Factory(ABC):
#     @abstractmethod
#     def get_dish(self, type_of_meal):
#         pass
# * Это **фабрика-шаблон**.
# * Она говорит: "Любая кухня (фабрика) должна уметь давать блюдо, если я скажу `main` или `dessert`".

# ## 🍕 ЭТАП 4: ИТАЛЬЯНСКАЯ ФАБРИКА
# class ItalianDishesFactory(Factory):
#     def get_dish(self, type_of_meal):
#         if type_of_meal == "main":
#             return FettuccineAlfredo()
#         elif type_of_meal == "dessert":
#             return Tiramisu()
# * Если мы просим итальянскую фабрику `get_dish("main")`, она даст `FettuccineAlfredo`.
# * Если просим `"dessert"` — даст `Tiramisu`.

# ## 🥖 ЭТАП 5: ФРАНЦУЗСКАЯ ФАБРИКА
# class FrenchDishesFactory(Factory):
#     def get_dish(self, type_of_meal):
#         if type_of_meal == "main":
#             return DuckALOrange()
#         elif type_of_meal == "dessert":
#             return CremeBrulee()

# Аналогично итальянской фабрике, но для французских блюд.

# ## 🧠 ЭТАП 6: ФАБРИКА ФАБРИК
# class FactoryProducer:
#     def get_factory(self, type_of_factory):
#         if type_of_factory == "italian":
#             return ItalianDishesFactory()
#         elif type_of_factory == "french":
#             return FrenchDishesFactory()
# * Это **менеджер**, который говорит:
#   — "Окей, ты хочешь итальянскую кухню? Вот тебе фабрика".
#   — "Французскую? Легко!"

# ## 🎬 КАК ВСЁ РАБОТАЕТ ВМЕСТЕ
# ### Пример:
# producer = FactoryProducer()  # создаём менеджера фабрик

# italian_factory = producer.get_factory("italian")  # получаем итальянскую фабрику
# dish = italian_factory.get_dish("dessert")         # просим десерт
# dish.cook()  # → Italian dessert prepared: Tiramisu

# ## 💡 В чём польза?
# * Легко добавлять **новые кухни** (просто создаёшь новую фабрику);
# * Всё **чётко организовано**: итальянская фабрика не может дать французское блюдо;
# * Код **гибкий и расширяемый** — не надо переписывать кучу `if` в одном месте.

# ## ✅ Что такое `ABC` и `abstractmethod`?
# ### 🔹 `ABC` = **Abstract Base Class**
# Это специальный класс, который говорит:
# > "Я — **абстрактный**, меня нельзя использовать напрямую. Я — шаблон."

# В Python это делается так:

# from abc import ABC, abstractmethod
# * `ABC` — базовый класс для **абстрактных** классов;
# * `@abstractmethod` — говорит: "этот метод обязателен в наследниках".

# ### 📌 Зачем нужен `ABC`?
# Чтобы **заставить потомков реализовать метод**, иначе будет ошибка:
# class Product(ABC):
#     @abstractmethod
#     def cook(self):
#         pass

# Если ты забудешь `cook()` в каком-то блюде — Python выбросит ошибку.
# 📌 Это защита от ошибок: ты чётко задаёшь правила для всех потомков.

# ## 🧩 Почему нельзя просто без `Product(ABC)`?
# Ты можешь не использовать `ABC`, но тогда:
# * ничего не заставит тебя реализовать `cook()` в потомках;
# * это может привести к **багам** — вызовешь `cook()`, а его нет.

# Абстрактный класс — это **контракт**: "любой, кто от меня наследуется — обязан уметь готовить (`cook()`)".
# ## 🍽 Зачем `Factory` как абстрактный класс?
# Точно так же! Вот он:
# class Factory(ABC):
#     @abstractmethod
#     def get_dish(self, type_of_meal):
#         pass

# Он говорит:
# > "Любая кухня обязана уметь выдавать блюдо по запросу — main или dessert".

# ## 🔧 А можно было просто без `Factory(ABC)`?
# Можно. Но ты тогда потеряешь:
# * понятную архитектуру;
# * **расширяемость**;
# * защиту от ошибок.

# **Паттерн проектирования** (Abstract Factory) специально создаёт абстрактный класс — как **единый интерфейс** для всех фабрик.

# ## 🍝 Почему блюда наследуют `Product`?
# Чтобы они:
# * **все гарантированно имели метод `cook()`**
# * были **взаимозаменяемыми** — ты не думаешь: это `Tiramisu` или `CremeBrulee`, ты просто вызываешь `.cook()`.

# Это называется **полиморфизм** — ты работаешь с объектами одного типа (`Product`), не зная, какой именно у тебя объект.

# ## 🧠 Обобщим:
# | Элемент                   | Зачем нужен                                              |
# | ------------------------- | -------------------------------------------------------- |
# | `ABC`                     | Делает класс абстрактным, нельзя создать напрямую        |
# | `@abstractmethod`         | Обязывает потомков реализовать метод                     |
# | `Product(ABC)`            | Шаблон для всех блюд: они обязаны реализовать `cook()`   |
# | `Factory(ABC)`            | Шаблон для всех фабрик: они обязаны уметь выдавать блюдо |
# | Наследование от `Product` | Все блюда реализуют `cook()`, работают одинаково         |
# | Наследование от `Factory` | Все кухни реализуют `get_dish()`, единый подход          |

# Пример, **почему `ABC` и `@abstractmethod` защищают нас от ошибок**, и **что произойдёт, если их не использовать**.

# ## ❌ Пример без `ABC` и без `@abstractmethod`
# class Product:
#     def cook(self):
#         pass  # просто заглушка

# Теперь создаём блюдо, но… **забываем** реализовать `cook()`:
# class Tiramisu(Product):
#     def __init__(self):
#         self.name = "Tiramisu"
#     # cook забыли!

# ### Что произойдёт, если вызвать `cook()`?
# dessert = Tiramisu()
# dessert.cook()  # работает! ... но ничего не делает 😱

# ### ❗ Это ПЛОХО:
# * Ошибка не возникнет.
# * Ты думаешь, что блюдо приготовлено — но `cook()` ничего не делает.
# * Такой баг может быть **очень сложно заметить**, особенно в больших программах.

# ## ✅ Теперь пример с `ABC` и `@abstractmethod`
# ```python
# from abc import ABC, abstractmethod

# class Product(ABC):
#     @abstractmethod
#     def cook(self):
#         pass

# Теперь если ты снова забудешь реализовать `cook()` в Tiramisu:
# class Tiramisu(Product):
#     def __init__(self):
#         self.name = "Tiramisu"
#     # cook снова забыли!

# ### Что теперь?
# dessert = Tiramisu()  # 💥 ВОТ ТЕПЕРЬ БУДЕТ ОШИБКА!

# ❌ **Ошибка:**
# ```txt
# TypeError: Can't instantiate abstract class Tiramisu with abstract method cook
# ```

# ## 💡 Что это значит?
# Python говорит:
# > “Ты обещал, что все продукты будут уметь готовить (`cook()`),
# > а сам не сделал. Так не пойдёт. Ошибка.”

# Это — **защита от будущих багов.**

# ## 🧠 Вывод:
# | Без `ABC`                                             | С `ABC`                                          |
# | ----------------------------------------------------- | ------------------------------------------------ |
# | Код молча «работает», даже если метод не реализован   | Код выбрасывает ошибку, если метод не реализован |
# | Ошибка проявляется только в рантайме (и то не всегда) | Ошибка видна сразу                               |
# | Сложнее поддерживать код                              | Код надёжный и самодокументированный             |

# Хочешь — покажу короткий пример и с **абстрактной фабрикой (`Factory`)** и аналогичную ситуацию там.


