from tkinter import *

root = Tk()
root.geometry('600x400+450+250')

l1 = Label(root, text = "Hello world!", bg = "#3498db",
           fg = "#fff", font = "16", padx = 20, pady = 8)
l1.place(x = 0, y = 0)

l2 = Label(root, text = "Hello world!", bg = "#2ecc71",
           fg = "#fff", font = "16", padx = 20, pady = 8)
l2.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root2 = Tk()

btn1 = Button(root2, text = "Button1", bg = "#3498db",
           fg = "#fff", font = "16", padx = 20, pady = 8)
btn1.place(x = 0, y = 0)

btn2 = Button(root2, text = "Button2", bg = "#2ecc71",
           fg = "#fff", font = "16", padx = 20, pady = 8)
btn2.place(relx = 0.5, rely = 0.5, anchor = CENTER)

btn3 = Button(root2, text = "Button3", bg = "#f1c40f",
           fg = "#fff", font = "16", padx = 20, pady = 8)
btn3.place(relx = 1, rely = 1, anchor = SE)

'''
Квадрат Малевича
'''

root3 = Tk()
l = Label(root3, bg = '#000')
l.place(relheight = 0.8, relwidth = 0.8, relx = 0.1, rely = 0.1) 

root.mainloop()
