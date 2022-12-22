'''
Распечатать каждую букву строки методом рекурсии
'''
text = ('Распечатать каждую букву строки методом рекурсии')

def recurs_print(text):         # создаё функцию с рекурсией
    if not text:                # проверяем, есть ли текст в переданной переменной text. Это является частным случаем рекурсивной функции
        return                  # если строка пустая, то функция завершает свою работу путём возвращения пустого return  
    first_letter = text[0]      # присваиваем переменной первый символ строки. И это действие будет циклически повторяться, но с другим, следующим, индексом следующего символа
    print(first_letter)         # выводим переменную с первым символом строки 
    recurs_print(text[1:])      # в этой строке начинается рекурсия. Вызываем функцию внутри себя, но применяем её для текста со второго символа, ведь первый мы уже вывели на экран
        
recurs_print(text)              # вызываем в программе функцию с рекурсией

'''
Выводим все четные числа из списка чисел от 0 до 5
'''
num_list = range(0, 5)

def recurs_find_even(num_list, result = []):    
    if not num_list:
        return
    else:
        element = num_list[0]
        if element % 2 == 0:
            result.append(element)
        recurs_find_even(num_list[1:])
        return result

print(recurs_find_even(num_list))

'''
Поиск значения в словаре с любым кол-вом вложенных словарей
'''
def recurs_find_key(key, obj):
    if key in obj:
        return obj[key]
    for k, v in obj.item():
        if type(v) == dict:
            result = recurs_find_key(key, v)
            if result is not None:
                return result
'''
Рекурсивная функция - возвращает сумму чисел во входящем наборе
'''
def CalcSumNumbers(A):
    if A == []:
        return 0                        # если набор пуст, возвратить 0
    else:
        summ = CalcSumNumbers(A[1:])    # Вычислить сумму - прибавить первый элемент набора. Рекурсивный вызов этой же функции
        summ = summ + A[0]              # Прибавить к общей сумме первый элемент
        return summ

'''
Демонстрация использования функции CalcSumNumbers()
'''

L = [ 2, 3, 8, 11, 4, 6 ]   # 1. Создать набор чисел
summ = CalcSumNumbers(L)    # 2. Вызвать функцию
print("summ = ", summ)      # 3. Распечатать суммуРезультат выполнения программы summ = 34


'''
Рекурсивная функция - возвращает количество отрицательных чисел в списке
'''

def CalcSumNegativeNumbers(A):
    if A == []:
        return 0                                # если набор пуст, вернуть 0
    else:
        count = CalcSumNegativeNumbers(A[1:])   # Вычислить количество, перейти к дальнейшей обработке и без без первого элемента. Рекурсивный вызов этой же функции
        if A[0]<0:                              # Увеличить на 1 при условии, что текущее число отрицательно
            count = count + 1
        return count

'''
Демонстрация использования функции CalcSumNumbers()
'''
L = [ -2, 3, 8, -11, -4, 6 ]                    # 1. Создать набор чисел
n = CalcSumNegativeNumbers(L)                   # 2. Вызвать функцию
print("n = ", n)                                # 3. Распечатать сумму. Результат выполнения программы n = 3

print('Увеличение списка на 2 циклом for')
print('')
number = list(range (0, 10))
print('Изначальный список', number)
new_list = []
for i in number:
    new_number = number[i] * 2
    new_list.append(new_number)
    
print('Список после увеличения на 2: ', new_list)
print('')

print('Увеличение списка на 2 функцией')
print('')
number = range (0, 10)
print('Изначальный список', list(range (0, 10)))
new_list = []
def for_number(number):
    for i in number:
        new_number = number[i] * 2
        new_list.append(new_number)
    return new_list

print('Список после увеличения на 2: ', for_number(number))
print('')

print('Увеличение списка на 2 рекурсией')
print('')
number = range (0, 10)
print('Изначальный список', list(number))
new_list = []
def for_number(number):
    if not number:
        return
    else:
        new_number = number[0] * 2
        new_list.append(new_number)
        for_number(number[1:])
        return new_list
print(for_number(number))
