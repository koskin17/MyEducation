CREATE TABLE customer
(
	customer_id serial,
	full_name text,
	status char DEFAULT 'r', -- Просто придумали, что обычный customet по умолчание обозначается "r", а привелигированный - "p"

	CONSTRAINT PK_customer_customer_id PRIMARY KEY(customer_id),
	CONSTRAINT CHK_customer_status CHECK (status = 'r' OR status = 'p') -- В этом случае идёт проверка status и проверка на обязательное
																		 -- только "r" или только "p"
);

INSERT INTO customer (full_name)
VALUES
('name');

SELECT * FROM customer
-- В результате вставилась строчка с "r" в status по умолчанию и ничего другого в status кроме "r" или "p" не будет.
-- Для удаления этого ограничения применяется процедура
ALTER TABLE customer
ALTER COLUMN status DROP DEFAULT
-- В результате в поле status по умолчанию будет записываться null
INSERT INTO customer (full_name)
VALUES
('name');

SELECT * FROM customer

-- Для добавления ограничения применятся команда
ALTER TABLE customer
ALTER COLUMN status SET DEFAULT 'r'
-- Если теперь вставлять, то уже автоматически по умолчанию дует проставляться 'r'
INSERT INTO customer (full_name)
VALUES
('name');
SELECT * FROM customer