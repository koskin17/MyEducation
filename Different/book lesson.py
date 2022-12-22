'''
Упражнения типы данных, значения, переменные, имена
'''
prince = 99
print(prince, type(prince))
print('5', type(5))
print('2.0', type(2.0))
print('При сложении целого числа и числа с плавающей точкой - 5+2.0 - тип данных будет: 5+2.0 = ', 5+2.0, type(5+2.0))


'''
Упражнения числа, строки и булевые переменные
'''
sec_per_minute = 60
min_per_hour = 60
print('В минуте - ', sec_per_minute, ' секунд.')
print('В часе - ', min_per_hour, ' минут')
print('Значит в часе: ', sec_per_minute*min_per_hour, ' секунд.')
seconds_per_hour = sec_per_minute*60
print('Значит в сутках: ', seconds_per_hour*24, ' секунд')
seconds_per_day = sec_per_minute * min_per_hour * 24
print('При делении с плавающей точкой \ получается результат: ', seconds_per_day / seconds_per_hour)
print('При целочисленном делении \\ результат получается: ', seconds_per_day // seconds_per_hour )


'''
Упражнения на оператор if + walrus
'''
secret = 7
guess = 5
if guess < secret:
    print('toolow')
elif guess > secret:
    print('toohigh')
else: ('justright')

'''
Упражнения текстовые строки
'''
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
print(song)
print(song.replace('moray!', 'Moray!'))

'''
Фильтруем список слов только на те,
которые начинаются с большой буквы 
'''
l = ['How', 'are', 'You']
l1 = filter(str.istitle, l)
print(list(l1))

questions = [
"We don't serve strings around here. Are you a string?",
"What is said on Father's Day in the forest?",
"What makes the sound 'Sis! Boom! Bah!'?"
]

answers = [
"An exploding sheep.",
"No, I'm a frayed knot.",
"'Pop!' goes the weasel."
]
for i in range(0, len(questions)):
    print('Q: ', questions[i])
    print('A: ', answers[i])
roast = 'roastbeef'
ham = 'ham'
head = 'head'
clam = 'clam'
print('My kitty cat likes %s' %(roast))
print('My kitty cat likes %s,' %(ham))
print('My kitty cat fell on his %s' %(head))
print('And now thinks he\'s a %s.' %(clam))

salutation = '1'
name = '2'
product = '3'
verbed = '4'
room = '5'
amount = '5.1'
animals = '6'
percent = '7'
spokesman = '8'
job_title = '9'

letter = f"""
Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.
Sincerely,
{spokesman}
{job_title}
"""

print(letter.format())

'''
Циклы While и For
'''
spisok = [3,2,1,0]
for i in range(0, len(spisok)):
    print(spisok[i])

things = ["mozzarella", "cinderella", "salmonella"]
print(things)
things[1] = 'золушка'
things[1] = things[1].capitalize()
print(things)
things[0] = things[0].upper()
print(things[0])
print(things)
things.remove('salmonella')
print(things)

surprise = ["Groucho", "Chico", "Harpo"]
print(surprise)
print(type(surprise))
surprise[2] = surprise[2].lower()
print(surprise[2])

even = [even for even in range(11) if even %2 == 0]
print(even)
print('')


start1 = ["fee", "fie", "foe"]
rhymes = [
("flop", "get a mop"),
("fope", "turn the rope"),
("fa", "get your ma"),
("fudge", "call the judge"),
("fat", "pet the cat"),
("fog", "walk the dog"),
("fun", "say we're done"),
]
start2 = "Someone better"

max_lenght = max(len(start1), len(rhymes), len(start2))
start1 = start1 * max_lenght + start1

for i in range(0, len(rhymes)):
        print(start1[i].capitalize() + '!')
        print(rhymes[i][0].capitalize() + '!')
        print(rhymes[i][1].capitalize() + '!')
print(start2)
print('')

'''
Словари
'''

print('Из двух списков при помощи итерации циклом for\
можно сделать словарь')
d1 = [1,2,3,4,5,6]
print('Изначально списов d1: ', d1)
d2 = ['a','b','c','d','e','f']
print('Изначально список d2', d2)
d3 = []
print('Изначально список d3 - пустой', d3)
for comb in zip(d1, d2):
    d3.append(comb)

print('По завершению цикла for в переменной d3 будут храниться данные с типом данных: ', type(d3))
print('При помощи функции dict их можно представить в виде словаря: ', dict(d3))
print('Однако тип данных в переменной d3 будет оставаться: ', type(d3))
print('Для преобразования типа данных в d3 в тип данных "словарь" необходимо переменной d3 присвоить значение dict(d3).')
d3 = dict(d3)
print('В этом случае в d3 уже будут храниться данные:', d3, 'с типом данных: ', type(d3))
print('Вывести все ключи словаря можно кодом print(d3.keys()):')
print(d3.keys())
print('А список всех значений выводится кодом print(d3.values())')
print(d3.values())
print('Если же нужно вывести весь словарь - ключ+значение, то это делается кодом print(d3.items())')
print(d3.items())
print('')

print('Подсчет кол-ва гласных в слове')
vowels = 'уеэоаыяию'                                                    # создаём переменную с гласными
word = 'привет'                                                         # создаём переменную со словом
vowel_counts = {letter: word.count(letter) for letter in set(word) if letter in vowels}       # создаём словарь с выражением, которое считает кол-во гласных в слове
print('В слове', word, 'есть гласные в таком количестве: ', vowel_counts)                     # печатаем список гласных и их кол-во
print()

print('Создаем французско-английский словарь')
'''Сначала создаём словарь из пар слов'''
e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
print('На французском слово морж или walrus звучик как: ', e2f['walrus'])
print()

print('Создаём новый словарь, в котором:\n'
'- ключами становятся значения из старого словаря;\n'
'- значениями становятся ключи старого словаря')
f2e = {}                                                            # создаём пустой словарь
for item in e2f.items():                                            # делаем цикл перебора for методом item - он возвращает кортежи на каждую пару (ключ, значение)
    f2e[item[1]] = item[0]                                          # из полученного кортежа (ключ, значение) значение по индексу [1] присваиваем ключу в новом словаре.
                                                                    # Это можно сделать просто обратившись к ключу в словаре и если его нет, то он будет создан
                                                                    # ключу, к которому обратились (т.е. он создасться), присваиваем значение по индексу [0] из котрежа
print('Выводим изначальный словарь для примера', e2f)               # выводим изначальный словарь для примера
print('Выводим получившийся словарь', f2e)                          # выводим получившийся словарь
print('Выводим перевод слова chien, обращаясь к новому словарю по ключу', f2e['chien'])             # выводим перевод слова chien, обращаясь к новому словарю по ключу 
print('Меняем тип данных "словарь" на "множество"', set(e2f.keys()))          # меняем тип данных "словарь" на "множество"
print()

print('Делаем многоуровневый словарь')
life = {'animals':
                {'cats':
                        ['Henri', 'Grumpy', 'Lucy'],
                 'octopi':{},
                 'emus':{}},
        'plants':{}, 'other':{}}
print('Получаем все ключи словаря', life.keys())                      # получаем все ключи словаря
print('Получаем все ключи словаря в виде списка', list(life.keys()))                # получаем все ключи словаря в виде списка
print('Получаем все ключи словаря в виде списка', life['animals'].keys())           # получает ключи вложенного словаря, на который ссылает ключ animals
print('Получаем все ключи словаря в виде списка', list(life['animals'].keys()))     # получаем ключи вложенного словаря, на который ссылает ключ animals в виде списка
print('Получаем все ключи словаря в виде списка', life['animals']['cats'])          # получаем значения вложенного словаря cats на который ссылается вложенный словарь animals
print()

print('Формируем множество из цифр(ключей) и их квадратов(значения)')
squares = {}                            # создаём пустой словарь
for i in range(10):                     # заполнять словарь будем цифрами от 0 до 10
    squares[i] = i**2                   # в качестве ключа словаря присваивается значение i, в качестве значения ключа присваивается возведённое в квадрат значение i
print(squares)
print()

print('Формирование множества из нечетных чисел циклом for')
odd = set()
for i in range(10):
    if i %2 == 1:
        odd.add(i)
print(odd)
print()

print('Формирование множества из нечетных чисел методом включения')
odd2 = {number for number in range(10) if i %2==1}
print(odd2)
print()

print('Создаём словарь из двух списков')
per1 = ('optimist', 'pessimist', 'troll')
print('Первый список', per1)
per2 = ('The glass i shalf full', 'The glass is half empty', 'How did you get a glass?')
print('Второй сисок', per2)
dic = {}

for i,y in zip(per1, per2):
    dic[i] = y
print('Получился словарь: ', dic)
print('Тип данных у нового словаря: ', type(dic))
print()

print('Формирование словаря из двух списков методом zip()')
titles=['Creature of Habit','Crewel Fate','Sharks On a Plane']
print('Первый список', titles)
plots=['Anunturns into a monster','A haunted yarn shop','Check your exits']
print('Второй список', plots)
movies = {}
print('Новый словарь изначально пустой', movies)
for i,y in zip(titles, plots):
    movies[i] = y
print('После обработки двух списков циклом for получился слловарь: ', movies)
print('')

print('Функции')
print('Создаём функцию good, которая при вызове формирует список name и возвращает его в качестве результата')
def good():
    name = ['Harry','Ron','Hermione']
    return name
print('Вызываем функцию good внутри оператора print и получаем:', good())
print()


def my_shiny_new_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate() # Сама функция
        print("А я - код, срабатывающий после")
    # Вернём эту функцию
    return the_wrapper_around_the_original_function

# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")

stand_alone_function()
# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
# который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
# готовую к использованию функцию:
stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
stand_alone_function_decorated()

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print("Смотри, что я получил:", arg1, arg2)
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

# Теперь, когда мы вызываем функцию, которую возвращает декоратор, мы вызываем её "обёртку",
# передаём ей аргументы и уже в свою очередь она передаёт их декорируемой функции
@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("Меня зовут", first_name, last_name)
print_full_name("Vasya", "Pupkin")
print()

print('Создаём функцию Декоратор')

print('Cоздаём функцию get_odds(i), которая будет получать в качестве параметра номер элемента и будет выводить этот элемент из списка number')
def get_odds():
    numbers = [number for number in range(10) if number %2 == 1]
    print()
    print('Третий элемент в списке: ', numbers[i])
    print()
                                                                
for i in range(10):
        if i == 3-1:
                get_odds()

                
print('Теперь создадим функцию декоратор, которая будет выполняться до функции get_odds и после неё')
def test(func):
    def wrapper():
        print('Выводится маркет начала работы функции-декоратора: ' + 'start')
        func()
        print('Выводится маркет завершения работы функции-декоратора: ' + 'end')
    return wrapper

print('И вызовем функцию get_odds с применением к ней декоратора')

@test
def get_odds2():
    numbers2 = [number for number in range(10) if number %2 == 1]
    print()
    print('Третий элемент в списке: ', numbers2[i])
    print()
                                                                
for i in range(10):
        if i == 3-1:
                get_odds2()
