-- Сначала удаляем таблицу publisher
-- DROP TABLE publisher
-- -- Потом удаляем таблицу book, но удалить её сразу нельзя потому что на неё ссылается таблица boot_author.
-- -- Из-за этого сначала удаляем таблицу book_author, а потом уже таблицу book
-- DROP TABLE book_author
-- DROP TABLE book
-- Теперь создаём заново таблицу publisher
CREATE TABLE publisher
(
	publisher_id INT,
	publisher_name varchar(128) NOT NULL,
	address text,

	-- Добавляем PRIMARY KEY в отдельном блоке CONSTRAINT
	CONSTRAINT PK_publisher_publisher_id PRIMARY KEY(publisher_id)
);

-- Создаём таблицу book
CREATE TABLE book
(
	book_id INT,
	title text NOT NULL,
	isbn varchar(32) NOT NULL,
	publisher_id INT,

	CONSTRAINT PK_book_id PRIMARY KEY(book_id)
)


INSERT INTO publisher
VALUES
(1, 'The Diary of a Yoing Girl', '0199535566'),
(2, 'Pride and Prejudice', '9780307594006'),
(3, 'To Kill a Mockingbird', '04461310786'),
(4, 'The Book of Gutsy Women', '1501178415'),
(5, 'War and Peace', '1788886526');

-- Если мы не добавляем PRIMARY KEY, то в поля можно вставить всё, что угодно
INSERT INTO book
VALUES
(1, 'The Diary of a Yoing Girl', '0199535566', 10)
SELECT * FROM book
-- В результате в publisher_id запишется 10, которая никуда не ссылается и ни к чему не относится.
-- Для того, чтобы этого не было добавляется ограничение внешнего ключа
-- Сначала удаляем данные в таблице book
TRUNCATE TABLE book
-- Теперь добавляем CONSTRAINT в таблицу
ALTER TABLE book
ADD CONSTRAINT FR_books_publisher FOREIGN KEY(publisher_id) REFERENCES publisher(publisher_id) -- FOREIGN KEY по колонке publisher_id
																								 -- который относится/ссылается на таблицу
																								 -- publisher и колонку publisher_id
-- Теперь, после добавления CONSTRAINT, если пробовать вставлять в таблицу вот такое:
INSERT INTO book
VALUES
(1, 'The Diary of a Yoing Girl', '0199535566', 10)
-- То выдаётся ошибка из-за нарушения правил внешнего ключа: сервер видет, что в таблице,
-- на котороую ссылкается foreing key, такого значения нет.
-- Если надо сразу задать такое ограничение, то в блоке CONSTRAINT таблицы book: CONSTRAINT PK_book_id PRIMARY KEY(book_id)
-- через запятую, на следующей строке добавляется еще одно огранчение CONSTRAINT:
-- CONSTRAINT PK_book_publisher FOREIGN KEY(publisher_id) REFERENCES publisher(publisher_id)
-- Теперь проверяем:
DROP TABLE book

CREATE TABLE book
(
	book_id INT,
	title text NOT NULL,
	isbn varchar(32) NOT NULL,
	publisher_id INT,

	CONSTRAINT PK_book_id PRIMARY KEY(book_id),
	CONSTRAINT FK_book_publisher FOREIGN KEY(publisher_id) REFERENCES publisher(publisher_id)
)

-- Также можно удалять CONSTRAINT:
ALTER TABLE book
DROP CONSTRAINT FK_book_publisher

-- Просмотр имеющихся CONSTRAINT
SELECT constraint_name
FROM information_schema.key_column_usage
WHERE table_name = 'book'
	AND table_schema = 'public'
