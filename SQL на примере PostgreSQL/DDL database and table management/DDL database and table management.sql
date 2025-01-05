CREATE TABLE student
(
	student_id serial,
	first_name varchar,
	last_name varchar,
	birthday date,
	phone varchar
);

CREATE TABLE cathedra
(
	cathedra_id serial,
	cathedra_name varchar,
	dekan varchar
)

-- Команды изменения таблиц
ALTER TABLE student
ADD COLUMN middle_name varchar;

ALTER TABLE student
ADD COLUMN rating float;

ALTER TABLE student
ADD COLUMN enrolled date;

-- Команды изменения таблиц 2
ALTER TABLE student
DROP COLUMN middle_name

-- Команды изменения таблиц 3
ALTER TABLE cathedra
RENAME TO chair

-- Команды изменения таблиц 4
ALTER TABLE chair
RENAME cathedra_id TO chair_id;

ALTER TABLE chair
RENAME cathedra_name TO chair_name;

-- Команды изменения таблиц 5
ALTER TABLE student
ALTER COLUMN first_name SET DATA TYPE varchar(64);

ALTER TABLE student
ALTER COLUMN last_name SET DATA TYPE varchar(64);

ALTER TABLE student
ALTER COLUMN phone SET DATA TYPE varchar(30);

-- Команды изменения таблиц 6
CREATE TABLE faculty
(
	faculty_id serial,
	faculty_name varchar
);
INSERT INTO faculty (faculty_name)
VALUES
('faculty 1'),
('faculty 2'),
('faculty 3');

SELECT * FROM faculty

TRUNCATE TABLE faculty RESTART IDENTITY --TRUNCATE по умолчанию не перезапускает serial или индекс.
										-- Для рестарта нужно специально прописать TRUNCATE TABLE table_name RESTART IDENTITY

DROP TABLE faculty