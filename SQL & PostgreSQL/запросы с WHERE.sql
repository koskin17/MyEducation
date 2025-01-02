-- Выбор всех клиентов в USA
SELECT company_name, contact_name, phone, country
FROM customers
WHERE country = 'USA';

-- Подсчёт всех товаров, цена которых больше 20
SELECT COUNT(*)
FROM products
WHERE unit_price < 20;

-- Выбрать все товары, которые мы не продаём
SELECT *
FROM products
WHERE discontinued = 1;

-- Выбрать всех заказчиков, которые не в Берлине
SELECT *
FROM customers
WHERE city <> 'Berlin';

-- Выбрать все заказы после 01.03.1988. Дата указывается как строка, в '' и в том формате,
-- в котором она в базе данных
SELECT *
FROM orders
WHERE order_date > '1988-03-01';

-- Выбрать все заказы в октябре 1996 году. Дата указывается как строка, в '' и в том формате,
-- в котором она в базе данных
SELECT *
FROM orders
WHERE order_date >= '1996-10-01' AND order_date <= '1996-10-31'