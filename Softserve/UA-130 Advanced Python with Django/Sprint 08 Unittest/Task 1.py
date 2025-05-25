# Write the programm that calculate total price with discount by the products.
# Use class Product(name, price, count) and class Cart. In class Cart you can add the products.
# Discount depends on count product:
# count	discount
# at least 5	5%
# at least 7	10%
# at least 10	20%
# at least 20	30%
# more than 20	50%

# Write unittest with class CartTest and test all methods with logic

# import unittest
# class Product:
#     pass
# class Cart:
#     pass
# class CartTest(unittest.TestCase):
#     pass

# Задача — реализовать **корзину покупок (Cart)**, которая может содержать **товары (Product)**, рассчитывать итоговую цену и **применять скидки в зависимости от количества товара**.

## 📌 ЗАДАЧА В ДЕТАЛЯХ
# Ты должен реализовать:
# 1. Класс `Product` — отдельный товар с названием, ценой и количеством.
# 2. Класс `Cart` — корзина, в которую можно добавлять товары и считать итоговую сумму со скидками.
# 3. Класс `CartTest` — модульные тесты, проверяющие работу корзины.

## ✅ ШАГ 1. Класс `Product`
# class Product:
#     def __init__(self, name, price, count):
#         self.name = name
#         self.price = price
#         self.count = count

### 🔍 Что здесь происходит:
# * `self.name`: Название товара (например, `"Apple"`).
# * `self.price`: Цена за единицу (например, `2.5`).
# * `self.count`: Сколько штук купили (например, `10`).

## ✅ ШАГ 2. Класс `Cart`
# class Cart:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product: Product):
#         self.products.append(product)

#     def get_total_count(self):
#         return sum(product.count for product in self.products)

#     def get_discount(self):
#         count = self.get_total_count()
#         if count > 20:
#             return 0.50
#         elif count >= 20:
#             return 0.30
#         elif count >= 10:
#             return 0.20
#         elif count >= 7:
#             return 0.10
#         elif count >= 5:
#             return 0.05
#         return 0.0

#     def get_total_price(self):
#         total = sum(product.price * product.count for product in self.products)
#         discount = self.get_discount()
#         return total * (1 - discount)

### 🔍 Пояснение к методам:
# | Метод               | Что делает                                                 |
# | ------------------- | ---------------------------------------------------------- |
# | `add_product`       | Добавляет товар в корзину (`self.products`)                |
# | `get_total_count()` | Возвращает общее количество товаров в корзине              |
# | `get_discount()`    | Смотрит общее количество и выбирает скидку по правилам     |
# | `get_total_price()` | Считает итоговую цену со скидкой: (цена × кол-во) − скидка |

## ✅ ШАГ 3. Тесты (модуль `unittest`)
# import unittest

# class CartTest(unittest.TestCase):
#     def test_add_single_product(self):
#         cart = Cart()
#         p1 = Product("Apple", 2, 1)
#         cart.add_product(p1)
#         self.assertEqual(len(cart.products), 1)

#     def test_total_count(self):
#         cart = Cart()
#         cart.add_product(Product("Apple", 2, 4))
#         cart.add_product(Product("Banana", 1, 3))
#         self.assertEqual(cart.get_total_count(), 7)

#     def test_discount_levels(self):
#         cart = Cart()
#         cart.add_product(Product("Apple", 1, 4))
#         self.assertEqual(cart.get_discount(), 0.0)

#         cart.add_product(Product("Apple", 1, 1))  # Итого 5
#         self.assertEqual(cart.get_discount(), 0.05)

#         cart.add_product(Product("Apple", 1, 2))  # Итого 7
#         self.assertEqual(cart.get_discount(), 0.10)

#         cart.add_product(Product("Apple", 1, 3))  # Итого 10
#         self.assertEqual(cart.get_discount(), 0.20)

#         cart.add_product(Product("Apple", 1, 10))  # Итого 20
#         self.assertEqual(cart.get_discount(), 0.30)

#         cart.add_product(Product("Apple", 1, 1))  # Итого 21
#         self.assertEqual(cart.get_discount(), 0.50)

