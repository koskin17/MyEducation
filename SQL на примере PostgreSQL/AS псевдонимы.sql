SELECT COUNT(*) AS employees_count
FROM employees

SELECT COUNT(DISTINCT country) AS country
FROM employees

-- Важно помнить, что псевдонимы AS не будут рабоать в WHERE. Дело в том, что FROM и WHERE отрабатывают первые, а потом работает SELECT
-- Т.е. назначение псевдонима происходит после этих команд и из-за этого FROM и WHERE еще не знают про псевдонимы.

-- Пример
SELECT category_id, SUM(units_in_stock) AS units_in_stock
FROM products
GROUP BY category_id
ORDER BY units_in_stock DESC
LIMIT 5

-- Пример того, как не работает
SELECT category_id, SUM(unit_price * units_in_stock) AS total_price
FROM products
WHERE discontinued <> 1
GROUP BY category_id
HAVING total_price > 5000 -- Здесь надо дублировать запись SUM(unit_price * units_in_stock)
ORDER BY total_price DESC