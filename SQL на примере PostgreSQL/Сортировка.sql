-- Сортировка по возрастанию
SELECT DISTINCT country
FROM customers
ORDER BY country ASC

-- Сортировка по убыванию
SELECT DISTINCT country
FROM customers
ORDER BY country DESC

-- Сортировка по двум колонкам
SELECT DISTINCT country, city
FROM customers
ORDER BY country DESC, city DESC

-- Сортировка по двум колонкам в обратную сторону
SELECT DISTINCT country, city
FROM customers
ORDER BY country DESC, city ASC