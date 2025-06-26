from itertools import groupby


data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bod', 'age': 30},
    {'name': 'Charlie', 'age': 25},
    {'name': 'Dave', 'age': 30}
]

# Сначала сортируем по age
sorted_data = sorted(data, key=lambda x: x['age'])

# Потом группируем
groups = groupby(sorted_data, key=lambda x: x['age'])

for age, group in groups:
    print(f"Age: {age}")
    for item in group:
        print(f" - {item['name']}")