SELECT product_name, suppliers.company_name, units_in_stock -- Если выбираются столбцы из разных таблиц, то перед именем столбца прописывается название таблицы
FROM products
INNER JOIN suppliers ON products.supplier_id = suppliers.supplier_id
ORDER BY units_in_stock DESC

SELECT category_name, SUM(units_in_stock) AS total_units
FROM products
INNER JOIN categories ON products.category_id = categories.category_id
GROUP BY category_name
ORDER BY total_units DESC
LIMIT 5

SELECT category_name, SUM(unit_price * units_in_stock)
FROM products
INNER JOIN categories ON products.category_id = categories.category_id
WHERE discontinued <> 1
GROUP BY category_name
HAVING SUM(unit_price * units_in_stock) > 5000
ORDER BY SUM(unit_price * units_in_stock) DESC

SELECT order_id, customer_id, employees.first_name, employees.last_name, employees.title
FROM orders
INNER JOIN employees ON orders.employee_id = employees.employee_id

SELECT orders.order_date, products.product_name, orders.ship_country, products.unit_price, order_details.quantity, order_details.discount
FROM orders
INNER JOIN order_details ON orders.order_id = order_details.order_id
INNER JOIN products ON order_details.product_id = products.product_id

SELECT customers.contact_name, customers.company_name, customers.phone, employees.first_name, employees.last_name,
		employees.title, orders.order_date, products.product_name, orders.ship_country, products.unit_price,
		order_details.quantity, order_details.discount
FROM orders
JOIN order_details ON orders.order_id = order_details.order_id -- Если просто написать JOIN, то по умолчанию подразумевается INNER JOIN
JOIN products ON order_details.product_id = products.product_id
JOIN customers ON orders.customer_id = customers.customer_id
JOIN employees ON orders.employee_id = employees.employee_id
WHERE orders.ship_country = 'USA'