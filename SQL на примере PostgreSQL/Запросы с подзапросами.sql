-- Выбор компаний-заказчиков и стран, из которых они
SELECT country, company_name
FROM suppliers
WHERE country IN (SELECT DISTINCT country
					FROM customers)

-- Аналогичный запрос, но без подзапроса
SELECT DISTINCT suppliers.country, suppliers.company_name
FROM suppliers
JOIN customers USING(country)

-- Выбор минимального id (для пример))
SELECT MIN(product_id)
FROM products

-- Выбор суммы единиц товаров, разбитых на группы, и лимитировать набор записей числом, которое необходимо вычислить
SELECT category_name, SUM(units_in_stock)
FROM products
INNER JOIN categories USING (category_id)
GROUP BY category_name
ORDER BY SUM(units_in_stock) DESC
LIMIT (SELECT MIN(product_id) + 4 FROM products) -- Выбор на 4 записи больше, чем минимальный id, с использованием подзапроса

-- Выбоор товаров, количество которых больше, чем в среднем
SELECT product_name, units_in_stock
FROM products
WHERE units_in_stock > (SELECT AVG(units_in_stock)
							FROM products)
ORDER BY units_in_stock DESC