INSERT INTO author
VALUES ('10', 'John Silver', 4.5);

SELECT * FROM author

-- Если же мы хотим вставить данные лишь частично, то нам обязательно!!! после имени таблицы в скобках указать имена столбцов,
-- в которые ставляем
INSERT INTO author(author_id, fullname)
VAlUES (11, 'Bob Gray')

-- Синтаксис INSERT для создания таблицы на основании выборки
SELECT *
INTO best_authors
FROM author
WHERE rating > 4.5;
-- Т.е. мы указывае ЧТО вставлять, КУДА вставлять и потом условие

SELECT * FROM best_authors
-- Но тут важно помнить, что дополнить эту табличку, когда она уже существует нельзя!

-- Если мы хотим выбрать данные из таблицы и потом их вставить в другу таблицу, то делается это так:
INSERT INTO best_authors
SELECT * FROM author
WHERE rating = 4.5

SELECT * FROM best_authors
-- Т.е. мы сначала указываем КУДА вставлять, потом ЧТО вставлять и условие
