-- Последовательности или SEQUENCES
-- Создаём последовательность
CREATE SEQUENCE seq1;
-- Для генерации следующего значения в последовательности вызывается функция nextval
-- и передаётся ей в качестве аргумента имя последовательности
SELECT nextval('seq1');
-- Также есть функция currval, которая также получает имя последовательности, но возвращает текущее значение
SELECT currval('seq1');
-- Есть функция lastval, которая не принимает аргументы (имя последовательности) и возвращающая последнее значение
-- любой из последовательностей, сгенерированной в текущей сессии.
SELECT lastval('seq1');

-- Манипулировать последовательностью можно при помощи функции setval, которая принимает имя последовательности и значение,
-- которое нужно установить.
-- Также есть третий аргумент FALSE или TRUE(по умолчанию)
SELECT setval('seq1', 16, TRUE);
SELECT currval('seq1');
SELECT nextval('seq1');
SELECT currval('seq1');

SELECT setval('seq1', 16, FALSE);
SELECT currval('seq1');
SELECT nextval('seq1');
SELECT currval('seq1');

-- Можно создавать счётчики с разными инкрементами / шагами
CREATE SEQUENCE IF NOT EXISTS seq2 INCREMENT 16;
SELECT nextval('seq2');
-- В результате получаем 17: на старте - 1, плюс (INCREMENT) 16 и тучемфд - 17.

-- Кроме инкремента для последовательности можно задать другие параметры
CREATE SEQUENCE IF NOT EXISTS seq3
INCREMENT 16
MINVALUE 0
MAXVALUE 128
START WITH 0;

SELECT nextval('seq3');

-- Уже имеющийся SEQUENCE можно переименовать
ALTER SEQUENCE seq3 RENAME TO seq4
-- Рестарт последовательности
ALTER SEQUENCE seq4 RESTART WITH 16;
SELECT nextval('seq4')

-- Удалить имеющийся SEQENCE
DROP SEQUENCE seq4;
