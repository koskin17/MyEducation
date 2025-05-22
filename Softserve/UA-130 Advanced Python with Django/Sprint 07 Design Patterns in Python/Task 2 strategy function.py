# Your task is to create an application for the departmental store. Initially, there was one and only one type of discount called the On-Sale-Discount (50%). But as time passes, the owner of the departmental store demands for including some other types of discount also for the customers. 

# Please, solve the above-described problem in an efficient way. Our actual class should store the reference to one of the strategy function.

# You have the structure of your future application in the answer box preload.

# Заготовка кода:
# class Goods: 
  
#     def __init__(self, price, discount_strategy = None): 
          
#     def price_after_discount(self): 
          
# def on_sale_discount(product): 
      
# def twenty_percent_discount(product): 
      
# Цель этой задачи — реализовать **гибкую систему скидок** для магазина, используя **паттерн проектирования "Стратегия" (Strategy Pattern)**.

## 🧠 Суть задачи
# У нас есть товары (`Goods`) с ценой.
# Раньше скидка была только одна — 50%, но теперь нужно:
# * применять разные стратегии скидок;
# * уметь **гибко переключаться между ними**, не переписывая код класса `Goods`.

## ✅ Как это решается?
# Через **паттерн "Стратегия"**:
# > Объект (`Goods`) хранит ссылку на функцию-стратегию (в нашем случае — скидку), и вызывает её при расчёте цены.

## 🔨 Шаг за шагом
### 🔹 Шаг 1. Класс `Goods`
# Он должен:
# * хранить цену (`price`);
# * ссылку на стратегию скидки (`discount_strategy`);
# * иметь метод `price_after_discount()` — он вызывает стратегию, если она есть.
# class Goods:
#     def __init__(self, price, discount_strategy=None):
#         self.price = price
#         self.discount_strategy = discount_strategy

#     def price_after_discount(self):
#         if self.discount_strategy:
#             return self.discount_strategy(self)
#         return self.price

### 🔹 Шаг 2. Стратегии (функции)
# Они принимают **объект товара (`product`)**, и возвращают новую цену:
# def on_sale_discount(product):
#     """50% скидка"""
#     return product.price * 0.5

# def twenty_percent_discount(product):
#     """20% скидка"""
#     return product.price * 0.8

# Ты можешь легко добавлять ещё стратегии, не меняя класс `Goods`.

# Main class with reference to function-strategy
class Goods:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy  # set a discount - link to function for calculation price with set discount

    def price_after_discount(self):
        if self.discount_strategy:  # if discount is set - call function for calculation price with set discount 
            return self.discount_strategy(self) #call function with the appropriate discount
        return self.price   # return the same price if discount is not set
    
    def __str__(self):
        return f"Price: {self.price}, price after discount: {self.price_after_discount()}"

def on_sale_discount(product):
    """calculation price with 50% discount"""
    return product.price * 0.5

def twenty_percent_discount(product):
    """calculation price with 20% discount"""
    return product.price * 0.8

## 🎯 Пример использования:
item1 = Goods(100, discount_strategy=on_sale_discount)
print(item1.price_after_discount())  # 👉 50.0

item2 = Goods(200, discount_strategy=twenty_percent_discount)
print(item2.price_after_discount())  # 👉 160.0

item3 = Goods(150)  # без скидки
print(item3.price_after_discount())  # 👉 150.0

## 📌 Преимущества такого подхода
# * ✅ Стратегии можно **добавлять или изменять** отдельно от класса товара.
# * ✅ Поддержка **расширяемости** — можно сделать скидку по времени, по акции, по клубной карте и т.д.
# * ✅ Класс `Goods` остаётся **простым и чистым**.

# Мы сделали класс `Goods` и при создании объекта класса "прикрепляем к нему" ссылку на функцию расчёта скидки (функцию-стратегию)::
# item = Goods(100, discount_strategy=on_sale_discount)

# В результате у объекта есть параметр, который является ссылкой на функцию-стратегию потому что мы передали её в конструктор `__init__()`.
# class Goods:
#     def __init__(self, price, discount_strategy=None):
#         self.price = price
#         self.discount_strategy = discount_strategy

# Вот эта строчка делает всю магию:
# self.discount_strategy = discount_strategy

# И теперь, когда мы вызывает параметр `discount_strategy` и объекта 'self', мы для этого объекта вызывается функцию, на которую установлена ссылка. А эта функция уже делает то, что в ней прописано и возвращает то, что мы указали возвращать:
# self.discount_strategy(self)

### Что это значит?
# * `self.discount_strategy` — это **ссылка на функцию**, которую мы передали;
# * `self` — это объект `Goods`, и он передаётся в качестве параметра `order` (мы его переименовали в order при передаче в функцию).

