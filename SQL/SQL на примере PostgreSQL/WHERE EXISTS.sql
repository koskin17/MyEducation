-- Выбор компании и имена заказчиков, которые делали заказы весом от 50 до 100 кг.
SELECT company_name, contact_name
FROM customers
WHERE EXISTS (SELECT customer_id FROM orders
				WHERE orders.customer_id = customers.customer_id
				AND freight BETWEEN 50 AND 100)

-- Выбрать заказчиков, которые не customers.contact_name
FROM customers
WHERE NOT EXISTS (SELECT customer_id FROM orders
					WHERE orders.customer_id = customers.customer_id
					AND order_date BETWEEN '1995-02-01' AND '1995-02-15')

-- Выбрать продукты, которые не покупались в период с 1995-02-01 по 1995-02-15
SELECT product_name
FROM products
WHERE NOT EXISTS (SELECT orders.order_id FROM orders
					JOIN order_details USING (order_id)
					WHERE order_details.product_id = product_id
					AND order_date BETWEEN '1995-02-01' AND '1995-02-15')
