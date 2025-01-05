-- Выбрать все уникальные компании-заказчиков, которые делали заказы на более, чем 40 ед. товаров
SELECT DISTINCT company_name
FROM customers
JOIN orders USING(customer_id)
JOIN order_details USING(order_id)
WHERE quantity > 40

-- Тоже самое, но с подзапросом
SELECT DISTINCT company_name
FROM customers
WHERE customer_id = ANY(
						SELECT customer_id
						FROM orders
						JOIN order_details USING(order_id)
						WHERE quantity > 40
)

-- Выбор товаров, кол-во которых больше среднего по заказам
SELECT DISTINCT product_name, quantity
FROM products
JOIN order_details USING(product_id)
WHERE quantity > (
					SELECT AVG(quantity)
					FROM order_details
)
ORDER BY quantity DESC

-- Выбор всех продуктов, кол-во которых больше среднего значения кол-ва товаров,
-- заказанных из групп, полученных группированием по product_id
SELECT DISTINCT product_name, quantity
FROM products
JOIN order_details USING(product_id)
WHERE quantity > ALL(SELECT AVG(quantity)
					FROM order_details
					GROUP BY product_id
					)
ORDER BY quantity