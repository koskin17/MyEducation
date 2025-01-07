-- UPDATE
SELECT * FROM author

UPDATE author
SET rating = 6.2
WHERE author_id = 11

SELECT author.author_id FROM author
WHERE fullname = 'Alice'

-- DELETE
DELETE FROM author
WHERE rating < 4.5;

SELECT * FROM author

-- Для удаления всех строк просто указывается имя таблицы и всё
DELETE FROM author
-- При этом лог удаления запишется в базу логов, в отличие от команды  TRUNCATE, которая никаких логов не пишет.

-- RETURNING
DROP TABLE book

CREATE TABLE book
(
	book_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
	title TEXT NOT NULL,
	isbn VARCHAR(32) NOT NULL,
	publisher_id INT NOT NULL,

	CONSTRAINT PK_book_book_id PRIMARY KEY(book_id)
)

-- В этом случае в БД просто добавятся данные, но мы не увидим результат / output
INSERT INTO book(title, isbn, publisher_id)
VALUES('title', 'isbn', 3)
-- Если же мы хотим и сразу получить результат, но надо использовать команду RETURNING
RETURNING book_id -- К примеру, посмотреть сгенерированный book_id

-- RETURNING можно и хорошо использовать при апдейтах.
UPDATE author
SET fullname = 'Walter', rating = 5
WHERE author_id = 1
RETURNING fullname, rating, author_id
-- Также можно написать RETURNING *
UPDATE author
SET fullname = 'Koskin', rating = 11
WHERE author_id = 1
RETURNING *