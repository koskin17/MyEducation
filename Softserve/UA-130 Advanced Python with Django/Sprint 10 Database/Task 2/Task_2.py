# Given a database with (at least) two tables: customers and orders as shown below, write an SQL query that returns the customer name, city and amount for all orders between $100 and $3500 inclusive, grouped by name and ordered by city.

# result for example
# name                  city                  totalSum
# --------------------  --------------------  ---------------
# Graham Zusi           California            261
# Jozy Altidore         Kyiv                  2000.0
# Brad Guzan            London                270.65
# Julian Green          London                250.45
# Nick Rimando          New York              3210.86

# First 5 rows of "customers" table, ordered by id
# id      name             city          grade   salesperson_id
# ------  ---------------  ------------  ------  --------------
# 3001    Brad Guzan       London        100     5005
# 3002    Nick Rimando     New York      100     5001
# 3003    Jozy Altidore    Kyiv          200     5007
# 3004    Fabian Johns     Paris         300     5006
# 3005    Graham Zusi      California    200     5002 

# First 5 rows of "orders" table ordered by order_num
# order_num   amount     date        customer_id  saleperson_id
# ----------  ---------  ----------  -----------  -------------
# 70001       150.5      2022-10-05  3005         5002
# 70002       65.26      2022-10-05  3002         5001
# 70003       2480.4     2022-10-10  3009         5003
# 70004       110.5      2022-08-17  3005         5003
# 70005       2400.6     2022-07-27  3007         5001

# For example:
# Тест	-- Testing with original db
# 
# Result
# name                  city                  totalSum
# --------------------  --------------------  ---------------
# Geoff Cameron         Berlin                2590.9
# Graham Zusi           California            1099.0
# Brad Guzan            London                270.65
# Julian Green          London                250.45
# Brad Davis            New York              2400.6
# Nick Rimando          New York              3210.86
# Fabian Johns          Paris                 1983.43

# ## 🔹 Таблиці:
# 1. **customers**
#    * `id`, `name`, `city`, `grade`, `salesperson_id`
# 2. **orders**
#    * `order_num`, `amount`, `date`, `customer_id`, `saleperson_id`

# ## 🎯 Завдання:
# Написати SQL-запит, який:
# * Вибирає ім’я клієнта (`name`), місто (`city`) і **загальну суму** замовлень (`totalSum`)
# * Враховує **тільки замовлення з сумою від \$100 до \$3500 включно**
# * Групує результат за іменем клієнта
# * Сортує результат за містом (`city`)

# ### 🔸 КРОК 1: З'єднуємо таблиці
# Ми хочемо пов’язати `customers` і `orders`. Вони зв’язані через:
# * `customers.id` = `orders.customer_id`
# Отже, будемо використовувати `JOIN`.

# ### 🔸 КРОК 2: Фільтруємо замовлення
# Нам потрібно врахувати **тільки ті замовлення, де `amount` між 100 і 3500**:
# ```sql
# WHERE o.amount BETWEEN 100 AND 3500
# ```

# ### 🔸 КРОК 3: Групування
# Ми групуємо по клієнту, тому потрібно групувати за `name` і, відповідно, показати `SUM(o.amount)`.

# ### 🔸 КРОК 4: Сортування
# Після групування, сортуємо по `city` у порядку зростання.

# ## ✅ Підсумковий SQL-запит:
# ```sql
# SELECT 
#     customers.name,
#     customers.city,
#     SUM(orders.amount) AS totalSum
# FROM 
#     customers
# JOIN 
#     orders o ON customers.id = orders.customer_id
# WHERE 
#     orders.amount BETWEEN 100 AND 3500
# GROUP BY 
#     customers.name, customers.city
# ORDER BY 
#     customers.city ASC;

# ## 🧠 Простими словами:
# * Ми поєднуємо клієнтів і замовлення по `id`
# * Фільтруємо тільки ті замовлення, де сума від \$100 до \$3500
# * Групуємо по клієнту, щоб порахувати суму всіх його замовлень у цьому діапазоні
# * Виводимо ім’я клієнта, місто і загальну суму замовлень
# * І нарешті — впорядковуємо за містом

# ## 📌 Результат буде виглядати приблизно так:
# | name          | city       | totalSum |
# | ------------- | ---------- | -------- |
# | Brad Guzan    | London     | 270.65   |
# | Julian Green  | London     | 250.45   |
# | Nick Rimando  | New York   | 3210.86  |
# | Jozy Altidore | Kyiv       | 2000.00  |
# | Graham Zusi   | California | 261.00   |

# ## 🧪 Код для проходження тестів (повний блок):
# -- SQL-запит для виводу імені, міста і загальної суми замовлень
SELECT 
    customers.name,
    customers.city,
    SUM(orders.amount) AS totalSum
FROM 
    customers
JOIN 
    orders ON customers.id = orders.customer_id
WHERE 
    orders.amount BETWEEN 100 AND 3500
GROUP BY 
    customers.name, customers.city
ORDER BY 
    customers.city;
