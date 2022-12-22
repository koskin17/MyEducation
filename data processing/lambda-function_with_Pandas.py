import pandas as pd

# К примеру, у нас есть функция
# def sum_2(x, y):
#     return x + y
#
# # Её можно вызвать, например, через print()
# print(sum_2(2, 3))
# Теперь определим функцию через lambda-выражение
sum_2 = lambda x, y: x + y
# Сейчас sum_2 определена как лямбда-функция и её
# можно вызывать от любых значений
print(sum_2(3, 4))
# Также лямбда-функция может вызываться с аргументами
# по умолчанию
sum_3 = lambda x=3, y=5: x + y
print("Вызов функции без аргументов: ", sum_3())
print("Вызов функции с одним аргументом: ", sum_3(2))
print("Вызов функции с одним аргументом, равным 0: ", sum_3(0, 10))

data = pd.read_csv("https://video.ittensive.com/python-advanced/internet-2017.csv",
                   na_values="NA", names=["Регион", "2017"], decimal=",", skiprows=1, index_col="Регион")
data.fillna(0, axis=1, inplace=True)
print()
print("Данные до преобразования", data["2017"])
# Теперь к серии данных "2017" применим лямбда-функцию через метод apply.
# Это наиболее используемый способ - применение лямбда-функции к данным при их приобразовании
data["2017"] = data["2017"].apply(lambda x: int(x // 10))
print()
print("Данные после преобразования", data["2017"])


# Если мы хотим выделить БЕЛГОРОДСКАЯ ОБЛ. и пропуск интернета большой, то лучше сделать отдельную функцию
# x[0] - это значение региона
def findMoscow(x):
    if x[0].find("БЕЛГОРОДСКАЯ ОБЛ.") > -1:
        return x[1] * 5
    else:
        return x[1]


# Для применения функции findMosсow нужно удалить индекс
data = pd.read_csv("https://video.ittensive.com/python-advanced/internet-2017.csv",
                   na_values="NA", names=["Регион", "2017"], decimal=",", skiprows=1)
# Также нужно, чтобы функция применялась построчно
data["2017"] = data.apply(findMoscow, axis=1)
print()
print("Отбор региона и умножение значения на 5:")
print(data)


# Мы видимо, что по БЕЛГОРОДСКАЯ ОБЛ. данные увеличились в 5 раз
# Теперь изменим целиком всю строчку или переписать весь DataFrame методом apply
# Нужен дополнительный параметр result_type="expand", что значит, что мы расширяем все результаты
# на всю строку данных.
# Также в функции мы должны изменить возвращаемое значение на набор, который должен заменить
# нашу строчку данных
def findMoscow2(x):
    if x[0].find("БЕЛГОРОДСКАЯ ОБЛ.") > -1:
        return [x[0], x[1] * 5]
    else:
        return x


data = pd.read_csv("https://video.ittensive.com/python-advanced/internet-2017.csv",
                   na_values="NA", names=["Регион", "2017"], decimal=",", skiprows=1)
data = data.apply(findMoscow2, axis=1, result_type="expand")
print()
print("Отбор региона и умножение значения на 5 (вторая попытка):")
print(data)
