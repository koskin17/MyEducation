# list.append(x) - Добавляет элемент в конец списка
# list.extend(L) - Расширяет список list, добавляя в конец все элементы списка L
# list.insert(i, x) - Вставляет на i-ый элемент значение x
# list.remove(x) - Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
# list.pop([i]) - Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
# list.index(x, [start [, end]]) - Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
# list.count(x) - Возвращает количество элементов со значением x
# list.sort([key=функция], [reverse=False]) - Сортирует список на основе функции
# list.reverse() - Разворачивает список
# list.copy() - Возвращает копию списка
# list.clear() - Очищает список


print('Замена значения в списке на другое')
m = [[5, 6], [1, 2], ['s', 'f']]
print(m)
m[0] = 9
print(m)
print('')

print('Увеличение первого элемента списка на 2')
m[0] = m[0] + 2
print(m)
print('')

print('Поменяли местами элементы в списке')
m[1], m[2] = m[2], m[1]
print(m)
print('')

print('Добавление к списку элемента "7"')
m = m + [7]
print(m)
print('')

print('Увеличение списка в 2 раза')
m *= 2
print(m)
print('')

print('Создание списка из слова')
n = list('string')
print(n)
print('')

print('Создание списка из сгенерированных значений')
w = list(range(10))
print(w)
print('')

print('Применение к списку цикла For')
for i in w:
    print(i)
print('')

print('Исключение из списка элемента с индексом 8 и выведение списка')
q = []
for i in w:
    if i == 8:
        continue
    q += [i]
else:
    print(q)

print('Метод append: добавляем элемент в список')
x = [9, 8, 7, 6, 5]
print(x)
x.append(4) #метод append добавляет элемент в список
print(x)
print('')

print('Метод insert: вставляем элемент по указанному индексу: в элемент с индексом 1 вставляем 7')
print(x)
x.insert(1, 7)
x.insert(2, 7)
print(x)
print('')

print('Метод count позволяет посчитать конкретный элемент в списке / строке')
print(x)
print('Одинаковых элементов "7" в списке: ', x.count(7))
print('')

print('Метод sort: сортирует список по возрастанию')
print(x)
x.sort()
print(x)
print('')

print('Метод reverse: переварачивает (сортирует в обратном порядке) список в обратную сторону')
print(x)
x.reverse()
print(x)
print('')

'''
Также можно отсортировать список в обратном порядке
при помощи функции sorted с ключём reverse

sorted(arr, reverse = True)
'''

''' Если нужно отсортировать список списков,то:
- для сортировки по длине вложенных списков указынвается ключ key=len: sorted(array_of_arrays, key=len)

print('Метод pop: удаление элемента из списка.')
print('Если номер индекса не указан, то будет удален последний элемент из списка')
print(x)
print(x.pop())
print(x)
print('При этом элемент с конкретным индексом можно не просто удалить из списка, а сохранить его в переменную')
print('Удаляем элемент с индексом 3 и сохраняем его в переменную Y')
print(x)
y = x.pop(3)
print(y)
print(x)
print('')

print('Метод remove удаляет конкретный элемент без указания его индекса и удаляет его только один раз, т.е. только один элемент')
print(x)
print('Удаляем элемент 7')
x.remove(7)
print(x)
print('Если указать элемент, которого нет в списке, то выводится ошибка')
print('')

print('Метод clear полностью очищает список')
print(x)
x.clear()
print(x)
print('')

print('Метод extend позволяет добавить в список, в конец этого списка, значения из другого списка')
print('Список Х на данный момент: ', x)
x.extend(['a', 's', ])
print('Список Х после добавления списка: ', x)
print('')

print('Метод copy позволяет полностью продублировать список')
print('Первоначально список в переменной Х: ', x)
y = x.copy()
print('Добавили переменную Y и в неё скопировали список из переменной Х: ', y)
print('')

print('Формируем последовательность цифр от 0 до 9')
n = list(range(10))
print(n)
m = []
print('Перебираем последовательность при помощи цикла For, проверяем, чтобы элементы не были равны 8 и при помощи функции append создаём новый список')
for i in n:
    if i == 8:
        continue
    m.append(i)

else:
    print(m)
print('')

print('Теперь из имеющейся последовательности цифр создадим список только из четных чисел при помощи оператора остатка при делении')
n = list(range(22))
b = n.copy()    #копируем первоначальный список для его сохранения
b = n[::]       #также весь список можно скопировать при помощь вот такой записи "start (с какого индекса:stop (по какой индекс): step(шаг перебирания индексов"
b1 = n[0::2]    #c такой записью из первоначального списка можно сразу скопировать все нечетные числа потому что индекс начинается с 0, а под 0 у нас 1 и шаг 2. Если начать с 1-го индекса, т.е. с 2, то с шагом 2 мы скопируем все чётные числа
b2 = n[1::2]    #c такой записью из первоначального списка можно сразу скопировать все чётные числа. Если начать с 1-го индекса, т.е. с 2, то с шагом 2 мы скопируем все чётные числа
print(b)
print(b1)
print(b2)
print(n)
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print('Нечётные числа: ', n)
    print('Чётные числа', m)
    print('Первоначальный список', b)
print('')

''' Метод isinstance проверяет соответствие типа элемента указанному

isinstance(1, int)  # True
isinstance('some', str)  # True
isinstance(1.7, float)  # True '''

''' Вывести последние значения из списка можно конструкцией
list[-n:]
