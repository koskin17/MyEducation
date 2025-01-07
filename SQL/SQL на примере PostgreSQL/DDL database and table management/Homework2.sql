-- Создать таблицу exam с полями:
-- - идентификатора экзамена - автоинкрементируемый, уникальный, запрещает NULL;
-- - наименования экзамена
-- - даты экзамена
CREATE TABLE exam
(
	exam_id serial UNIQUE NOT NULL,
	exam_title varchar(256) NOT NULL,
	exam_date DATE
)

-- Удалить ограничение уникальности с поля идентификатора
ALTER TABLE exam
DROP CONSTRAINT "exam_pkey"
-- По умолчаню, у exam_id в случае указания serial UNIQUE NOT NULL имя будет exam_exam_id_key

-- Добавить ограничение первичного ключа на поле идентификатора
ALTER TABLE exam
ADD PRIMARY KEY(exam_id)

-- Просмотр имеющихся ограничений CONSTRAINT
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
    tc.table_name = 'exam'
ORDER BY 
    ccu.column_name;

-- Создать таблицу person с полями
-- - идентификатора личности (простой int, первичный ключ)
-- - имя
-- - фамилия

CREATE TABLE person
(
	person_id INT PRIMARY KEY NOT NULL,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL

	-- Также ограничение на person_id можно прописать в отдельном блоке CONSTRAINT как:
	-- CONSTRAINT pk_person_person_id PRIMARY KEY(person_id)
)

-- 5. Создать таблицу паспорта с полями:
-- - идентификатора паспорта (простой int, первичный ключ)
-- - серийный номер (простой int, запрещает NULL)
-- - регистрация
-- - ссылка на идентификатор личности (внешний ключ)
CREATE TABLE passport
(
	passport_id INT PRIMARY KEY NOT NULL,
	serial_number_passport INT NOT NULL,
	registration TEXT NOT NULL,
	person_id INT NOT NULL,
	
	CONSTRAINT FK_passport_person FOREIGN KEY(person_id) REFERENCES person(person_id)
	-- Также можно прописать:
	-- CONSTRAINT PK_passport_passport_id PRIMARY KEY(passport_id)
	-- CONSTRAINT FK_passport_person FOREING KEY(person_id) REFERENCES person(person_id) 
)

-- 6. Добавить колонку веса в таблицу book (создавали ранее) с ограничением, проверяющим вес (больше 0 но меньше 100)
ALTER TABLE book
ADD COLUMN weight DECIMAL CONSTRAINT CHK_book_weight CHECK(weight > 0 AND weight < 100)

-- 8. Создать таблицу student с полями:
-- - идентификатора (автоинкремент)
-- - полное имя
-- - курс (по умолчанию 1)
CREATE TABLE students
(
	student_id SERIAL PRIMARY KEY NOT NULL,
	full_name TEXT NOT NULL,
	grade INT DEFAULT 1
)
-- DROP TABLE students
-- 9. Вставить запись в таблицу студентов и убедиться, что ограничение на вставку значения по умолчанию работает
INSERT INTO students(full_name)
VALUES ('fullname');

SELECT * FROM students

-- 10. Удалить ограничение "по умолчанию" из таблицы студентов
ALTER TABLE students
ALTER COLUMN grade DROP DEFAULT

-- 11. Подключиться к БД northwind и добавить ограничение на поле unit_price таблицы products (цена должна быть больше 0)
ALTER TABLE products
ADD CONSTRAINT CHK_price_unit_price CHECK(unit_price > 0);

-- 12. "Навесить" автоинкрементируемый счётчик на поле product_id таблицы products (БД northwind).
-- Счётчик должен начинаться с числа следующего за максимальным значением по этому столбцу.
-- Сначала узнаём максимальный id в БД
SELECT MAX(product_id) FROM products
-- Теперь создаём SEQUENCE
CREATE SEQUENCE IF NOT EXISTS product_id_seq
START WITH 78 OWNED BY products_product_id
-- После создания последовательности для product_id меняем колонку и устанавливаем для неё DEFAULT из последовательности product_id_seq
ALTER TABLE products
ALTER COLUMN product_id SET DEFAULT nextval('product_id_seq')