#     def test_total_price_with_discount(self):
#         cart = Cart()
#         cart.add_product(Product("Apple", 10, 10))  # Сумма: 100
#         # Должна быть скидка 20% => цена 80
#         self.assertEqual(cart.get_total_price(), 80.0)

## ✅ Полный код целиком
import unittest

class Product:
    # Class for product in Cart
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    # Class for Cart with products
    def __init__(self, products=None):
        self.products = list(products) if products else []

    # | Код              | Пояснение                                                  |
    # | ---------------- | ---------------------------------------------------------- |
    # | `products=None`  | Аргумент по умолчанию. Можно не передавать список товаров. |
    # | `if products`    | Если список передан — используем его.                      |
    # | `list(products)` | Преобразуем в обычный список (на случай, если это кортеж). |
    # | `[]`             | Если ничего не передано — корзина пустая.                  |


    # Add product to Cart
    def add_product(self, product: Product):
        self.products.append(product)

    # Get total count of products in Cart
    def get_total_count(self):
        return sum(product.count for product in self.products)

    # Get discount based on total count of products
    def get_discount(self):
        count = self.get_total_count()
        if count > 20:
            return 0.50
        elif count >= 20:
            return 0.30
        elif count >= 10:
            return 0.20
        elif count >= 7:
            return 0.10
        elif count >= 5:
            return 0.05
        return 0.0

    # Get total price with discount applied
    def get_total_price(self):
    # The discount is applied to each product separately, depending on its count.
        total = 0
        for product in self.products:
            count = product.count
            price = product.price

            # Determine the discount by quantity
            if count > 20:
                discount = 0.5
            elif count >= 20:
                discount = 0.3
            elif count >= 10:
                discount = 0.2
            elif count >= 7:
                discount = 0.1
            elif count >= 5:
                discount = 0.05
            else:
                discount = 0

            total += price * count * (1 - discount)

        return total


# Test for logic of Cart
class CartTest(unittest.TestCase):
    # Test adding a single product to Cart
    def test_add_single_product(self):
        cart = Cart()
        p1 = Product("Apple", 2, 1)
        cart.add_product(p1)
        self.assertEqual(len(cart.products), 1)

    # Test total count of products in Cart
    def test_total_count(self):
        cart = Cart()
        cart.add_product(Product("Apple", 2, 4))
        cart.add_product(Product("Banana", 1, 3))
        self.assertEqual(cart.get_total_count(), 7)

    # Test discount levels based on total count of products
    def test_discount_levels(self):
        cart = Cart()
        cart.add_product(Product("Apple", 1, 4))
        self.assertEqual(cart.get_discount(), 0.0)

        cart.add_product(Product("Apple", 1, 1))  # 5
        self.assertEqual(cart.get_discount(), 0.05)

        cart.add_product(Product("Apple", 1, 2))  # 7
        self.assertEqual(cart.get_discount(), 0.10)

        cart.add_product(Product("Apple", 1, 3))  # 10
        self.assertEqual(cart.get_discount(), 0.20)

        cart.add_product(Product("Apple", 1, 10))  # 20
        self.assertEqual(cart.get_discount(), 0.30)

        cart.add_product(Product("Apple", 1, 1))  # 21
        self.assertEqual(cart.get_discount(), 0.50)

    # Test total price with discount applied
    def test_total_price_with_discount(self):
        cart = Cart()
        cart.add_product(Product("Apple", 10, 10))  # 100
        self.assertEqual(cart.get_total_price(), 80.0)


if __name__ == "__main__":
    unittest.main()

## 🧠 Зачем всё это делается?
# | Элемент          | Почему нужен                                          |
# | ---------------- | ----------------------------------------------------- |
# | Класс `Product`  | Чтобы разделить логику товара и корзины. Модульность. |
# | Класс `Cart`     | Управляет товарами, считает общую цену и скидку.      |
# | `get_discount()` | Логика скидки в одном месте — проще поддерживать.     |
# | `unittest`       | Проверка работы на автомате — быстро, надёжно.        |

