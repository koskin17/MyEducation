from tkinter import *

root = Tk()
root.geometry('800x600+350+100')

'''
Для меню сначала создаётся экземпляр класса Menu в окне root
'''
main_menu = Menu(root)
'''
После этого для окна вызывается метод config
и указывается, что menu - это наше созданное main_menu
'''
root.config(menu = main_menu)

def about_program():
    print('Это программа!')
##'''
##Для добавления элементов в простое однострочное меню
##используется метод add_command и указываются пункты меню
##'''
##main_menu.add_command(label = "File")
##main_menu.add_command(label = "About")

'''
Многострочное меню.
Обязательно надо писать tearoff = 0.
Это метод, который позволяет открепить меню и
переставить окно меню куда угодно на экране в отельно окне.
Бесполезная функция.
'''
file_menu = Menu(main_menu, tearoff = 0)
file_menu.add_command(label = "Открыть")
file_menu.add_command(label = "Сохранить")
file_menu.add_separator()
file_menu.add_command(label = "Выход")
main_menu.add_cascade(label = "Файл", menu = file_menu)

'''
Выпадающее меню
'''
help_menu = Menu(main_menu, tearoff = 0)
help_menu_sub = Menu(help_menu, tearoff = 0)
help_menu_sub.add_command(label = "Онлйан")
help_menu_sub.add_command(label = "Оффлайн")

help_menu.add_cascade(label = "Помощь", menu = help_menu_sub)
help_menu.add_command(label = "О программе", command = about_program)
main_menu.add_cascade(label = "Справка", menu = help_menu)





f_text = Frame(root)
f_text.pack(fill = BOTH, expand = True)


'''
За правильный перенос вводимого текста отвечает атрибут wrap
За цвет курсора отвечает свойство INSERTBACKGROUND
За цвет фона при выделенииотвечает свойство SELECTBACKGROUND
За отступ между строками и абзацами отвечают настройки
- spacing1 - включая отступ для первой строки;
- spacing2 - мжстрочный интервал;
- spacing3 - отступ между абзацами.

Атрибут width устанавливает ширину текстового поля,
при которой будет видел скролл бар.
По умолчанию она равна 80, но изменяем на 10,
чтобы скроллбар всегда был видет справа.


'''

t = Text(f_text, bg = "#fff", fg = "#000",
         font = "Atial 12", padx = 10, pady = 10,
         wrap = WORD, insertbackground = "BLACK",
         selectbackground = "#4E5A65",
         width = 10, spacing3 = 10)
t.pack(fill = BOTH, expand = True, side = LEFT)

scroll = Scrollbar(f_text, command = t.yview)
scroll.pack(fill = Y, side = LEFT)
'''
За скролинг текста отвечает виджет SCROLLBAR.
Для того, чтобы скролл бар применялся именно для текстового
поля используется настройка config с командой yscrollcommand
и указанием настроеного скролла scroll и методом установки set()
'''
t.config(yscrollcommand = scroll.set)
root.mainloop()
