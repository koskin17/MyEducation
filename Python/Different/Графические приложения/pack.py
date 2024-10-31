from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')

'''
Frame можно использовать для разметки окна.
Т.е. как-бы расчертить окно и уже в каждом Frame размещать свои виджеты

f_top = Frame(root)
f_top.pack()
f_bottom = Frame(root)
f_bottom.pack()

l1 = Label(f_top, text = "1", font = "15", fg = "#fff", bg = "#3498db", width = 8, height = 4).pack(side = LEFT)
l2 = Label(f_top, text = "2", font = "15", fg = "#fff", bg = "#2ecc71", width = 8, height = 4).pack(side = LEFT)
l3 = Label(f_bottom, text = "3", font = "15", fg = "#fff", bg = "#f1c40f", width = 8, height = 4).pack(side = LEFT)
l4 = Label(f_bottom, text = "4", font = "15", fg = "#fff", bg = "#34495e", width = 8, height = 4).pack(side = LEFT)
'''

'''
Метод LabelFrame позволяет делать рамку с подзаголовком.
При помощи свойств padx и pady задаются отступы внутри Frame по осям.
'''
f_top = LabelFrame(root, text = "Top Frame", padx = 10, pady = 10)
'''
Для отступов фреймов друг от друга свойства padx и pady применяются
уже для упаковщика pack
'''
f_top.pack(pady = 10)
f_bottom = LabelFrame(root, text = "Bottom Frame", padx = 10, pady = 10)

l1 = Label(f_top, text = "1", font = "15", fg = "#fff", bg = "#3498db", width = 8, height = 4).pack(side = LEFT)
l2 = Label(f_top, text = "2", font = "15", fg = "#fff", bg = "#2ecc71", width = 8, height = 4).pack(side = LEFT)
l3 = Label(f_bottom, text = "3", font = "15", fg = "#fff", bg = "#f1c40f", width = 8, height = 4).pack(side = LEFT)
l4 = Label(f_bottom, text = "4", font = "15", fg = "#fff", bg = "#34495e", width = 8, height = 4).pack(side = LEFT)

root.mainloop()
