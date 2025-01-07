-- Создать таблицу teacher с полями teacher_id serial, first_name varchar, last_name varchar, birthday date, phone varchar, title varchar
-- CREATE TABLE teacher
-- (
-- 	teacher serial,
-- 	first_name varchar,
-- 	last_name varchar,
-- 	birthdate date,
-- 	phone varchar,
-- 	title varchar
-- )

-- Добавить в таблицу после создания колонку middle_name varchar
-- ALTER TABLE teacher
-- ADD COLUMN middle_name varchar

-- Удалить колонку middle_name
-- ALTER TABLE teacher
-- DROP COLUMN middle_name

-- Переименовать колонку birthday в birth_date
-- ALTER TABLE teacher RENAME COLUMN birthdate TO birth_date;

-- Изменить тип данных колонки phone на varchar(32)
-- ALTER TABLE teacher
-- ALTER COLUMN phone SET DATA TYPE varchar(32)

-- Создать таблицу exam с полями exam_id serial, exam_name varchar(256), exam_date date
-- CREATE TABLE exam
-- (
-- 	exam_id serial,
-- 	exam_name varchar(256),
-- 	exam_date date
-- )

-- Вставить три любых записи с автогенерацией идентификатора
-- INSERT INTO teacher (first_name, last_name, birth_date, phone, title)
-- VALUES (
-- 	'first_name teacher1',
-- 	'last_name teacher1',
-- 	'01.01.2025',
-- 	'+380123456',
-- 	'title1'
-- );
-- INSERT INTO teacher (first_name, last_name, birth_date, phone, title)
-- VALUES (
-- 	'first_name teacher2',
-- 	'last_name teacher2',
-- 	'01.01.2025',
-- 	'+380123456',
-- 	'title2'
-- );
-- INSERT INTO teacher (first_name, last_name, birth_date, phone, title)
-- VALUES (
-- 	'first_name teacher3',
-- 	'last_name teacher3',
-- 	'01.01.2025',
-- 	'+380123456',
-- 	'title3'
-- );

-- Посредством полной выборки убедиться, что данные были вставлены нормально и идентификаторы были сгенерированы с инкрементом
-- SELECT * FROM teacher

-- Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
-- TRUNCATE TABLE teacher RESTART IDENTITY;
