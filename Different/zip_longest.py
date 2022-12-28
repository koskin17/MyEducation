# Функция zip() итерирует последовательность по самой короткой и останавливается.
# Если нужно проитерировать по последовательностям, независимо от длинны, используется zip_longest().
# Значение в более коротких последовательностях будут установлены как None

from itertools import zip_longest

a = [_ for _ in range(5)]
b = [_ for _ in range(10)]
lst = []
for x, y in zip_longest(a, b):
    # Формируем кортеж
    tmp = (x, y)
    lst.append(tmp)

print("Возвращается список кортежей: ", lst)
print()

print("Можно возвращать кортежи со значениями:")
for _ in zip_longest(a, b):
    x, y = _
    print(x, y, ' - ', type(_))
