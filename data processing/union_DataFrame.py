# Объединение DataFrame
import pandas as pd
# Для вывода графиков нужна библиотека matplotlib
import matplotlib.pyplot as plt

data_2017 = pd.read_csv("https://video.ittensive.com/python-advanced/internet-2017.csv",
                        na_values="NA", decimal=",", skiprows=1, names=["Регион", "2017"], index_col="Регион")
data_2018 = pd.read_csv("https://video.ittensive.com/python-advanced/internet-2018.csv",
                        na_values="NA", decimal=",", skiprows=1, names=["Регион", "2018"], index_col="Регион")
# Смотрим, какие данные в обоих фреймах
print("Данные за 2017 год:")
print(data_2017.head())
print()
print("Данные за 2018 год:")
print(data_2018.head())
# Получаем объединённый набор данных при помощи метода merge(), в который передаются 2 набора данных.
# Важно помнить, что метод merge() может объединять только 2 набора данных.
# Если надо объединить несколько наборов данных, то сначала объединяются попарно, а потом вместе.
# Также указываем, что используется индекс справа и слева.
data = pd.merge(data_2017, data_2018, left_index=True, right_index=True)
print(data)
# Для вывода данных на графике применяем функцию заполнения пустых значений.
data.fillna(0, axis=1, inplace=True)
print()
print("Данные после заполнения пустых значений:")
print(data)
# Выводим среднее значение проникновения интернета по годам в виде линейного графика
data.mean().plot.line()     # Сначала рисуем сам график
plt.show()      # Потом график отображаем
