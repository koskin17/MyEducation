from tkinter import *

'''
#ff0000: Красный
#ff7d00: Оранжевый
#ffff00: Желтый
#00ff00: Зеленый
#007dff: Голубой
#0000ff: Синий
#7d00ff: Фиолетовый
'''

def get_color(text_color, hex_color):
    l['text'] = text_color
    e.delete(0, END)
    e.insert(0, hex_color)
    
root = Tk()

l = Label(root)
e = Entry(root, width = 30, justify = 'center')
l.pack()
e.pack()

btn_red = Button(root, bg = "#ff0000", command = lambda: get_color('Красный', '#ff0000'))
btn_red.pack(fill = 'x')

btn_orange = Button(root, bg = "#ff7d00", command = lambda: get_color('Оранжевый', '#ff7d00'))
btn_orange.pack(fill = 'x')

btn_yellow = Button(root, bg = "#ffff00", command = lambda: get_color('Желтый', '#ffff00'))
btn_yellow.pack(fill = 'x')

'''
Остальные кнопки по цветам радуги добавляются добавлением соответствующих кнопок
'''

root.mainloop()
