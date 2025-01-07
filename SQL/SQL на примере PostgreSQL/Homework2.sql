-- Выбрать все заказы из стран France, Austria, Spain
SELECT *
FROM orders
WHERE ship_country IN ('France', 'Austria', 'Spain')

-- Выбрать все заказы,
-- отсортировать по requited_date (по убыванию) и отсортировать по дате отгрузке (по возрастанию)
SELECT *
FROM orders
ORDER BY required_date DESC, shipped_date

-- Выбрать минимальную цену среди тех продуктов, которых в продаже более 30 единиц.
SELECT MIN(unit_price)
FROM products
WHERE units_in_stock > 30

-- Выбрать максимальную цену среди тех продуктов, которых в продаже более 30 единиц.
SELECT MAX(units_in_stock)
FROM products
WHERE unit_price > 30

-- Найти среднее значение дней уходящих на доставку с даты формирования заказа в USA
SELECT AVG(shipped_date - order_date)
FROM orders
WHERE ship_country = 'USA'

-- Найти сумму, на которую имеется товаров (кол-во * цену) причём таких,
-- которые планируется продавать и в будущем (см. на поле discontinued)
SELECT SUM(unit_price * units_on_order)
FROM products
WHERE discontinued <> 1