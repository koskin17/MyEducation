/* E:\Python\MyPython\Обучение\SQL>sqlite3 employees_db.db

CREATE TABLE students(
	first_name TEXT,
	last_name TEXT,
	age INTEGER
);

CREATE TABLE employees(
	first_name TEXT,
	last_name TEXT,
	age INTEGER
);

# Выбрать все данные из таблицы
SELECT * FROM students;

# Вставить данные в таблицу: указывается таблица, имена столбцов, значения
INSERT INTO students (first_name, last_name, age) VALUES ("Jack", "White", 18
);
INSERT INTO students (first_name, last_name, age) VALUES ("Jane", "Black", 19
);

Для чтения данных их файла используется команда .read и указание имени файла
.read sql_syntax_basics.sql */

INSERT INTO employees (first_name, last_name, age) VALUES ("Jack", "White", 18
);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jim", "Brown", 19
);
INSERT INTO employees (first_name, last_name, age) VALUES ("Janet", "Rose", 20
);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jane", "Black", 21
);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jack", "White", 18
);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jim", "Brown", 19
);
INSERT INTO employees (first_name, last_name, age) VALUES ("Janet", "Rose", 20
);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jane", "Black", 21
);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jack", "White", 18
);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jim", "Brown", 19
);
INSERT INTO employees (first_name, last_name, age) VALUES ("Janet", "Rose", 20
);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jane", "Black", 21
);

/* INSERT INTO - одна из CRUD операций. CRUD - аббревиатура от Create, Read, Update, Delete
В данном случае команда INSERT INTO - это команда Create.
Командан SELECT - это команда Read */

SELECT first_name FROM employees;
SELECT first_name, age FROM employees;

/* Выбор всех работников с именем Jack */
SELECT * FROM employees WHERE first_name = "Jack";

/*Также выбор с условием можно записать через IS*/
SELECT * FROM employees WHERE first_name IS "Jack";

/*Выбор с условием по возрасту*/
SELECT * FROM employees WHERE age IS "19";

/* Примеры условий
SELECT first_name, age FROM employees WHERE first_name = "Jack";
SELECT first_name, age FROM employees WHERE first_name IS "Jack";
SELECT first_name, age FROM employees WHERE age IS 19;
SELECT last_name, age FROM employees WHERE last_name IS NOT "Black";
SELECT last_name, age FROM employees WHERE last_name IS NOT "Black" AND age IS NOT 17;
SELECT last_name, age FROM employees WHERE age < 18;

Знак % означает, что после или перед буквами могут идти любые символы в любом кол-ве.
Также указывается слово LIKE
SELECT first_name, age FROM employees WHERE first_name LIKE "Ja%";
SELECT * FROM employees WHERE first_name LIKE "%ck" OR last_name LIKE "%ck";
SELECT * FROM employees WHERE first_name LIKE "%an%"; */
