-- Вывести все страны и работников из этих стран
SELECT country
FROM customers
UNION -- Операция объединения, которая объединяет результаты двух SELECT и сразу удалляет дубликаты
SELECT country
FROM employees

-- Операция пересечения баз данных - вывод стран, из которых и customers и suppliers
SELECT country
FROM customers
INTERSECT
SELECT country
FROM suppliers

-- Найти те страны, в которых проживают customers, но не проживают suppliers
SELECT country
FROM customers
EXCEPT -- Исключает страны из левой (верхней БД), в которой customers не проживают
SELECT country
FROM suppliers