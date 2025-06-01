# Given a database with (at least) a table "customers" as shown below, write an SQL query that Update in to "customers" table , a customer  named Jozy Altidore ,id 3003, from city Kyiv to city Paris and from grade 500 to grade 300 , salesperson_id 5007  .

# After Update write an SQL query that returns the columns name, city and grade of all customers who live in London or Paris, in ascending order of id.

# First 5 rows of customers table, ordered by id
# id      name             city          grade   salesperson_id
# ------  ---------------  ------------  ------  --------------
# 3001    Brad Guzan       London        100     5005
# 3002    Nick Rimando     New York      100     5001
# 3003    Jozy Altidore    Kyiv          200     5007
# 3004    Fabian Johns     Paris         300     5006
# 3005    Graham Zusi      California    200     5002 

# For example:
# Тест -- Testing with original db
# Result
# name                  city             grade
# --------------------  ---------------  ----------
# Brad Guzan            London           100
# Jozy Altidore         Paris            300
# Fabian Johns          Paris            300
# Julian Green          London           300

# Ми маємо таблицю `customers`, і потрібно зробити два запити:
# 1. **Оновити дані конкретного користувача** (`Jozy Altidore`) — змінити його місто та grade.
# 2. **Вибрати всіх користувачів, які живуть у містах London або Paris**, і показати їх ім’я, місто та grade, впорядкувавши за `id`.

## 🔹 Крок 1: Оновлення користувача `Jozy Altidore`
### Що потрібно зробити:
# * `city` змінити з `Kyiv` на `Paris`
# * `grade` змінити з `200` на `300`
# * `salesperson_id` змінити на `5007` (він і так такий, але для повноти включимо його в `UPDATE`)
# * `id` залишається 3003, тому ми будемо шукати рядок саме за ним

### SQL-запит:
# UPDATE customers
# SET city = 'Paris',
#     grade = 300,
#     salesperson_id = 5007
# WHERE id = 3003;

## 🔹 Крок 2: Вибірка клієнтів з London або Paris
### Що потрібно:
# * Вибрати `name`, `city`, `grade`
# * Лише ті, у кого місто — **London** або **Paris**
# * Відсортувати за `id` у порядку зростання (це важливо для правильного порядку виводу)

### SQL-запит:
# SELECT name, city, grade
# FROM customers
# WHERE city = 'London' OR city = 'Paris'
# ORDER BY id ASC;

## 🔹 Повний код для проходження тесту
Ось обидва запити разом:
# -- Крок 1: Оновлюємо дані користувача Jozy Altidore
UPDATE customers
SET city = 'Paris',
    grade = 300,
    salesperson_id = 5007
WHERE id = 3003;

# -- Крок 2: Отримуємо список клієнтів з London або Paris
SELECT name, city, grade
FROM customers
WHERE city = 'London' OR city = 'Paris'
ORDER BY id ASC;

## 🔍 Що станеться після цього?
Після виконання `UPDATE`, запис для `Jozy Altidore` буде виглядати так:
# id      name             city          grade   salesperson_id
# 3003    Jozy Altidore    Paris         300     5007

# А `SELECT` поверне щось подібне до:
# name                  city             grade
# --------------------  ---------------  ----------
# Brad Guzan            London           100
# Jozy Altidore         Paris            300
# Fabian Johns          Paris            300
# Julian Green          London           300

## ✅ Пояснення простими словами:
# * `UPDATE ... WHERE id = 3003` — ми оновлюємо тільки того клієнта, в кого `id` 3003.
# * `SET` — вказуємо, що саме ми хочемо змінити: місто, рівень (grade), айді продавця.
# * У другому запиті `SELECT ... WHERE city = 'London' OR city = 'Paris'` — фільтруємо клієнтів тільки з цих двох міст.
# * `ORDER BY id ASC` — впорядковуємо за id (щоб збігалося з тестом).
