SELECT customers.contact_name, customers.company_name, customers.phone, employees.first_name, employees.last_name,
		employees.title, orders.order_date, products.product_name, orders.ship_country, products.unit_price,
		order_details.quantity, order_details.discount
FROM orders
JOIN order_details USING(order_id) -- ON orders.order_id = order_details.order_id -- Если просто написать JOIN, то по умолчанию подразумевается INNER JOIN
JOIN products USING(product_id) -- ON order_details.product_id = products.product_id
JOIN customers USING(customer_id) -- ON orders.customer_id = customers.customer_id
JOIN employees USING(employee_id) -- ON orders.employee_id = employees.employee_id
WHERE orders.ship_country = 'USA'

-- NATURAL JOIN
-- Работает как INNER JOIN, но соединение проходит по всем столбцам, которые имеют одинаковое наименование.
-- Т.е. нам не обязательно прописывать USING и наименование столбца. Система сама находит и объединяет.
-- Но в данно случае код не явен и настоятельно рекомендуется указывать по какому столбцу происходит соединение.
-- Это проще при отладке. Это более понятно.
-- Также есть риск того, что после написание запроса с NATURAL JOIN могут быть введены столбцы с одинаковыми именами
-- и запрос в итоге будет работать некорретно.
-- ЛУЧШЕ ЕГО ВООБЩЕ НИКОГДА НЕ ИСПОЛЬЗОВАТЬ
SELECT order_id, customer_id, first_name, last_name, title
FROM orders
NATURAL JOIN employees