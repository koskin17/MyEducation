-- Помимо внешних ограничений внешнего ключа есть еще и логические ограничения по условиям.
DROP TABLE IF EXISTS book

CREATE TABLE book
(
	book_id INT,
	title text NOT NULL,
	isbn varchar(32) NOT NULL,
	publisher_id INT,

	CONSTRAINT PK_book_id PRIMARY KEY(book_id)
)

ALTER TABLE book
ADD COLUMN price decimal CONSTRAINT CHK_book_price CHECK(price >= 0)
-- При попытке вставить отрицательное значение выдаётся ошибка из-за нарушения ограничений проверки
INSERT INTO book
VALUES
(1, 'The Diary of a Yoing Girl', 'isbn', 1, -1.5)

INSERT INTO book
VALUES
(1, 'The Diary of a Yoing Girl', 'isbn', 1, 1.5);
SELECT * FROM book

-- Т.е. при помощи CHECK можно прописывать любый условия с операторами AND, OR, накладывать ограничения и т.д.