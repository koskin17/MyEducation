# https://telegra.ph/Skrytye-sokrovishcha-Python-01-12

# 1. Атрибуты функции.
# В функции, как и в классах, можно использовать атрибуты и методы, а потом обращаться к ним через имя функции.
def func(x):
    var = x**2 + x + 1

    if var % 2:
        print("Число было нечётное.")
    else:
        print("Число было чётное.")

    # установка атрибутов в функции
    func.optional_return = var
    func.is_awesome = "Mu func is awesome!"

    return var


y = func(3)
print("В результате работы функции получилось: ", y)
# Получаем атрибуты функции
print("Результат вычисления в функции: ", func.optional_return)
print(func.is_awesome)

# 2. В цикле for можно использовать ветку else
#     При добавлении ветки else в цикл for она будет срабатывать, если в теле цикла не обнаружен оператор break

my_list = ['some', 'list', 'containing', 'five', 'elements']
min_len = 3

for element in my_list:
    if len(element) < min_len:
        print(f'Caught an element shorter than {min_len} letters')
        break
else:
    print(f'All elements at least {min_len} letters long')

# В списке ни один элемент не был короче 3 и оператор break никогда не сработает. Следовательно, else будет
# срабатывать (после выполнения цикла for) и печатать показанный выше вывод.
# Этого можно добиться и с отдельной переменной, которая будет отслеживать появление break.

my_list = ['some', 'list', 'containing', 'five', 'elements']
min_len = 3
no_break = True

for element in my_list:
    if len(element) < min_len:
        print(f'Caught an element shorter than {min_len} letters')
        no_break = False
        break

if no_break:
    print(f'All elements at least {min_len} letters long')


# 3. Методы eval() и exec()
# В Python строка может быть считана как програмный код:
# - eval() используется для вычисления выражений;
# - exec() используется для выполнения операторов.
a = 3

b = eval('a + 2')
print('b =', b)

exec('c = a ** 2')
print('c is', c)

# 5. Ellipsis и placeholder
# Ellipsis или троеточие "..." используется в Python как placeholder или как альтернатива None
# В качестве placeholder, когда код еще не написан, то нужно заполнить какое-то место в программе.
def some_function():
    ...
def another_function():
    pass

# В качестве альтернативы None, если нужно обозначить пустой input или return,
# но ни один из них не подходит
# вычисление nth odd
def nth_odd(n):
    if isinstance(n, int):
        return 2 * n - 1
    else:
        return None

# вычисление исходных данных n в nth odd
def original_num(m=...):
    if m is ...:
        print('This function needs some input')
    elif m is None:
        print('Non integer input provided to nth_odd() function')
    elif isinstance(m, int):
        if m % 2:
            print(f'{m} is {int((m + 1)/2)}th odd number')
        else:
            print(f'{m} is not an odd number')

original_num()

a = nth_odd(n='some string')
original_num(a)

b = nth_odd(5)
original_num(b)

original_num(16)

# Функция nth_odd() вычисляет энное нечетное число.
# Функция original_num() вычисляет исходное число n, учитывая энное нечетное число.
# Здесь None является одним из ожидаемых входных данных функции original_num(),
# поэтому мы не можем использовать его в качестве плейсхолдера по умолчанию для аргумента m.

# Нарезка массива в NumPy
# NumPy использует многоточие для среза массива.
# Следующий код показывает два эквивалентных способа нарезки массива NumPy:
import numpy as np

a = np.arange(16).reshape(2,2,2,2)

print(a[..., 0].flatten())
print(a[:, :, :, 0].flatten())
# Таким образом ... сообщает о наличии стольких ':', сколько необходимо.

