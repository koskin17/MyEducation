-- SELECT * FROM orders --Выбрать все данные из таблицы customers
-- SELECT order_id, shipped_date - order_date FROM orders -- Выбрать все записи из таблицы orders, но взять две колонки: идентификатор заказа и колонку, значение в которой мы рассчитываем как разницу между датой отгрузки и датой формирования заказа.
-- SELECT DISTINCT ship_city FROM orders -- Выбрать все уникальные города в которых "зарегестрированы" заказчики
-- SELECT DISTINCT ship_city, ship_country FROM orders -- Выбрать все уникальные сочетания городов и стран в которых "зарегестрированы" заказчики
-- SELECT COUNT(DISTINCT employee_id) FROM employees --  Посчитать кол-во заказчиков
-- SELECT COUNT(DISTINCT country) FROM customers -- Посчитать кол-во уникальных стран в которых "зарегестрированы" заказчики

-- SELECT column_name FROM information_schema.columns WHERE table_name = 'orders';
