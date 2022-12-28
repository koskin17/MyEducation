# https://telegra.ph/Vsyo-o-sortirovke-v-Python-ischerpyvayushchij-gajd-11-30

# Метод .sort() применим только к спискам.
# Он изменяет первоначальный список и возвращает None.
# Метод sorted() применим ко всем итерируемым объектам и он возвращает новый отсортированный список.
str1 = "Kostia"
lst1 = list(str1)
print(f"Первоначальный список 1: {lst1}")
lst1.sort()
print(f"Отсортированный список 1 методом .sort(): {lst1}")
str2 = "Kostia"
lst2 = list(str2)
print(f"Первоначальный список 2: {lst2}")
print(f"Отсортированный методом sorted(): {sorted(lst2)}")

# При сортировке метода .sort() и sorted() можно использовать ключи - параметр key - функцию,
# которая будет выполняться для каждого элемента.
# Пример - регистронезависимое сравнение строк:
print(sorted("This is a test string from Andrew".split(),
             key=str.lower))  # ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

# Сортировка сложных объектов по индексу:
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print("Сортировка по индексу (возрасту): ",
      sorted(student_tuples, key=lambda student: student[2]))  # сортируем по возрасту


# Также метод работает с именованными атрибутами:
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def weighted_grade(self):
        return 'CBA'.index(self.grade) / self.age


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print("Сортировка по индексу (возрасту) сложным объектов: ",
      sorted(student_objects, key=lambda student: student.age))  # сортируем по возрасту

# Для простоты сортировки есть специальные методы: itemgetter(), attrgetter() и methodcaller()
from operator import itemgetter, attrgetter, methodcaller

print("Сортировка методом itemgetter() по индексу признака: ",
      sorted(student_tuples, key=itemgetter(2)))  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print("Сортировка методом attrgetter() по названию атрибута: ", sorted(student_objects, key=attrgetter('age')))

# Функции сортировки operator дают возможность сортировать по нескольким признакам / уровням.
# Сортировка по оценке, а потом по возрасту:
print("Сортировка по оценке и возрасту кортежа методом itemgetter(): ", sorted(student_tuples, key=itemgetter(1, 2)))
print("Сортировка по оценке и возрасту кортежа методом attrgetter(): ",
      sorted(student_objects, key=attrgetter('grade', 'age')))

# Метод methodcaller() можно использовать для сортировки по взвешенной оценке, которая считается в методе класса Student
print("Сортировка методом methodcaller() по средневзвешенной оценке: ", [(student.name, student.weighted_grade()) for
                                                                         student in student_objects])
print("Сортировка методом methodcaller(), передаваемого в качестве key: ",
      sorted(student_objects, key=methodcaller('weighted_grade')))

print("Сортировка списка по возрастанию и по убыванию параметром reverse:")
print(sorted(student_tuples, key=itemgetter(2), reverse=True))
print(sorted(student_objects, key=attrgetter('age'), reverse=True))
print()

# Если у записей одинаковые ключи, то их порядок сохраняется
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print("Первоначальный список: ", data)
print("Отсортированный методом sorted() с сохранением порядка записей с одинаковыми ключами: ",
      sorted(data, key=itemgetter(0)))
print()

# Сортировка учеников сначала по возрасту в порядке возрастания,
# а затем по оценкам в убывающем порядке.
s = sorted(student_objects, key=attrgetter('age'))  # сортировка по первичному ключу
print("Список. отсортированный сначала по возврасту (первичный признак),"
      "а потом по оценке (вторичный признак): ",
      sorted(s, key=attrgetter('grade'), reverse=True))  # сортировка по вторичному ключу
print()

# Декорируем-сортируем-раздекорируем
print("Первоначальный список: ", student_objects)
# 1. Декорируем
# Сначала исходный список пополняется новыми значениями, контролирующими порядок сортировки.
# Добавляем i в качестве параметра для сортировки:
decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
print("Получился декорированный список с добавленным значением: ", decorated)
# 2. Сортируем декорированный список методом sort(), который меняет первоначальный список
decorated.sort()
# 3. Убираем добавленный значения и получаем первоначальный отсортированный список.
print("Первоначальный, но отсортированный и очищенный список: ", [student for grade, i, student in decorated])

# Кортежи сравниваются лексикографически, т.е. сравниваются первые элементы, а если они совпадают,
# то сравниваются вторые и так далее.#
# Не всегда обязательно включать индекс в декорируемый список, но у него есть преимущества:
# 1. Сортировка стабильна — если у двух элементов одинаковый ключ, то их порядок не изменится.
# 2. У исходных элементов необязательно должна быть возможность сравнения,
# так как порядок декорированных кортежей будет определяться максимум по первым двум элементам.
# Например, исходный список может содержать комплексные числа, которые нельзя сравнивать напрямую.
# 3. Ещё эта идиома называется преобразованием Шварца в честь Рэндела Шварца,
# который популяризировал её среди Perl-программистов.
# Для больших списков и версий Python ниже 2.4, «декорируем-сортируем-раздекорируем» будет
# оптимальным способом сортировки. Для версий 2.4+ ту же функциональность предоставляют функции-ключи.

# Использование параметра cmp
"""Все версии Python 2.x поддерживали параметр cmp для обработки пользовательских функций сравнения.
В Python 3.0 от этого параметра полностью избавились. В Python 2.x в sort() можно было передать функцию,
которая использовалась бы для сравнения элементов.
Она должна принимать два аргумента и возвращать отрицательное значение для случая «меньше чем»,
положительное — для «больше чем» и ноль, если они равны:

>>> def numeric_compare(x, y):
        return x - y
>>> sorted([5, 2, 4, 1, 3], cmp=numeric_compare)
[1, 2, 3, 4, 5]


Можно сравнивать в обратном порядке:

>>> def reverse_numeric(x, y):
        return y - x
>>> sorted([5, 2, 4, 1, 3], cmp=reverse_numeric)
[5, 4, 3, 2, 1]


При портировании кода с версии 2.x на 3.x может возникнуть ситуация,
когда нужно преобразовать пользовательскую функцию для сравнения в функцию-ключ.
Следующая обёртка упрощает эту задачу:

def cmp_to_key(mycmp):
    'Перевести cmp=функция в key=функция'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


Чтобы произвести преобразование, оберните старую функцию:

>>> sorted([5, 2, 4, 1, 3], key=cmp_to_key(reverse_numeric))
[5, 4, 3, 2, 1]


В Python 2.7 функция cmp_to_key() была добавлена в модуль functools."""
