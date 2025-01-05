-- Показ имён ограничений в таблице
SELECT constraint_name
FROM information_schema.key_column_usage
WHERE table_name = 'chair'
	AND table_schema = 'public'
	AND column_name = 'chair_id'

-- Удалить ограничение
ALTER TABLE chair
DROP CONSTRAINT chair_pkey

-- Добавить ограничение
ALTER TABLE chair
ADD PRIMARY KEY(chair_id)