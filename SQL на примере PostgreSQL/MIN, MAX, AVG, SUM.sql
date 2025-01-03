-- Сортировка по умолчанию по возрастанию
SELECT ship_city, order_date
FROM orders
WHERE ship_city = 'London'
ORDER BY order_date

-- Получаем самый первый заказ (минимальная дата)
SELECT MIN(order_date)
FROM orders
WHERE ship_city = 'London'

-- Сортировка по умолчанию по убыванию
SELECT ship_city, order_date
FROM orders
WHERE ship_city = 'London'
ORDER BY order_date DESC

-- Получаем самый новый / последний заказ (максимальная дата)
SELECT MAX(order_date)
FROM orders
WHERE ship_city = 'London'

--Определяем среднюю цену по всем продуктам
SELECT AVG(unit_price)
FROM products
WHERE discontinued <> 1

-- Вычисляем сумму
SELECT SUM(units_in_stock)
FROM products
WHERE discontinued <> 1