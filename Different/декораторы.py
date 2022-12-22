text = input()


def uppercase_decorator(func):
    def wrapper(text):
        return func(text).upper()

    return wrapper


@uppercase_decorator
def display_text(text):
    return (text)


print(display_text(text))

print('Создаём функцию good, которая при вызове формирует список name и возвращает его в качестве результата')


def good():
    name = ['Harry', 'Ron', 'Hermione']
    return name


print('Вызываем функцию good внутри оператора print и получаем:', good())
print()


def my_shiny_new_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate()  # Сама функция
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

print(
    'Cоздаём функцию get_odds(i), которая будет получать в качестве параметра номер элемента и будет выводить этот элемент из списка number')


def get_odds():
    numbers = [number for number in range(10) if number % 2 == 1]
    print()
    print('Третий элемент в списке: ', numbers[i])
    print()


for i in range(10):
    if i == 3 - 1:
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
    numbers2 = [number for number in range(10) if number % 2 == 1]
    print()
    print('Третий элемент в списке: ', numbers2[i])
    print()


for i in range(10):
    if i == 3 - 1:
        get_odds2()

'''
https://pythonworld.ru/osnovy/dekoratory.html
'''