## 🔍 А функция — это что-то особенное?
# Нет. В Python **функции — это объекты**, и их можно:
# * передавать как аргументы;
# * хранить в переменных;
# * возвращать из других функций.
# Это и называется **функция высшего порядка** (higher-order function).

## 📦 Схема
# Goods
# │
# ├── price = 100
# └── discount_strategy = on_sale_discount  ← ссылка на функцию

# ↓ при вызове

# item.price_after_discount()
# ↓
# self.discount_strategy(self)
# ↓
# on_sale_discount(self)
# ↓
# self.price * 0.5

## 💡 Важно понимать:
# * Мы **не "импортируем" функцию внутрь класса**;
# * Мы просто **сохраняем на неё ссылку в атрибуте объекта**, как если бы это была переменная или строка.

## 🧪 Хочешь увидеть?
# def hello():
#     print("Hello!")

# x = hello   # теперь x — это ссылка на функцию
# x()         # вызовет hello()

# Точно так же:
# item = Goods(100, discount_strategy=on_sale_discount)
# item.discount_strategy(item)  # вызовет функцию

# Давай разберём, **почему лучше использовать стратегию (как ты сейчас изучаешь)**, а не `if` или `match-case` внутри класса.

## ❓Что ты предлагаешь?
# Ты говоришь:
# А почему бы не сделать так:
# class Goods:
#     def __init__(self, price, discount_type=None):
#         self.price = price
#         self.discount_type = discount_type

#     def price_after_discount(self):
#         if self.discount_type == "on_sale":
#             return self.price * 0.5
#         elif self.discount_type == "twenty":
#             return self.price * 0.8
#         else:
#             return self.price
# На первый взгляд — **логично и просто**. Но есть серьёзные **проблемы, особенно при масштабировании**:

## ❌ Минусы подхода с `if` / `case` в методе
### 1. **Нарушение принципа открытости/закрытости (OCP)**
# > Принцип Открытости/Закрытости (Open-Closed Principle):
# > *«Программа должна быть открыта для расширения, но закрыта для изменения».*

# Каждый раз, когда ты хочешь добавить новый тип скидки:
# * тебе нужно лезть в класс `Goods` и **менять код**;
# * это увеличивает риск ошибок;
# * и нарушает принцип OCP.

### 2. **Усложнение кода и снижение читаемости**
# Вместо того чтобы просто описать скидку, ты:
# * увеличиваешь количество ветвлений `if`/`elif`;
# * начинаешь проверять кучу строк типа `"on_sale"`, `"twenty"` — **это хрупкие "магические строки"** (magic strings);
# * читаемость падает.

### 3. **Нет гибкости и переиспользования**
# Функции или классы-стратегии можно:
# * **переиспользовать** в других проектах;
# * **тестировать отдельно**;
# * **комбинировать**, передавать, заменять.

# А `if` внутри метода — это **жёстко вшитая логика**, которую нельзя поменять "снаружи".

## ✅ Преимущества паттерна "Стратегия"
# | Характеристика                | `if` внутри класса        | Стратегия (функция/объект)     |
# | ----------------------------- | ------------------------- | ------------------------------ |
# | Добавить новую скидку         | ❌ Меняем код класса       | ✅ Просто создаём новую функцию |
# | Нарушение OCP                 | ❌ Да                      | ✅ Нет                          |
# | Гибкость и переиспользуемость | ❌ Нет                     | ✅ Высокая                      |
# | Тестирование                  | ❌ Только вместе с классом | ✅ Каждую стратегию отдельно    |
# | IDE автоподсказки             | ❌ Нет для строк           | ✅ Да (по функциям)             |

## 💬 Простой пример:
# Сравни:
# Strategy (гибко и чисто)
# item = Goods(100, discount_strategy=twenty_percent_discount)

# С этим:
# if-версия
# item = Goods(100, discount_type="twenty")

# ✅ В первом случае:
# * discount\_strategy — **реальная функция**, IDE подскажет, что она принимает, что возвращает.
# * можно сделать стратегию классом, параметризовать её.

# ❌ Во втором — строка `"twenty"`:
# * может быть с опечаткой (`"twnety"`) — баг.
# * никаких подсказок, никакой гибкости.

## 🎯 Вывод:
# > Использование стратегии — это архитектурное решение, которое делает код **гибким, масштабируемым, читаемым и безопасным**.
# Ты **можешь** использовать `if` — особенно в маленьких проектах.
# Но в серьёзных и расширяемых — **лучше сразу идти по пути "Стратегия"**.
