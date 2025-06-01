Звісно! Давай розберемо твоє завдання покроково та створимо наочну і зрозумілу програму на Python, яка працює з базою **SQLite** (`q1.db`) та виводить дані з таблиці `customers`.

---

## 🧩 **Що потрібно зробити:**

1. **Підключитися до бази даних `q1.db`**
2. **Вивести повідомлення про успішне підключення**
3. **Виконати SQL-запит: вибрати всі записи з таблиці `customers`, у яких `grade > 200`, впорядкувати за `id`**
4. **Вивести кількість знайдених записів**
5. **Вивести кожен запис у форматі:**

   ```
   Id:  <значення>
   Name:  <значення>
   City:  <значення>
   Grade:  <значення>
   Seller:  <значення>
   ```
6. **Закрити підключення до бази даних**
7. **Вивести повідомлення про закриття з'єднання**

---

## 🔧 Структура таблиці `customers` (за прикладом):

```sql
id INTEGER
name TEXT
city TEXT
grade INTEGER
salesperson_id INTEGER
```

---

## ✅ **SQL-запит** для вибірки:

```sql
SELECT * FROM customers WHERE grade > 200 ORDER BY id;
```

---

## 🐍 **Повний Python-код:**

```python
import sqlite3

def fetch_customers_with_high_grades():
    try:
        # 1. Підключення до бази даних
        connection = sqlite3.connect("q1.db")
        cursor = connection.cursor()
        print("Connected to SQLite")

        # 2. SQL-запит
        query = "SELECT * FROM customers WHERE grade > 200 ORDER BY id;"
        cursor.execute(query)

        # 3. Отримання результатів
        rows = cursor.fetchall()
        print("Total rows are:  ", len(rows))
        print("Printing each row")

        # 4. Вивід кожного рядка у зручному форматі
        for row in rows:
            print(f"Id:  {row[0]}")
            print(f"Name:  {row[1]}")
            print(f"City:  {row[2]}")
            print(f"Grade:  {row[3]}")
            print(f"Seller:  {row[4]}")
            print()  # порожній рядок для кращої читабельності

    except sqlite3.Error as error:
        print("Error while connecting to SQLite", error)

    finally:
        # 5. Закриття підключення
        if connection:
            connection.close()
            print("The SQLite connection is closed")

# Виклик функції
fetch_customers_with_high_grades()
```

---

## 📘 Пояснення простими словами:

* Ми підключаємось до файлу `q1.db` як до звичайного файлу (це особливість SQLite — він не потребує сервера).
* Далі виконуємо `SELECT` з умовою `grade > 200`.
* Зчитуємо всі результати через `fetchall()`.
* Виводимо кількість записів та самі записи.
* І на завершення — обов’язково закриваємо з'єднання.

---

## 📌 Результат при запуску (приклад):

```
Connected to SQLite
Total rows are:   2
Printing each row
Id:  3022
Name:  Nik Rimando
City:  Madrid
Grade:  1000
Seller:  6001

Id:  3025
Name:  Grem Zusisa
City:  USA
Grade:  2000
Seller:  6002

The SQLite connection is closed
```

---

🔔 **Порада:** Перед запуском переконайся, що файл `q1.db` знаходиться у тій самій папці, що й твій скрипт. Якщо ні — вкажи повний шлях до нього.

---

Готовий до запуску 🎯. Якщо хочеш — можу допомогти зробити цей скрипт більш гнучким або дописати обробку помилок для тестування!
