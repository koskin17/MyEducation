-- Выборка компаний, которые не делают заказы
SELECT customers.company_name, orders.order_id
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.customer_id
WHERE order_id IS NULL

-- Выборка работников, которые не получают заказы - результат: все работники работают :)
SELECT employees.last_name, orders.order_id
FROM employees
LEFT JOIN orders ON orders.employee_id = employees.employee_id
WHERE order_id IS NULL

-- Вариант подсчёта кол-ва работников
SELECT COUNT(*)
FROM employees
LEFT JOIN orders ON orders.employee_id = employees.employee_id
WHERE order_id IS NULL

-- RIGHT JOIN
SELECT customers.company_name, orders.order_id
FROM orders
RIGHT JOIN customers ON orders.customer_id = customers.customer_id
WHERE order_id IS NULL