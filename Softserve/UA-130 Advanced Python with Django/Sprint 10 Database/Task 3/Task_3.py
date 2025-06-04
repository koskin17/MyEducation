# Create a Python program to use the sqlite database named "q1.db". The query to the database should display information, as shown in the example below, including phrases: about the successful connection, the total number of records, the actual records, the record of closing the database. From the table of "customers" to deduce all records for which in a "grade" field of value more than 200 with sort ordering on id

# For example output:
# Connected to SQLite
# Total rows are:   2
# Printing each row
# Id:  3022
# Name:  Nik Rimando
# City:  Madrid
# Grade:  1000
# Seller:  6001

# Id:  3025
# Name:  Grem Zusisa
# City:  USA
# Grade:  2000
# Seller:  6002

# The SQLite connection is closed

## 🧩 **Що потрібно зробити:**
# 1. **Підключитися до бази даних `q1.db`**
# 2. **Вивести повідомлення про успішне підключення**
# 3. **Виконати SQL-запит: вибрати всі записи з таблиці `customers`, у яких `grade > 200`, впорядкувати за `id`**
# 4. **Вивести кількість знайдених записів**
# 5. **Вивести кожен запис у форматі:**
#    Id:  <значення>
#    Name:  <значення>
#    City:  <значення>
#    Grade:  <значення>
#    Seller:  <значення>
#    ```
# 6. **Закрити підключення до бази даних**
# 7. **Вивести повідомлення про закриття з'єднання**

## 🔧 Структура таблиці `customers` (за прикладом):
# id INTEGER
# name TEXT
# city TEXT
# grade INTEGER
# salesperson_id INTEGER

## ✅ **SQL-запит** для вибірки:
# ```sql
# SELECT * FROM customers WHERE grade > 200 ORDER BY id;
# ```

import sqlite3
from pathlib import Path

def getting_customers_on_condition():
    db_path = Path(__file__).parent / "q1.db"  # Get the current folder of python-script for conection to database

    try:
        # connect to DB
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        print("Connected to SQLite")

        # make SQL-query on condition
        query = """
                SELECT * FROM customers
                WHERE grade > 200
                ORDER BY id;
                """
        cursor.execute(query)

        # Get results
        rows = cursor.fetchall()

        # ### `fetchall()` — це метод, який використовується після SQL-запиту, щоб **отримати всі результати** з бази даних у вигляді **списку рядків (list of tuples)**.
        # ## 📦 Як це працює:
        # ### Уявімо:
        # Ти зробив SQL-запит, наприклад:
        # ```python
        # cursor.execute("SELECT * FROM customers WHERE grade > 200")
        # ```
        # Тепер у курсорі (`cursor`) зберігаються всі записи, які відповідають умові.
        # ### І тоді:
        # ```python
        # rows = cursor.fetchall()
        # ```
        # — означає: «Візьми **всі записи** з результату цього запиту та збережи їх у змінну `rows` у вигляді списку кортежів».
        # ---
        # ## ✅ Приклад:
        # ### Таблиця:
        # | id | name  | grade |
        # | -- | ----- | ----- |
        # | 1  | Alice | 300   |
        # | 2  | Bob   | 250   |
        # ```python
        # cursor.execute("SELECT id, name, grade FROM customers WHERE grade > 200")
        # rows = cursor.fetchall()
        # ```
        # Тепер `rows` буде:
        # ```python
        # [
        #     (1, 'Alice', 300),
        #     (2, 'Bob', 250)
        # ]
        # ```
        # Кожен запис — це **кортеж (tuple)**.
        # ---
        # ## 🔁 Що можна зробити з цими даними:
        # ```python
        # for row in rows:
        #     print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}")
        # ```
        # ---
        # ## 📌 Що потрібно пам’ятати:
        # | Особливість       | Опис                                           |
        # | ----------------- | ---------------------------------------------- |
        # | `fetchall()`      | Повертає **всі записи** як список кортежів     |
        # | Після `execute()` | Використовується, щоб зчитати результат запиту |
        # | Якщо нічого нема  | Повертає **порожній список** (`[]`)            |
        # ---
        # ## 🧠 Для порівняння:
        # * `fetchone()` — повертає **тільки перший** рядок результату
        # * `fetchmany(n)` — повертає **перші `n` рядків**
        # ---
        # ## 🎯 У реальному житті:
        # Коли ти робиш `fetchall()`, у пам’ять завантажуються всі результати. Це ок, якщо рядків не надто багато. Якщо ти очікуєш **тисячі або мільйони записів** — краще використовувати `fetchone()` або обробляти курсор поступово (ітерувати по ньому).
        # ---
        # Ти ставиш правильні запитання! Без розуміння `fetchall()` не обійтись при роботі з базами 💡
        # Хочеш, можу зробити маленький демонстраційний приклад із `sqlite3`, щоб потренуватись?
        print("Total rows are:  ", len(rows))
        print("Printing each row")
        # Output each line
        for row in rows:
            print(f"Id:  {row[0]}")
            print(f"Name:  {row[1]}")
            print(f"City:  {row[2]}")
            print(f"Grade:  {row[3]}")
            print(f"Seller:  {row[4]}")
            print()  # empty line
    except sqlite3.Error as error:
        print("Error while connecting to SQLite", error)
    finally:
        # Close the connection
        if connection:
            connection.close()
            print("The SQLite connection is closed")

getting_customers_on_condition()

## 📘 Пояснення простими словами:
# * Ми підключаємось до файлу `q1.db` як до звичайного файлу (це особливість SQLite — він не потребує сервера).
# * Далі виконуємо `SELECT` з умовою `grade > 200`.
# * Зчитуємо всі результати через `fetchall()`.
# * Виводимо кількість записів та самі записи.
# * І на завершення — обов’язково закриваємо з'єднання.

## 📌 Результат при запуску (приклад):
# Connected to SQLite
# Total rows are:   2
# Printing each row
# Id:  3022
# Name:  Nik Rimando
# City:  Madrid
# Grade:  1000
# Seller:  6001

# Id:  3025
# Name:  Grem Zusisa
# City:  USA
# Grade:  2000
# Seller:  6002

# The SQLite connection is closed