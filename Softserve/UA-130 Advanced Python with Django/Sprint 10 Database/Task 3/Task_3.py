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

## 🐍 **Повний Python-код:**
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
        query = "SELECT * FROM customers WHERE grade > 200 ORDER BY id;"
        cursor.execute(query)

        # Get results
        rows = cursor.fetchall()
        print("Total rows are:  ", len(rows))
        print("Printing each row")

        # Output each line
        for row in rows:
            print(f"Id:  {row[0]}")
            print(f"Name:  {row[1]}")
            print(f"City:  {row[2]}")
            print(f"Grade:  {row[3]}")
            print(f"Seller:  {row[4]}")
            print()  # empry line

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