-- Просмотр имеющихся CONSTRAINT во всей базе данных PostgreSQL
-- В этом запросе явно указано, что:
-- `table_name` и `column_name` берутся из таблицы `constraint_column_usage`.

SELECT 
    ccu.table_name,
    ccu.column_name,
    tc.constraint_name,
    tc.constraint_type
FROM 
    information_schema.constraint_column_usage AS ccu
JOIN 
    information_schema.table_constraints AS tc
    ON ccu.constraint_name = tc.constraint_name
WHERE 
    tc.constraint_type IN ('PRIMARY KEY', 'FOREIGN KEY', 'UNIQUE', 'CHECK')
ORDER BY 
    ccu.table_name, ccu.column_name;


-- Просмотр имеющихся CONSTRAINT в PostgreSQL БД в конкретной таблице

SELECT 
    ccu.table_name,
    ccu.column_name,
    tc.constraint_name,
    tc.constraint_type
FROM 
    information_schema.constraint_column_usage AS ccu
JOIN 
    information_schema.table_constraints AS tc
    ON ccu.constraint_name = tc.constraint_name
WHERE 
    tc.table_name = 'name of table'
ORDER BY 
    ccu.column_name;
