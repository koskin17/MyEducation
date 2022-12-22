import sqlite3

def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] =row[idx]

    return d

'''
Для начала нужно подключиться к Базе Данных.
Если файла с БД нет, то он будет созда.
При подключении к БД сразу нужно прописать функцию
закрытия подключения (последняя строка кода), как с файлами'''
Database = sqlite3.connect('test.sqlite')
Database.row_factory = dict_factory
'''
Для работы с БД нужен метод "курсор"
'''
cursor = Database.cursor()

'''
Для формирования запроса к БД используется метод execute.
В данном случае создаётся таблица и в ней определяются поля.
Запрос IF EXISTS создан для того, чтобы избежать создания
таблицы, которая уже есть в БД.
'''
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE)''')

'''
Создание запрос на добавление информации в таблицу БД.
Поля имена полей, в которые добавляется информация,
указывать обязательно.
'''
##cursor.execute("INSERT INTO users (name, email) VALUES ('Иванов Иван', 'ivanov@gmail.com')")

'''
Метод EXECUTE как-бы готовит данные для вставки, а метод COMMIT уже вставляет эти данные.
Выполняется метод COMMIT обращением к соединению, а не к курсору
'''
##Database.commit()

##cursor.execute("INSERT INTO users (name, email) VALUES ('Петров Петр', 'petrov@gmail.com')")

##cursor.execute("INSERT INTO users (name, email) VALUES ('Сидоров', 'sidorov@gmail.com')")
##cursor.execute("INSERT INTO users (name, email) VALUES ('Я я', 'ya@gmail.com')")
##cursor.execute("INSERT INTO users (name, email) VALUES ('Пупкин Вася', 'pupkin@gmail.com')")

'''
Для одновременного добавления нескольких записей в MySQLLite используется метод
executescript.
Прописываются в 2 или более строки команды и они должны быть разделены точкой с запятой ";"
'''

##cursor.executescript('''
##                    INSERT INTO users (name, email) VALUES ('John Doe', 'doe@gmail.com');
##                    INSERT INTO users (name, email) VALUES ('Nick Sand', 'sand@gmail.com');
##                        ''')

'''
Вставка данных в БД.
Для вставки данных в БД используется метод executemany().
Прописывается строка запроса, но в качестве VALUES ставятся знаки вопроса "?",
а вторым параметров указывается последовательность.
В данном случае это список кортежей users.
'''
##users = [('User 1', 'user1@gmail.com'),
##         ('User 2', 'user2@gmail.com'),
##         ('User 3', 'user3@gmail.com')
##         ]
##cursor.executemany(''' INSERT INTO users (name, email) VALUES (?, ?)''', users)
##
##Database.commit()
'''
Извлечение данных из БД
Для извлечения данных исползуется команда SELECT.
Далее перечисляютя поля, которые хотим получить: SELECT name, email и т.д.
Можно использовать звездочку - "*", но это плохая практика и рекомендуется именно
перечислять поля.
Далее указываеться откуда: ...FROM users. Если оставить вот так, то выбирутся все данные.
Если же написать ... WHERE email = ...

Для чтения данных из БД не нужно использовать метод commit - выполнение.
Применяется метод fetchone (возвращает одну запись) или fetchall (возвращает все записи).
'''
##email = 'petrov@gmail.com'
##cursor.execute(f"SELECT * FROM users WHERE email = '{email}'") # так делать не следует, но можно
##res = cursor.fetchone()
##print(res)

'''
Мы получаем кортеж и значит к элементам можем обратиться по индексу
'''
##print(res[1])
##print()

'''
Рекомендуется использовать следующий способ.
При этом ВАЖНО помнить, что из БД вытаскиваются кортежи, т.е. PYTHON ждёт, что в скобках будет кортеж.
Если просто написать одно значение в скобках, то оно принимает тип данных - строка str.
Если же после значения поставить запятую, то тип данных станет кортеж - tuple.
'''
##cursor.execute("SELECT * FROM users WHERE email = ?", (email, ))
##res = cursor.fetchone()
##print(res)
##print()

'''
Также можно использовать список и тогда, без запятой, мы получил нужный кортеж.
'''
##cursor.execute("SELECT * FROM users WHERE email = ?", [email])
##res = cursor.fetchone()
##print(res)
##print()

'''
Если же надо выбрать данные из БД по нескольким полям, то в запросе прописывается OR.
В этом случае, если email не найдёт, то, к примеру, выведятся данные по имени
'''
##email = 'petrov2@gmail.com'
##cursor.execute("SELECT * FROM users WHERE email = ? OR name = ?", (email, 'User 1'))
##res = cursor.fetchone()
##print(res)
##print()

'''
Также можно использовать именованые аргументы.
Тогда параметры указываются в виде словаря
'''
##email = 'petrov2@gmail.com'
##cursor.execute("SELECT * FROM users WHERE email = :email OR name = :name", {'email': email, 'name': 'User 2'})
##res = cursor.fetchone()
##print(res)
##print()

'''
Пользовательские данные или полученные от пользователя данные
НИКОГДА НЕ ПОДСТАВЛЯТЬ в текст запроса.
'''

'''
Выборка всех данных из БД
В этом случае мы получаем СПИСОК КОРТЕЖЕЙ
'''
##cursor.execute("SELECT * FROM users")
##res = cursor.fetchall()
##print(res)
##print()

'''
Для красивой печати можно использовать что-то в стиле...
'''
##for user in res:
##    print(user[1], user[2])

'''
Получение данных из БД в виде словаря.
Для этого создаётся функция, которая сейчас описана на самом верху.
Также сразу после соединения добавляется строчка
Database.row_factory = dict_factory, где Database - имя переменной, в которой установлено соединение
После этого выполняется ниже приведеный код...
И мы получаем данные в виде словаря.
'''

cursor.execute("SELECT * FROM users")
res = cursor.fetchall()
print(res)

'''
Для красивой печати запускается цикл...
'''
for user in res:
    print(user['name'], user['email'])
    
Database.close()
