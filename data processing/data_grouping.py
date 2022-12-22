# Группировка данных
import pandas as pd

data = pd.read_csv("https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv",
                   delimiter=";", na_values="NA")
print("Смотрим на данные")
print(data.head())
# Чистим данные от NaN
data.fillna(0, axis=1, inplace=True)
print()
print("Данные после чистки от Nan")
print(data.head())
# Для того чтобы сгруппировать данные, используется метод groupby.
# Он принимает названия столбцов (серий), по значениям которых нужно выполнить группировку.
data_group = data.groupby("AdmArea")
print()
print("Смотрим на объект data_group")
print(data_group)
# Получившийся data_group - не DataFrame, а фрейм группы данных
# Для работы с группой данных нужно применить групповую функцию.
# К примеру функция расчета среднего значения - avg
data_avg = data_group.mean()
print()
print("Теперь смотрим на data_avg")
print(data_avg)
# В результате выводят средние значения по всем значениям
# Если надо среднее значение по конкретной серии данных, то её просто указываем
data_avg_test = data_group.mean()["Calls"]
print("Средние данные по конкретной серии данных:")
print(data_avg_test)
print("Можно посчитать максимальное число вызовов по фрейму группы данных")
print(data_group.max()["Calls"])
# Часто используется показатель общего числа элементов в каждой группе.
# Оно выводится через групповую функцию count()
print()
print("Считаем общее число элементов в каждой группе")
print(data_group.count()["Calls"])

# Важно помнить, что функции min, max, count применяются к группе данных.
# Мы внутри каждой группы получаем соответствующие данные
# Довольно часто приходится суммировать данные
print()
print("Просуммированные данные:")
print(data_group.sum()["Calls"])
print()
print("Выводим первую строку данных в каждой группе данных")
print(data_group.first()["Calls"])
print()
print("Выводим последнюю строку данных в каждой группе данных")
print(data_group.last()["Calls"])
# Использование столбца данных как категории.
# В этом случае данные из серии данных становятся уникальными категориями
data["AdmArea"] = data["AdmArea"].astype("category")
