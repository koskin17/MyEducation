from tkinter import *

root = Tk()
root.geometry('800x600+350+100')

def add_str():
    t.insert('2.4', 'Hello!')

'''
Если в текстовом поле необходимо удалить
определённоё кол-во символов с конкретного места / символа,
то записывается в кавычках номер позиции 'номер строки.номер позиции',
а потом через запятую в кавычках 'номер строки.до какого символа'
'''
def del_str():
##    t.delete('2.4', '2.10')
    t.delete('1.0', END)

def get_str():
    print(t.get('1.0', END))


f_menu = Frame(root, bg = "#1F252A", height = 40)
f_text = Frame(root)
f_menu.pack(fill = X)
f_text.pack(fill = BOTH, expand = True)

l_menu = Label(f_menu, text = "Menu", bg = "#2B3239",
               fg = "#C6DEC1", font = "Atial 12")
l_menu.place(x = 5, y = 10)

btn_add = Button(root, text = "Add", command = add_str).place(x = 50, y = 10)
btn_del = Button(root, text = "Delete", command = del_str).place(x = 90, y = 10)
btn_get = Button(root, text = "Get", command = get_str).place(x = 140, y = 10)

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
