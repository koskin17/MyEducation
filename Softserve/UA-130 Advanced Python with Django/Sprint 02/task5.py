# As input data you have list of strings with information about some location:

# "id,name,poppulation,is_capital",
# "3024,eu_kyiv,24834,y",
# "3025,eu_volynia,20231,n",
# "3026,eu_galych,23745,n",
# "4892,me_medina,18038,n",
# "4401,af_cairo,18946,y",
# "4700,me_tabriz,13421,n",
# "4899,me_bagdad,22723,y",
# "6600,af_zulu,09720,n"

# Using regular expression write method max_populationulation() for parsing strings and get info about location with highest population 

# For example:

# Тест	Result
# data = ["id,name,poppulation,is_capital",
# "3024,eu_kyiv,24834,y",
# "3025,eu_volynia,20231,n",
# "3026,eu_galych,23745,n",
# "4892,me_medina,18038,n",
# "4401,af_cairo,18946,y",
# "4700,me_tabriz,13421,n",
# "4899,me_bagdad,22723,y",
# "6600,af_zulu,09720,n"]

# print(max_populationulation(data))
# ('eu_kyiv', 24834)

# Вот решение задачи с использованием **регулярного выражения** для извлечения данных и последующего поиска города с наибольшим населением:

import re

def max_population(data):
    # Регулярное выражение для извлечения id, name, population, is_capital
    pattern = r"(\d+),([\w_]+),(\d+),([yn])"

    city = None
    max_population = 0

    # Начинаем обработку данных, пропуская заголовок (data[0])
    for entry in data[1:]:
        match = re.match(pattern, entry)
        if match:
            _, city_name, population, _ = match.groups()
            population = int(population)  # Преобразуем в число
            
            # Проверяем, является ли население самым большим
            if population > max_population:
                max_population = population
                city = city_name

    return (city, max_population) if city else None

# Тестовые примеры:
data = [
    "id,name,poppulation,is_capital",
    "3024,eu_kyiv,24834,y",
    "3025,eu_volynia,20231,n",
    "3026,eu_galych,23745,n",
    "4892,me_medina,18038,n",
    "4401,af_cairo,18946,y",
    "4700,me_tabriz,13421,n",
    "4899,me_bagdad,22723,y",
    "6600,af_zulu,09720,n"
]

print(max_populationulation(data))  # Ожидаемый результат: ('eu_kyiv', 24834)

# ### 🔎 **Как работает код?**
# 1. **Используется регулярное выражение `r"(\d+),([\w_]+),(\d+),([yn])"`**
#    - `(\d+)` → идентификатор (`id`).
#    - `([\w_]+)` → название города (`name`), может содержать `_` (например, `eu_kyiv`).
#    - `(\d+)` → население (`population`), число.
#    - `([yn])` → признак столицы (`y` или `n`).

# 2. **Проходим по строкам (кроме заголовка)** и извлекаем данные с помощью `re.match()`.

# 3. **Определяем город с максимальным населением**, сравнивая текущий `population` с `max_population`.

# 4. **Возвращаем кортеж (`город`, `население`)**, если найден максимум.

# ---

# ### ✅ **Почему этот метод эффективен?**
# ✔ **Использует `re.match()`**, что быстро проверяет структуру строки.  
# ✔ **Работает без дополнительных списков**, сокращая использование памяти.  
# ✔ **Проходит по списку всего один раз** (`O(N)`, где `N` — количество строк).