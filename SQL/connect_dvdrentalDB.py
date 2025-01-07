from sqlalchemy import create_engine, text

# Установите параметры подключения
db_url = 'postgresql+psycopg2://postgres:koskin17@localhost:5432/dvdrental_for_data_analysis'

# Создайте объект Engine
engine = create_engine(db_url)

# Определите SQL-запрос
query = text('SELECT * FROM customer LIMIT 10')

# Выполните запрос и получите результаты
with engine.connect() as connection:
    result = connection.execute(query)

    # Выведите результаты
    for row in result:
        print(row)
