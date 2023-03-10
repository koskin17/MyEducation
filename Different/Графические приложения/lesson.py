import time

'''
Импортируем  модуль Tkinter.
Просто import tkinter не сработал и модуль не импортировался.
Пришлось импортировать именно from tjinter import *
'''
from tkinter import *

'''
Импортируем специальный модуль, чтобы кнопки отображались так,
как отображаются в операционной системе.
Он импорируется отдельно.
'''
from tkinter import ttk

'''
Создание тестовой функции для кнопки
'''
def clicked():
    print('Clicked!')
'''
Создание объекта класса Tk.
Название root - общепринятое, можно еще называть Window
'''
root = Tk()
'''
Изменение заголовка окна
'''
root.title('Первое приложение')

'''
Изменение логотипа окна.
Указывается путь к файлу. Если он лежит в той же папке, то
достаточно указать только его имя
'''
root.iconbitmap('axor.ico')

'''
Управление местом появления окна и размером окна.
W - ширина окна
H - высота окна
Далее 2 цифры - это координаты появления окна.
Отсчёт от 0 х 0 или верхний левый угол экрана
'''
root.geometry('600x600+400+200')

'''
Если надо, чтобы размеры окна были неизменяемые,
то применяется метод resizebla().
По умолчанию у него изменение размеров по ширине и высоте
установлено как True: resizebla(True, True)
Запрет на изменение делается установкой False
'''
root.resizable(False, False)

'''
Изменение фонового цвета окна.
Метод config с параметров bg (background), которому передаётся
цвет - слово или код цвета
'''
root.config(bg = '#008080')

'''
Для вставки изображения в label сначала необходимо
создать объект из этого изображения
'''
img = PhotoImage(file = 'logo.png')
l_logo = Label(root, image = img)
l_logo.pack()

'''
Создание кнопки.
Сначала кнопку / виджет нужно создать, а потом разместить/.
Команды можно написать одну под другой или сразу:
Button(root, text = 'Кнопка').btn.pack()
Однако иногда при такой записи кнопки могут не работать
При назначении функции ВАЖНО указать имя функции БЕЗ СКОБОК,
чтобы она вызывалась и отрабатывала только при клике по кнопке.
Происходит присваивание COLLABLE функции
'''
btn = Button(root, text = 'Кнопка1', command = clicked) # создание кнопки
btn.pack()                                          # размещение / отображение кнопки

'''
Пример второй кнопки в стиле операционной системы.
'''
btn2 = ttk.Button(root, text = 'Кнопка2', command = clicked)
btn2.pack()

'''
Управление шрифтом
'''
btn3 = Button(root, text = 'Кнопка3', command = clicked,
                  font = "Arial 20 italic")
btn3.pack()

'''
Параметры шрифта можно передавать кортежем.
Это удобно в том случае, если название шрифта состоит из нескольких слов
'''
btn4 = Button(root, text = 'Кнопка4', command = clicked,
                  font = ("Comic Sans MC", 20))
btn4.pack()

'''
Передача опций другими способами.
Это актуально, когда кнопка создана, но в каком-то случае нужно функцией, к примеру,
изменить что-то в самой кнопке и только одно.
Тогда можно напрямую обращаться к её свойствам и менять непосредственно.
'''
btn5 = Button(root, text = 'Кнопка5')
btn5.configure(width = 20, height = 5)
btn5['font'] = "Arial 5"
btn5.pack()

'''
Задача: при клике вывести текущее время на кнопке
'''
def check_time():
    btn_time['text'] = time.strftime('%H:%M:%S')

btn_time = Button(root, text = 'Текущее время', command = check_time)
btn_time.pack()

'''
Задача: посчитать кол-во кликов по кнопке и показ этого кол-ва в тайтле приложения
'''
clicks = 0   # счетчик кликов по кнопке

def counter():
    global clicks   # импортирование переменной из глобальной области видимости.
                    # теперь переменная доступна не только на чтение, но и на запись
    clicks += 1
    root.title(f'Counter: {clicks}')

btn_click = Button(root, text = 'Counter', command = counter)
btn_click.pack()

'''
Виджет Label
Своство justify - это выравнивание строк относительно друг друга.
Свойство anchor - выравнивание всего текста по сторонам света
'''
##l = Label(root, text = 'Текст в стркое 1\nСтрока 2\nСтрока 3\nСтрока 4\nСтрока 5',
##          bg = 'red', fg = '#fff', font = ("Comic Sans MS", 10, "bold"), justify = LEFT,
##          width = 50, height = 10, anchor = SE)
##l.pack()

l = Label(root, text = "Поле ввода") # label для подписи поля ввода
l.pack()                                # размещение label
'''
Если надо что-то написать в поле ввода,
то используется метод insert
'''
e = Entry(root)                         # Поле ввода в окне root
e.insert(0, 'Введите данные: ')
e.pack()                                # размещение поля ввода в окне

'''
Созадние небольшой программы для работы с полем ввода
'''

def add_str():
    '''
    При указании константы END текст добавляется в конец
    '''
    e2.insert(END, 'Hello')

def del_str():
    '''
    Полное удаление текста из поля ввода
    '''
    e2.delete(0, END)

def get_str():
    l_text['text'] = e2.get()

l2 = Label(root, text = "Поле ввода")
l2.pack()

e2 = Entry(root)
'''
У поля entry есть метод show.
Он отвечает за то, как будут отображаться символы, которые вводятся в поле entry/
Это полезно при вводе пароля, например.
Если написать e2 = Entry(root, show = '*'),
то вводимые символы будут отображаться в виде звёздочек.
'''
e2.pack()

btn_add = Button(root, text = "Add", command = add_str).pack()
btn_del = Button(root, text = "Delete", command = del_str).pack()
btn_get = Button(root, text = "Get", command = get_str).pack()

l_text = Label(root)
l_text.pack()
'''
У метода pack есть свойство fill.
Указывается в виде строки - l_text.pack(fill = 'x')
Оно отвечает за то, как будет заполняться 
'''

'''
Отображение окна.
Метод mainloop - это цикл обработки событий окна.
Он постоянно "крутится" в фоне и отлавливает события в окне.
'''
root.mainloop()

