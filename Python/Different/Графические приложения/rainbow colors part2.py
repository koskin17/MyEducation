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

colors = {
    "#ff0000": "Красный",
    "#ff7d00": "Оранжевый",
    "#ffff00": "Желтый",
    "#00ff00": "Зеленый",
    "#007dff": "Голубой",
    "#0000ff": "Синий",
    "#7d00ff": "Фиолетовый"
    }

for color_code, color_name in colors.items():
    but = Button(root, bg = color_code, command = lambda text = color_name, hex_code = color_code: get_color(text, hex_code))
    but.pack(fill = X)
    
root.mainloop()
